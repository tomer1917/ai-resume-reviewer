from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from ..services.resume_parser import extract_text_from_pdf
from ..models.response_models import ResumeReviewResponse
from ..services.resume_analyzer import analyze_resume

router = APIRouter()
@router.post(
    "/review",
    response_model=ResumeReviewResponse,
    summary= "review a resume PDF against a job description"
)
async def review_resume(
        resume_file: UploadFile = File(...),
        job_description: str = Form(...)
)-> ResumeReviewResponse:
    """check if the given file is a pdf, extract its text, analyze it"""
    if resume_file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    pdf_bytes = await resume_file.read()
    resume_text = extract_text_from_pdf(pdf_bytes)


    score, missing_keywords, suggestions = analyze_resume(resume_text=resume_text, job_description=job_description)

    return ResumeReviewResponse(score=score, missing_keywords=missing_keywords, suggestions=suggestions)

