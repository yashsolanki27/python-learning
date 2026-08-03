print("Welcome to the Quiz Game!")

question = "What is the capital of France?"
answer = input(f"{question}\nYour answer: ")

if answer.lower() == "paris":
    print("Correct!")
else:
    print("Wrong! The answer is Paris.")
