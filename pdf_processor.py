import logging
from PyPDF2 import PdfReader

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_file_path):
    """
    Extracts text from a PDF file.
    :param pdf_file_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    try:
        logger.info("Starting PDF text extraction.")
        # Open the PDF file
        with open(pdf_file_path, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            # Extract text from all pages
            text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
            if not text.strip():
                raise ValueError("The PDF contains no extractable text.")
            logger.info("PDF text extraction completed successfully.")
            return text
    except Exception as e:
        logger.exception("Error extracting text from PDF.")
        raise ValueError(f"Error extracting text from PDF: {str(e)}")

# Example usage
if __name__ == "_main_":
    try:
        # Replace 'example.pdf' with your test PDF file path
        pdf_text = extract_text_from_pdf("example.pdf")
        print("Extracted Text:")
        print(pdf_text)
    except ValueError as e:
        logger.error(e)