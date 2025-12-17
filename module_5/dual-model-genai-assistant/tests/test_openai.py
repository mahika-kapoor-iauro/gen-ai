import pytest
from src.models.openai import OpenAIClient

@pytest.fixture
def openai_client():
    return OpenAIClient(api_key="test_api_key")

def test_generate_summary(openai_client):
    research_data = "This is a test research topic."
    summary = openai_client.generate_summary(research_data)
    assert isinstance(summary, str)
    assert len(summary) > 0

def test_generate_creative_output(openai_client):
    prompt = "Write a short story about a robot learning to dance."
    creative_output = openai_client.generate_creative_output(prompt)
    assert isinstance(creative_output, str)
    assert len(creative_output) > 0

def test_invalid_api_key():
    client = OpenAIClient(api_key="invalid_key")
    with pytest.raises(Exception) as exc_info:
        client.generate_summary("Test")
    assert "Invalid API key" in str(exc_info.value)