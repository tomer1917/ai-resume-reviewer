import os
import json
from typing import Tuple, List

from dotenv import load_dotenv
import openai


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def analyze_resume(
    resume_text: str,
    job_description: str
) -> Tuple[float, List[str], List[str]]:
    prompt = f"""
    You are an expert hiring manager and HR specialist.
    Compare the following candidate resume to the job description.
    Return ONLY valid JSON with three keys:
      1. score — a number between 0.0 (no match) and 1.0 (perfect match)
      2. missing_keywords — an array of strings for skills/terms in the job description but absent in the resume
      3. suggestions — an array of reasonable improvement suggestions

    Resume:
    \"\"\"
    {resume_text}
    \"\"\"

    Job Description:
    \"\"\"
    {job_description}
    \"\"\"
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a precise JSON generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=500
    )

    content = response.choices[0].message.content.strip()
    data = json.loads(content)

    return (
        float(data["score"]),
        list(data["missing_keywords"]),
        list(data["suggestions"])
    )