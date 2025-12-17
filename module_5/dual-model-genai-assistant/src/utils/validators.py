def is_valid_api_key(api_key):
    """Validate the API key format."""
    return isinstance(api_key, str) and len(api_key) > 0

def is_valid_input(input_data):
    """Validate user input for expected format."""
    return isinstance(input_data, str) and len(input_data.strip()) > 0

def is_valid_response(response):
    """Validate the structure of the API response."""
    return isinstance(response, dict) and 'data' in response and 'status' in response

def is_valid_task(task):
    """Validate the task structure."""
    return isinstance(task, dict) and 'id' in task and 'description' in task and 'completed' in task