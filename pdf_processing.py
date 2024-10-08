from PyPDF2 import PdfReader
from utils import clean_text

def extract_text_from_pdf(pdf_file):
    """PDF 파일에서 텍스트 추출"""
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

def preprocess_text(text):
    """추출된 텍스트를 전처리"""
    cleaned_text = clean_text(text)
    return cleaned_text
