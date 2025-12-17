class PromptManager:
    def __init__(self):
        self.prompts = {
            "research": "Please provide detailed information on the following topic: {topic}",
            "summary": "Summarize the following content: {content}",
            "creative": "Generate a creative piece based on the following input: {input}"
        }

    def get_prompt(self, prompt_type, **kwargs):
        if prompt_type not in self.prompts:
            raise ValueError(f"Unknown prompt type: {prompt_type}")
        return self.prompts[prompt_type].format(**kwargs)

    def add_prompt(self, prompt_type, prompt_template):
        if prompt_type in self.prompts:
            raise ValueError(f"Prompt type '{prompt_type}' already exists.")
        self.prompts[prompt_type] = prompt_template

    def list_prompts(self):
        return self.prompts.keys()