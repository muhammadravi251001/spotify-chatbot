import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class QnAChatbot:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.history = [{"role": "user", "parts": data}]

    def ask_question(self, query):
        chat = self.model.start_chat(history=self.history)
        response = chat.send_message(query)
        self.history.append({"role": "user", "content": query})
        response_content = response.text
        self.history.append({"role": "assistant", "content": response_content})
        return response_content

def quality_score(question, response):
    embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    question_embedding = torch.tensor(embedder.encode([question])[0])
    response_embedding = torch.tensor(embedder.encode([response])[0])
    score = cosine_similarity([question_embedding], [response_embedding])[0][0]
    return score
