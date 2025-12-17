class AssistantService:
    def __init__(self, claude_client, openai_client, prompt_manager):
        self.claude_client = claude_client
        self.openai_client = openai_client
        self.prompt_manager = prompt_manager

    def process_research_request(self, topic):
        prompt = self.prompt_manager.create_research_prompt(topic)
        research_output = self.claude_client.send_research_request(prompt)
        return research_output

    def generate_summary(self, research_output):
        prompt = self.prompt_manager.create_summary_prompt(research_output)
        summary = self.openai_client.generate_summary(prompt)
        return summary

    def handle_user_input(self, user_input):
        if user_input.startswith("research:"):
            topic = user_input.split(":", 1)[1].strip()
            return self.process_research_request(topic)
        elif user_input.startswith("summarize:"):
            research_output = user_input.split(":", 1)[1].strip()
            return self.generate_summary(research_output)
        else:
            return "Error: Unrecognized command. Please use 'research:<topic>' or 'summarize:<output>'."