# Write a program to Create a simple quiz application.

def quiz_app():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
            "answer": "C"
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo", "D. Tesla"],
            "answer": "B"
        }
    ]

    score = 0
    print("Welcome to the Quiz Application!\n")

    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct\n")
            score += 1
        else:
            print(f"Wrong. Correct answer is {q['answer']}.\n")

    print(f"Your final score is {score}/{len(questions)}")

# Run the quiz
quiz_app()
