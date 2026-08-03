print("Welcome to the Quiz Game!")

easy_questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What color is the sky?", "answer": "blue"},
]

medium_questions = [
    {"question": "What planet is known as the Red Planet?", "answer": "mars"},
    {"question": "What is the largest ocean?", "answer": "pacific"},
    {"question": "How many continents are there?", "answer": "7"},
]

hard_questions = [
    {"question": "What is the speed of light in km/s?", "answer": "300000"},
    {"question": "What year was Python created?", "answer": "1991"},
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
]

def get_questions(difficulty):
    if difficulty == "easy":
        return easy_questions
    elif difficulty == "medium":
        return medium_questions
    else:
        return hard_questions

def run_quiz():
    print("\nSelect difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        difficulty = "easy"
    elif choice == "2":
        difficulty = "medium"
    else:
        difficulty = "hard"

    questions = get_questions(difficulty)
    score = 0

    print(f"\n--- {difficulty.upper()} MODE ---\n")

    for i, q in enumerate(questions, 1):
        answer = input(f"Q{i}: {q['question']}\nYour answer: ")
        if answer.lower() == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The answer is {q['answer'].title()}.\n")

    print(f"Game Over! Your final score: {score}/{len(questions)}")
    return score

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
