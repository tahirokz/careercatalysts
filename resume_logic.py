from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

def compare_resume(resume_text, job_description):
    llm = ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))
    template = """
    You are an AI assistant tasked with analyzing resumes and job descriptions only. 
    DO NOT answer unrelated questions.

    Compare the given RESUME and JOB DESCRIPTION. Provide:
    - A compatibility score out of 100.
    - The strengths of the resume.
    - The weaknesses of the resume.

    If the input is not relevant to resumes or job descriptions, respond with:
    'I only analyze resumes and job descriptions. Please provide valid inputs.'

    RESUME:
    {resume}

    JOB DESCRIPTION:
    {job_description}
    """
    prompt = PromptTemplate(input_variables=["resume", "job_description"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"resume": resume_text, "job_description": job_description})