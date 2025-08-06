from pydantic import BaseModel, Field
class ResumeReviewResquest(BaseModel):
    resume_text: str = Field(
        ...,
        description="Text of the candidate's resumes"
    )
    job_description: str = Field(
        ...,
        description="Text of the wanted job's description"
    )


