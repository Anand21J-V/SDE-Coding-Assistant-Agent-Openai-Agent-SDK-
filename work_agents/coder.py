from agents import Agent
from work_agents.config import gemini_model
from work_agents.models import CodeOutput

coder_agent = Agent(
    name="Code Generator",
    instructions="""
Given a task and tech stack, generate clear code and explain it.

Respond in this format:
{
  "filename": "file.py",
  "code": "...",
  "explanation": "..."
}
""",
    model=gemini_model,
    output_type=CodeOutput,
)
