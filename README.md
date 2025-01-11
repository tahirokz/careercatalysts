# Career-Catalysts
This is Computational intelligence mini project on llm based application
Explanation of the Provided Files:

File 1: main.py
This file sets up a REST API using FastAPI. Here's what it does:
Imports Libraries: Handles file uploads, environment variables, and HTTP exceptions.
Loads Environment Variables: Sets up the OpenAI API key from the .env file.
Defines a Validation Function: Ensures the job description includes key elements like responsibilities, skills, etc.
Defines the /analyze/ Endpoint:
Takes a resume (PDF file) and job description (string) as inputs.
Validates the job description and extracts text from the PDF using extract_text_from_pdf.
Ensures the resume has enough content (at least 50 words).
Compares the resume and job description using the compare_resume function.
Returns the analysis as a JSON response.
Runs the Server: Launches the API on port 8000 using uvicorn.


File 2: resume_logic.py
This file contains the logic for analyzing resumes:
Imports Libraries: Uses LangChain and OpenAI for LLM capabilities.
Defines compare_resume Function:
Initializes a GPT-4 instance using the OpenAI API key.
Sets up a prompt template that guides the LLM to compare resumes and job descriptions.
The AI evaluates compatibility, strengths, and weaknesses, then returns a structured response.


File 3: pdf_processor.py
This file processes PDF files:
Imports PyPDF2: A library for reading PDF files.
Defines extract_text_from_pdf Function:
Extracts text from all pages of a given PDF file.
Concatenates the extracted text into a single string for further analysis.


File 4: gradio_app.py
This file sets up a user-friendly interface using Gradio:
Imports Libraries: Uses requests for API communication and gradio for the UI.
Defines analyze Function:
Validates that both a resume file and a job description are provided.
Sends a POST request to the FastAPI endpoint (/analyze/) with the resume and job description.
Handles errors and displays the analysis results.
Builds the Gradio Interface:
Creates a user-friendly UI with a file uploader for resumes and a text box for job descriptions.
Includes custom CSS for styling.


How to Use the Application:

# Career Catalyst

Career Catalyst is an advanced AI-driven platform designed to revolutionize the hiring process. It seamlessly evaluates resumes against job descriptions, providing detailed insights to help employers and job seekers alike. With its intuitive interface and cutting-edge AI, Career Catalyst simplifies resume screening, enhances decision-making, and improves hiring efficiency.


## 🚀 Features
Resume Analysis: Upload resumes in PDF format for detailed evaluation.
Job Description Comparison*: Analyze resumes against specific job descriptions.
Actionable Insights:
Compatibility score out of 100.
Key strengths and weaknesses identified.
User-Friendly Interface: Intuitive Gradio UI for seamless interaction.
Error Handling: Clear and actionable feedback for invalid inputs.


## 🛠 Technologies Used
FastAPI: High-performance API framework for backend development.
Gradio: Interactive frontend for a user-friendly experience.
LangChain: Framework for language model integration.
OpenAI GPT-4: State-of-the-art language model for resume analysis.
PyPDF2: Reliable PDF processing for text extraction.


## 📦 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo-url.git
cd career-catalyst

1. Input Requirements:
Resume: Upload a PDF file containing the resume.
Job Description: Enter a detailed job description in the text box.

2. Analysis Process:
The resume text is extracted using pdf_processor.py.
The resume_logic.py file uses GPT-4 to compare the resume and job description.
Results are displayed via the Gradio interface, including:
Compatibility score out of 100.
Strengths and weaknesses of the resume.

3. API Integration:
The Gradio app communicates with the FastAPI server via the /analyze/ endpoint.



# Career Catalyst

Career Catalyst is an AI-powered tool designed to streamline the hiring process by analyzing resumes and job descriptions. It provides compatibility scores, highlights strengths, and identifies weaknesses in resumes.

## Features
Upload resumes in PDF format.
Compare resumes with job descriptions.
Receive a detailed analysis, including:
Compatibility score.
Resume strengths.
Resume weaknesses.
User-friendly Gradio interface for seamless interaction.

## Technologies Used
FastAPI: Backend API development.
Gradio*: Frontend user interface.
LangChain: Language model orchestration.
OpenAI GPT-4: Resume and job description analysis.
PyPDF2: PDF text extraction.

## Installation and Setup

1. Clone the Repository:

2. Install Dependencies:
pip install -r requirements.txt


3. Set Up Environment Variables:
Create a .env file in the root directory.
Add your OpenAI API key:
OPENAI_API_KEY=your_api_key


4. Run the FastAPI Server:
python main.py


5. Launch the Gradio Interface:
python gradio_app.py


6. Access the Application:
Open your browser and navigate to the Gradio URL displayed in the terminal.




Usage
1. Upload a resume in PDF format.
2. Enter a detailed job description.
3. Click the Analyze button to receive a comprehensive analysis.



API Endpoints
POST /analyze/:
Inputs:
file (PDF resume)
job_description (string)
Outputs:

JSON containing compatibility score, strengths, and weaknesses.




Example

Request:

curl -X POST "http://127.0.0.1:8000/analyze/" \
-F "file=@resume.pdf" \
-F "job_description=Senior Software Engineer with Python expertise"

Response:

{
  "analysis": {
    "compatibility_score": 85,
    "strengths": ["Strong Python experience", "Team leadership skills"],
    "weaknesses": ["Lack of cloud technology experience"]
  }
}

License

This project is licensed under the MIT License.
Let me know if you need further assistance!
