import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/analyze/"

def analyze(file, job_description):
    if not job_description.strip():
        return "Error: Job Description cannot be empty."
    if file is None:
        return "Error: Please upload a valid resume PDF file."

    files = {"file": (file.name, file, "application/pdf")}
    response = requests.post(API_URL, files=files, data={"job_description": job_description})
    
    if response.status_code != 200:
        return response.json().get("detail", "Error occurred.")
    return response.json().get("analysis", "Error in analysis.")

with gr.Blocks(title="Career Catalyst", css="""
    body {
        background-color: #f7f9fc; /* Light blue background */
        font-family: 'Arial', sans-serif;
    }
    #header h1 {
        color: #4CAF50; /* Green header */
        font-weight: bold;
    }
    #header p {
        color: #555; /* Subtle gray description */
    }
    #analyze-button {
        background-color: #4CAF50; /* Green button */
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    #analyze-button:hover {
        background-color: #45a049; /* Slightly darker green on hover */
    }
    .gr-file, .gr-textbox {
        border: 1px solid #ddd; /* Light gray border for inputs */
        border-radius: 5px;
        padding: 10px;
    }
    .gr-markdown div {
        color: #333; /* Darker text for footer */
    }
""") as interface:
    with gr.Row():
        gr.Markdown(
            """
            <h1 style="text-align: center;">Career Catalyst: Resume Analyzer</h1>
            <p style="text-align: center;">
                Upload your resume and provide a job description to analyze compatibility, strengths, and weaknesses.
            </p>
            <hr>
            """,
            elem_id="header",
        )

    with gr.Row():
        with gr.Column():
            resume_upload = gr.File(label="Upload Resume (PDF)", file_types=[".pdf"])
            job_description_input = gr.Textbox(
                label="Job Description", 
                placeholder="Paste the job description here...",
                lines=5,
            )
        with gr.Column():
            analysis_output = gr.Textbox(
                label="Analysis Result",
                placeholder="The analysis will appear here...",
                lines=10,
                interactive=False,
            )

    analyze_button = gr.Button(
        "Analyze Now",
        elem_id="analyze-button",
    )
    analyze_button.click(
        fn=analyze,
        inputs=[resume_upload, job_description_input],
        outputs=analysis_output,
    )

    with gr.Row():
        gr.Markdown(
            """
            <div style="text-align: center; font-size: 14px; margin-top: 10px;">
                <strong>Note:</strong> Ensure your resume is in PDF format, and the job description is detailed for accurate analysis.  
                Built with <a href="https://gradio.app" target="_blank">Gradio</a>.
            </div>
            """,
            elem_id="footer",
        )

interface.launch()