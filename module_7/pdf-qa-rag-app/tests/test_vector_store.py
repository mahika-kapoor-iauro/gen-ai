import pytest
from src.services.vector_store import VectorStore

def test_vector_store_initialization():
    vector_store = VectorStore()
    assert vector_store is not None

def test_add_and_retrieve_embedding():
    vector_store = VectorStore()
    sample_embedding = [0.1, 0.2, 0.3]
    vector_store.add_embedding("test_id", sample_embedding)
    
    retrieved_embedding = vector_store.retrieve_embedding("test_id")
    assert retrieved_embedding == sample_embedding

def test_retrieve_non_existent_embedding():
    vector_store = VectorStore()
    retrieved_embedding = vector_store.retrieve_embedding("non_existent_id")
    assert retrieved_embedding is None

def test_embedding_count():
    vector_store = VectorStore()
    vector_store.add_embedding("id_1", [0.1, 0.2, 0.3])
    vector_store.add_embedding("id_2", [0.4, 0.5, 0.6])
    
    assert vector_store.embedding_count() == 2

def test_clear_embeddings():
    vector_store = VectorStore()
    vector_store.add_embedding("id_1", [0.1, 0.2, 0.3])
    vector_store.clear_embeddings()
    
    assert vector_store.embedding_count() == 0