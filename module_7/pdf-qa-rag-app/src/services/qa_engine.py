class QAEngine:
    def __init__(self, llm, vector_store):
        self.llm = llm
        self.vector_store = vector_store

    def answer_question(self, question):
        # Retrieve relevant documents from the vector store
        relevant_docs = self.vector_store.retrieve(question)
        
        # Generate an answer using the language model
        answer = self.llm.generate_answer(question, relevant_docs)
        
        return answer