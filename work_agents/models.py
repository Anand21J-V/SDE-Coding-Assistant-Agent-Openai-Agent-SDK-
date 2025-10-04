from pydantic import BaseModel
from typing import List

class CodingPlan(BaseModel):
    problem: str
    subtasks: List[str]
    tech_stack: List[str]

class CodeOutput(BaseModel):
    filename: str
    code: str
    explanation: str
