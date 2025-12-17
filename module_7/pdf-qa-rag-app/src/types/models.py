class QuestionAnsweringModel:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

class PDFDocument:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

class Embedding:
    def __init__(self, vector: list):
        self.vector = vector

class Vector:
    def __init__(self, id: str, embedding: Embedding):
        self.id = id
        self.embedding = embedding

class QAResult:
    def __init__(self, question: str, answer: str, confidence: float):
        self.question = question
        self.answer = answer
        self.confidence = confidence