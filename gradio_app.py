import gradio as gr
import requests
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

API_URL = "http://127.0.0.1:8000/analyze"

def analyze(file, job_description):
    logger.info("Starting the analysis process.")
    
    # Check if the job description and file are provided
    if not job_description.strip():
        logger.error("Job Description cannot be empty.")
        return "Error: Job Description cannot be empty."
    if file is None:
        logger.error("No file uploaded. Please upload a valid resume PDF file.")
        return "Error: Please upload a valid resume PDF file."

    # Check file type (PDF only)
    if not file.name.endswith(".pdf"):
        logger.error("Uploaded file is not a PDF.")
        return "Error: Please upload a PDF file."

    # Prepare file data for API
    files = {"file": (file.name, file, "application/pdf")}
    
    try:
        logger.info("Sending request to the API...")
        response = requests.post(API_URL, files=files, data={"job_description": job_description})
        
        # Log status and content of the response
        logger.info(f"Received response with status code {response.status_code}")
        
        # Check if the response status is not successful
        if response.status_code != 200:
            logger.error(f"Error from API: {response.json().get('detail', 'Unknown error')}")
            return response.json().get("detail", "Error occurred while processing.")
        
        # Log successful analysis completion
        logger.info("Analysis completed successfully.")
        return response.json().get("analysis", "No analysis provided.")
    except requests.exceptions.RequestException as e:
        # Log any exception raised during the request
        logger.exception("Could not connect to the API.")
        return f"Error: Could not connect to the API. Details: {e}"

with gr.Blocks(
    title="Career Catalyst: Resume Analyzer",
    theme=gr.themes.Soft(
        primary_hue="teal",
        secondary_hue="indigo",
        neutral_hue="zinc",
        font=["Roboto", "ui-sans-serif", "system-ui", "sans-serif"],
    ),
    css="""
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    :root {
        --primary-color: #14b8a6;
        --secondary-color: #6366f1;
        --background-color: #f8fafc;
        --text-color: #1e293b;
    }
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    .container { 
        max-width: 1200px; 
        margin: 2rem auto; 
        padding: 2rem;
        background: white;
        border-radius: 1rem;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    #header {
        text-align: center;
        margin-bottom: 2rem;
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    #header h1 { 
        font-size: 3.5rem; 
        font-weight: 700; 
        color: var(--primary-color);
        margin-bottom: 1rem;
        letter-spacing: -1px;
    }
    
    #header p { 
        font-size: 1.25rem; 
        color: var(--text-color); 
        margin-bottom: 1rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    .gradio-button.primary-btn { 
        background-color: var(--primary-color);
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
        padding: 0.75rem 1.5rem;
        border-radius: 0.5rem;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 6px rgba(20, 184, 166, 0.25);
    }
    
    .gradio-button.primary-btn:hover { 
        transform: translateY(-2px);
        box-shadow: 0 7px 14px rgba(20, 184, 166, 0.3);
        background-color: #0d9488;
    }
    
    .input-box { 
        border: 2px solid #e2e8f0; 
        border-radius: 0.5rem;
        transition: all 0.3s ease;
        background-color: #f8fafc;
    }
    
    .input-box:focus-within {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(20, 184, 166, 0.2);
    }
    
    .output-box { 
        background-color: #f1f5f9;
        border: 2px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    
    .output-box:hover {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    #footer { 
        font-size: 0.9rem; 
        color: #64748b; 
        text-align: center; 
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 2px solid #e2e8f0;
    }
    
    #footer a { 
        color: var(--primary-color); 
        text-decoration: none; 
        font-weight: 500;
        transition: color 0.3s ease;
    }
    
    #footer a:hover { 
        color: var(--secondary-color);
    }
    
    .gr-form {
        border: none !important;
        background: transparent !important;
    }
    
    .gr-box {
        border-radius: 0.5rem !important;
        border: 2px solid #e2e8f0 !important;
        box-shadow: none !important;
    }
    
    .gr-input {
        border-radius: 0.5rem !important;
    }
    
    .gr-button {
        border-radius: 0.5rem !important;
    }
    
    .gr-panel {
        border-radius: 0.5rem !important;
    }
    
    @media (max-width: 640px) {
        #header h1 {
            font-size: 2.5rem;
        }
        
        #header p {
            font-size: 1rem;
        }
        
        .container {
            padding: 1rem;
        }
    }
    """
) as interface:
    gr.Markdown(
        """
        <div id="header">
            <h1>🚀 Career Catalyst</h1>
            <p>Supercharge your job search with our AI-powered Resume Analyzer. Get instant feedback on how your resume aligns with job descriptions, highlighting your strengths and areas for improvement.</p>
        </div>
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            resume_upload = gr.File(
                label="📄 Upload Your Resume",
                file_types=[".pdf"],
                elem_id="resume-upload"
            )
            job_description_input = gr.Textbox(
                label="💼 Job Description",
                placeholder="Paste the job description here...",
                lines=8,
                elem_classes="input-box"
            )
            analyze_button = gr.Button("🔍 Analyze Resume", elem_classes="primary-btn")

        with gr.Column(scale=1):
            gr.Markdown("### 📊 Analysis Results")
            analysis_output = gr.Textbox(
                label="",
                placeholder="Your personalized analysis will appear here...",
                lines=15,
                elem_classes="output-box"
            )

    analyze_button.click(
        fn=analyze,
        inputs=[resume_upload, job_description_input],
        outputs=analysis_output,
    )

    gr.Markdown(
        """
        <div id="footer">
            <p><strong>📌 Pro Tip:</strong> For the most accurate results, ensure your resume is in PDF format and provide a detailed job description.</p>
            <p>Powered by AI 🤖 | Built with 💖 using <a href="https://gradio.app" target="_blank">Gradio</a> | 
            <a href="#" target="_blank">Privacy Policy</a> | 
            <a href="#" target="_blank">Terms of Service</a></p>
        </div>
        """
    )

logger.info("Launching the Career Catalyst interface...")
interface.launch()

