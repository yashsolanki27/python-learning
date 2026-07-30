class LLMClient:

    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        self.prompt_count = 0

    def generate(self, prompt):

        # Increase count every time generate() is called
        self.prompt_count += 1

        print(f"\nUsing API Key: {self.api_key}")
        print(f"Using Model: {self.model}")
        print(f"Prompt: {prompt}")
        print(f"Total Prompts Sent: {self.prompt_count}")


client = LLMClient("abc123", "gpt-5")

client.generate("Hello")

client.generate("What is Python?")

client.generate("Explain APIs")
