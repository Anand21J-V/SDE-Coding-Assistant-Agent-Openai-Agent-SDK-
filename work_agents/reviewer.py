from agents import Agent
from work_agents.config import gemini_model

reviewer_agent = Agent(
    name="Code Reviewer",
    instructions="Review code and suggest improvements, optimizations, or warnings.",
    model=gemini_model,
)
