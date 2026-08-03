print("Welcome to the Quiz Game!")

questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What planet is known as the Red Planet?", "answer": "mars"},
]

def run_quiz():
    score = 0
    for i, q in enumerate(questions, 1):
        answer = input(f"Q{i}: {q['question']}\nYour answer: ")
        if answer.lower() == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {q['answer'].title()}.")
    print(f"\nGame Over! Your final score: {score}/{len(questions)}")
    return score

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
