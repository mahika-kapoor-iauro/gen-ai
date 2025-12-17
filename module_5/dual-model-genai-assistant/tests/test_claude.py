import pytest
from src.models.claude import ClaudeClient

@pytest.fixture
def claude_client():
    return ClaudeClient(api_key="test_api_key")

def test_send_research_topic(claude_client):
    response = claude_client.send_research_topic("What is the impact of climate change?")
    assert response is not None
    assert "structured_output" in response

def test_receive_structured_output(claude_client):
    response = claude_client.receive_structured_output("test_context")
    assert response is not None
    assert isinstance(response, dict)

def test_manage_conversational_context(claude_client):
    initial_context = "Initial context"
    claude_client.manage_conversational_context(initial_context)
    assert claude_client.context == initial_context

    new_context = "Updated context"
    claude_client.manage_conversational_context(new_context)
    assert claude_client.context == new_context

def test_error_handling(claude_client):
    with pytest.raises(ValueError):
        claude_client.send_research_topic("")  # Test with empty topic