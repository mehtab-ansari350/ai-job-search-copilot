"""
Resume Parser Module

Responsible for:
1. Reading PDF resumes
2. Extracting text 
"""

from pypdf import pdfReader 

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.
    
    Args:
        pdf_path (str): Path to PDF file
    
    Returns:
        str: Extracted text
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"
    
    return text

