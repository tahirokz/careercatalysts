from fastapi import FastAPI, UploadFile, Form, HTTPException
from pdf_processor import extract_text_from_pdf
from resume_logic import compare_resume
import gradio 
import gradio_app  # Import gradio.py from the same directory
import uvicorn


app = FastAPI(title="Career Catalyst API")

# Input validation helper
def validate_job_description(job_description):
    required_keywords = ["responsibilities", "skills", "experience", "requirements"]
    if not any(keyword in job_description.lower() for keyword in required_keywords):
        raise HTTPException(status_code=400, detail="Invalid Job Description: Must include responsibilities, skills, or experience.")

@app.post("/analyze/")
async def analyze_resume(file: UploadFile, job_description: str = Form(...)):
    # Validate job description
    validate_job_description(job_description)

    # Extract resume text
    resume_text = extract_text_from_pdf(file.file)
    if len(resume_text.split()) < 50:  # Ensures resume is substantial
        raise HTTPException(status_code=400, detail="Invalid Resume: The uploaded file seems too short.")

    # Run analysis
    analysis = compare_resume(resume_text, job_description)
    return {"analysis": analysis}