import streamlit as st
import asyncio

# Import Runner from the library
from agents import Runner

# Import local modular agents
from work_agents.planner import planner_agent
from work_agents.coder import coder_agent
from work_agents.reviewer import reviewer_agent
from work_agents.models import CodingPlan, CodeOutput

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="💻 SDE Coding Assistant (Gemini)", layout="wide")
st.title("💻 SDE Coding Agent Assistant")
st.markdown(
    "Streamline your development with planning, coding, and reviewing agents powered by **Gemini**."
)

# ---------------- SESSION STATE ----------------
if "code_plan" not in st.session_state:
    st.session_state.code_plan = None
if "generated_code" not in st.session_state:
    st.session_state.generated_code = None
if "code_review" not in st.session_state:
    st.session_state.code_review = None

# ---------------- HELPER ASYNC FUNCTIONS ----------------
async def run_agent(agent, input_text):
    """Run an agent asynchronously and return the final output."""
    result = await Runner.run(agent, input_text)
    return result.final_output

def run_agent_sync(agent, input_text, session_key):
    """Run async agent safely inside Streamlit (handles ScriptRunner threads)."""
    try:
        # Python >=3.10: use running loop if exists
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # No loop in this thread, create a new one
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    result = loop.run_until_complete(run_agent(agent, input_text))
    st.session_state[session_key] = result

# ---------------- INPUT ----------------
with st.sidebar:
    st.header("📥 Problem Input")
    problem_input = st.text_area("Describe your coding problem or feature request:")

    if st.button("Plan & Build", disabled=not problem_input):
        st.session_state.generated_code = None
        st.session_state.code_review = None
        run_agent_sync(planner_agent, problem_input, "code_plan")

# ---------------- DISPLAY PLAN ----------------
if st.session_state.code_plan:
    plan: CodingPlan = st.session_state.code_plan
    st.markdown(f"### 📋 Plan for: `{plan.problem}`")
    st.markdown("**🧩 Subtasks:**")
    for s in plan.subtasks:
        st.markdown(f"- {s}")
    st.markdown("**🧪 Suggested Tech Stack:**")
    st.markdown(", ".join(plan.tech_stack))

    if plan.subtasks:
        selected_task = st.selectbox("Select a subtask to implement:", plan.subtasks)

        if st.button("Generate Code for Task"):
            input_text = f"Task: {selected_task}\nTech stack: {plan.tech_stack}"
            run_agent_sync(coder_agent, input_text, "generated_code")
    else:
        st.warning("⚠️ No subtasks were returned by the planner agent.")

# ---------------- DISPLAY CODE ----------------
if st.session_state.generated_code:
    result: CodeOutput = st.session_state.generated_code
    st.markdown(f"### 🧾 Generated File: `{result.filename}`")
    st.code(result.code, language=result.filename.split('.')[-1])
    st.markdown(f"🧠 **Explanation:** {result.explanation}")

    if st.button("🔍 Review Code"):
        run_agent_sync(reviewer_agent, result.code, "code_review")

# ---------------- DISPLAY REVIEW ----------------
if st.session_state.code_review:
    st.markdown("### 🛠️ Review Suggestions")
    st.markdown(st.session_state.code_review)
