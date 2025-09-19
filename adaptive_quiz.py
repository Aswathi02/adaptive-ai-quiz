import random

questions = {
    "easy": [
        ("2 + 2 = ?", "4"),
        ("What is 5 - 3?", "2")
    ],
    "medium": [
        ("What is 12 / 3?", "4"),
        ("Square root of 49?", "7")
    ],
    "hard": [
        ("What is 15 * 12?", "180"),
        ("Solve: (25/5) + (12*2)", "29")
    ]
}

score_history = []

def ask_question(level):
    q, ans = random.choice(questions[level])
    user = input(q + " ")
    if user == ans:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Correct answer is {ans}")
        return 0

def adaptive_quiz():
    level = "easy"
    for i in range(5):
        score = ask_question(level)
        score_history.append(score)
        if score == 1 and level == "easy":
            level = "medium"
        elif score == 1 and level == "medium":
            level = "hard"
        elif score == 0 and level == "hard":
            level = "medium"
        elif score == 0 and level == "medium":
            level = "easy"

    print(f"\nFinal Score: {sum(score_history)}/5")

    with open("results.txt", "w") as f:
        f.write("Adaptive Quiz Results\n")
        f.write("----------------------\n")
        for i, s in enumerate(score_history, 1):
            f.write(f"Q{i}: {'Correct' if s==1 else 'Wrong'}\n")
        f.write(f"\nFinal Score: {sum(score_history)}/5\n")

adaptive_quiz()
