class LLMClient:

    def __init__(self, api_key):
        self.api_key = api_key

    def send_prompt(self, prompt):
        self.prompt = prompt
        print("Sending request...")
        print(f"API KEY : {self.api_key}")
        print(f"Prompt : {prompt}")


client = LLMClient("agsasdbas1434")

client.send_prompt("What is Pythonn??")
