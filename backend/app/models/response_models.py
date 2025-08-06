from typing import List
from pydantic import BaseModel, Field

class ResumeReviewResponse(BaseModel):
    score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Match score between 0 (no match) and 1 (perfect match)"
    )
    missing_keywords: List[str] = Field(
        default_factory=list,
        description="Keywords present in the job description but not found in the resume"
    )
    suggestions: List[str] = Field(
        default_factory=list,
        description="Actionable suggestions to improve resume alignment"
    )