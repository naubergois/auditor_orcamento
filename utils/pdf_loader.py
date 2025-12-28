import io
import pypdf

def extract_text_from_pdf(pdf_file) -> str:
    """
    Extracts text from a PDF file (bytes or file-like object).
    
    Args:
        pdf_file: A file-like object containing the PDF data.
        
    Returns:
        str: The extracted text from the PDF.
    """
    try:
        reader = pypdf.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        return f"Erro ao ler PDF: {str(e)}"
