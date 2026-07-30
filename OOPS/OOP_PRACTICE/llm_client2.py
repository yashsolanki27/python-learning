class LLMCastro:

    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt):

        print(f"Using API Key: {self.api_key}")
        print(f"Using Model: {self.model}")

        print(f"Prompt: {prompt}")


client = LLMCastro("grwenrue7", "Fable-5")

client.generate(
    "Can i explore today?? I really want to full of TL...help me guide me..."
)
