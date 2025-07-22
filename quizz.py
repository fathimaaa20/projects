questions = [
    {
        "Question": "What is the capital of India?",
        "Options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Pune"],
        "Answer": "A"
    },
    {
        "Question": "Which is the largest continent in the world?",
        "Options": ["A. Africa", "B. Australia", "C. Europe", "D. Asia"],
        "Answer": "D"
    },
    {
        "Question": "What is the smallest prime number?",
        "Options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "Answer": "C"
    },
    {
        "Question": "Which is the largest planet in our solar system?",
        "Options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "Answer": "C"
    }
]

def quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["Question"])  # Adds spacing before question
        for option in question["Options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == question["Answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {question['Answer']}\n")

    print(f"\nYour final score is {score}/{len(questions)}")

print("Welcome to the quiz game!")
quiz(questions)
print("Thanks for playing!")
