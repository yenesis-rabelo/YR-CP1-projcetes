#Yenesis Rabelo Quiz Creation ProficienyTest 

def quiz_game():
    

    # initialize score
    score = 0
    
    # question 1 (the harder question)
    question1 = {
        "question": "What is the largest planet in our solar system?",
        "options": {
            "A": "Earth",
            "B": "Jupiter",
            "C": "Saturn",
            "D": "Mars"
        },
        "correct_answer": "B"
    }

    # question 2 (the easier question)
    easier_question = {
        "question": "Which planet is closest to the Sun?",
        "options": {
            "A": "Mercury",
            "B": "Venus",
            "C": "Earth",
            "D": "Mars"
        },
        "correct_answer": "A"
    }

    # function that asks a question and checks the answer
    def ask_question(question):
        print(question["question"])
        for option, answer in question["options"].items():
            print(f"{option}: {answer}")
        user_answer = input("Your answer (A, B, C, D): ").upper()
        if user_answer == question["correct_answer"]:
            return True
        else:
            return False
    
    # asking the first question
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect again. Let's keep going.\n")

    # asking the second question 
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect again. Let's keep going.\n")

    # asking the third question
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect again. Let's keep going.\n")

    # asking the fourth question
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect again. Let's keep going.\n")

    # asking the fifth question 
    if ask_question(question1):
        score += 1
        print("Correct!\n")
    else:
        print("Incorrect. Let's try an easier one.\n")
        if ask_question(easier_question):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect again. Let's keep going.\n")

    # the final score
    print(f"Your final score is: {score}/5")
    if score == 5:
        print("Excellent! You know a lot about the Solar System!")
    elif score >= 3:
        print("Good job! You have a decent understanding of the Solar System.")
    else:
        print("Keep studying! You can do better next time!")

# start the quiz game
quiz_game()
