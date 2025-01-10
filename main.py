import logging
import os
from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pdf_processor import extract_text_from_pdf
from resume_logic import compare_resume
from dotenv import load_dotenv
import openai
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set. Please configure it in the .env file.")

openai.api_key = OPENAI_API_KEY

app = FastAPI(title="Career Catalyst API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
async def root():
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to Career Catalyst API"}

# Input validation helper
def validate_job_description(job_description):
    required_keywords = ["responsibilities", "skills", "experience"]
    if not any(keyword in job_description.lower() for keyword in required_keywords):
        logger.error("Invalid job description provided.")
        raise HTTPException(
            status_code=400,
            detail="Invalid Job Description: Must include responsibilities, skills, or experience.",
        )
    logger.info("Job description validated successfully.")

@app.post("/analyze/")
async def analyze_resume(file: UploadFile, job_description: str = Form(...)):
    try:
        logger.info("Starting resume analysis.")
        
        # Validate job description
        validate_job_description(job_description)
        
        # Extract text from the uploaded resume PDF
        logger.info("Extracting text from the uploaded resume.")
        resume_text = extract_text_from_pdf(file.file)
        
        # Check if resume text is too short
        if len(resume_text.split()) < 50:
            logger.warning("Uploaded resume seems too short.")
            raise HTTPException(
                status_code=400,
                detail="Invalid Resume: The uploaded file seems too short.",
            )
        
        # Compare resume with job description using OpenAI
        logger.info("Comparing resume with job description using OpenAI.")
        analysis = compare_resume(resume_text, job_description)
        
        logger.info("Resume analysis completed successfully.")
        return {"analysis": analysis}
    
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.exception("An unexpected error occurred during the resume analysis.")
        return {"detail": f"An unexpected error occurred: {str(e)}"}
