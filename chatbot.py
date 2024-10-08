from pdf_processing import extract_text_from_pdf, preprocess_text
from nlp import answer_question

def chatbot(pdf_file):
    # PDF에서 텍스트 추출 및 전처리
    document_text = extract_text_from_pdf(pdf_file)
    document_text = preprocess_text(document_text)
    
    print("PDF에서 텍스트를 추출하고 전처리했습니다.")
    print("질문을 입력하면 챗봇이 답변합니다. 종료하려면 'exit'를 입력하세요.\n")

    while True:
        question = input("질문을 입력하세요: ")
        if question.lower() == "exit":
            print("챗봇을 종료합니다.")
            break
        # 질문에 해당하는 답변을 가져옴
        answer = answer_question(document_text, question)
        print(f"답변: {answer}\n")

if __name__ == "__main__":
    # PDF 파일 경로 입력
    pdf_file_path = 'q_info_tech_whitepaper_2023.pdf'
    chatbot(pdf_file_path)
