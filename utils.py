import re

def clean_text(text):
    """텍스트를 정리하고 불필요한 요소 제거"""
    # 불필요한 공백 및 특수문자 제거
    text = re.sub(r'\s+', ' ', text)  # 다중 공백을 하나의 공백으로 변환
    text = re.sub(r'\[[^]]*\]', '', text)  # 괄호 안에 있는 내용 제거 (예: [1], [참조] 등)
    text = re.sub(r'\d+', '', text)  # 숫자 제거
    return text.strip()
