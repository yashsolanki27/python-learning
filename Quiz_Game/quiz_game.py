print("Welcome to the Quiz Game!")

score = 0

question = "What is the capital of France?"
answer = input(f"{question}\nYour answer: ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

print(f"Your score: {score}")
