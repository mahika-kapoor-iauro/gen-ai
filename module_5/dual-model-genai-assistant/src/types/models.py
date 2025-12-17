from pydantic import BaseModel
from typing import List, Optional

class ResearchOutput(BaseModel):
    title: str
    summary: str
    details: str
    references: List[str]

class UserInput(BaseModel):
    topic: str
    context: Optional[str] = None

class AssistantResponse(BaseModel):
    output: ResearchOutput
    model_used: str
    timestamp: str