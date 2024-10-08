from transformers import BertTokenizer, BertModel
import torch

# Pretrained BERT 모델과 토크나이저 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained('bert-base-multilingual-cased')

def get_bert_embedding(text):
    """텍스트를 BERT 임베딩으로 변환"""
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)

def answer_question(document_text, question):
    """BERT 기반으로 질문에 대한 답변 제공"""
    corpus = document_text.split(". ")  # 문단을 문장으로 나눔
    question_embedding = get_bert_embedding(question)
    
    # 코사인 유사도로 유사한 문장을 찾음
    similarities = []
    for sentence in corpus:
        sentence_embedding = get_bert_embedding(sentence)
        similarity = torch.nn.functional.cosine_similarity(question_embedding, sentence_embedding)
        similarities.append(similarity.item())
    
    closest_idx = similarities.index(max(similarities))
    return corpus[closest_idx]
