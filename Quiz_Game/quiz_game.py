print("Welcome to the Quiz Game!")

score = 0

# Question 1
question1 = "What is the capital of France?"
answer1 = input(f"Q1: {question1}\nYour answer: ")
if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

# Question 2
question2 = "What is 2 + 2?"
answer2 = input(f"Q2: {question2}\nYour answer: ")
if answer2 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is 4.")

# Question 3
question3 = "What planet is known as the Red Planet?"
answer3 = input(f"Q3: {question3}\nYour answer: ")
if answer3.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Mars.")

print(f"\nGame Over! Your final score: {score}/3")
