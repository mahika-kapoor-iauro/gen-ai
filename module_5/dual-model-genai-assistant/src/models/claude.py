class ClaudeClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.conversation_context = []

    def send_research_topic(self, topic):
        # Logic to send the research topic to the Claude Assistant API
        # and update the conversation context
        pass

    def receive_structured_output(self):
        # Logic to receive structured research outputs from the Claude Assistant API
        pass

    def update_conversation_context(self, message):
        # Logic to update the conversational context
        self.conversation_context.append(message)

    def clear_conversation_context(self):
        # Logic to clear the conversation context
        self.conversation_context = []