class LLMClient:

    def __init__(self, api_key, model):
        # Shared configuration
        self.api_key = api_key
        self.model = model

        # State data
        self.prompt_count = 0
        self.prompts = []

    def generate(self, prompt):

        # Update object state
        self.prompt_count += 1
        self.prompts.append(prompt)

        print("\n===== GENERATE =====")
        print(f"Using API Key: {self.api_key}")
        print(f"Using Model: {self.model}")
        print(f"Prompt: {prompt}")
        print(f"Total Prompts Sent: {self.prompt_count}")

    def show_history(self):

        print("\n===== PROMPT HISTORY =====")

        if len(self.prompts) == 0:
            print("No prompts found.")
            return

        for index, prompt in enumerate(self.prompts, start=1):
            print(f"{index}. {prompt}")

    def show_stats(self):

        print("\n===== STATS =====")
        print(f"Model: {self.model}")
        print(f"Total Prompts Sent: {self.prompt_count}")

    def reset_count(self):

        self.prompt_count = 0
        print("\nPrompt counter reset.")

    def clear_history(self):

        self.prompts.clear()
        print("\nPrompt history cleared.")

    def change_model(self, new_model):

        self.model = new_model
        print(f"\nModel changed to: {new_model}")


# Create Object
client = LLMClient(api_key="abc123", model="gpt-5")

# Generate Prompts
client.generate("Hello")

client.generate("What is Python?")

client.generate("Explain APIs in simple words")

# Show History
client.show_history()

# Show Stats
client.show_stats()

# Change Model
client.change_model("gpt-5-mini")

# Show Stats Again
client.show_stats()

# Reset Counter
client.reset_count()

# Show Stats Again
client.show_stats()

# Clear History
client.clear_history()


client.show_history()
