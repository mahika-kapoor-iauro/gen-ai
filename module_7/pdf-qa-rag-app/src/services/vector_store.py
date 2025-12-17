class VectorStore:
    def __init__(self):
        self.store = {}

    def add_embedding(self, key, embedding):
        self.store[key] = embedding

    def get_embedding(self, key):
        return self.store.get(key)

    def all_embeddings(self):
        return self.store.items()

    def clear(self):
        self.store.clear()