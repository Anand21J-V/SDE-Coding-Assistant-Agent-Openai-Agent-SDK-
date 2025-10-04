from agents import Agent
from work_agents.config import gemini_model
from work_agents.models import CodingPlan

planner_agent = Agent(
    name="Planner Agent",
    instructions="""
You're a software planner. Given a requirement, break it into components:
1. Identify key features.
2. Suggest relevant tech stack/tools.

Respond in JSON:
{
  "problem": "<problem>",
  "subtasks": ["task1", "task2"],
  "tech_stack": ["Python", "Flask", ...]
}
""",
    model=gemini_model,
    output_type=CodingPlan,
)
