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

gr.Interface(
    fn=analyze,
    inputs=[gr.File(label="Upload Resume (PDF)"), gr.Textbox(label="Job Description", lines=5)],
    outputs=gr.Textbox(label="Analysis Result", lines=10),
    title="Career Catalyst: Resume Analyzer",
).launch()