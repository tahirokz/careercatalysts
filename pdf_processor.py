import logging
from PyPDF2 import PdfReader

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.
    :param pdf_file: A file-like object containing the PDF.
    :return: Extracted text as a string.
    """
    try:
        logger.info("Starting PDF text extraction.")
        reader = PdfReader(pdf_file)
        # Extract text from all pages
        text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        if not text.strip():
            raise ValueError("The PDF contains no extractable text.")
        logger.info("PDF text extraction completed successfully.")
        return text
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Replace 'example.pdf' with your test PDF file path
        with open("example.pdf", "rb") as pdf_file:
            pdf_text = extract_text_from_pdf(pdf_file)
            print("Extracted Text:")
            print(pdf_text)
    except ValueError as e:
        logger.error(str(e))
    except FileNotFoundError:
        logger.error("Error: PDF file not found.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")

