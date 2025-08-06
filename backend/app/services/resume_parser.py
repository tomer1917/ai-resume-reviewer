import io
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    parse a pdf bytes into string
    """
    with io.BytesIO(pdf_bytes) as pdf_file:
        text = extract_text(pdf_file)
    return text