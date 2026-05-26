### Python Quiz ###
# This is a 10 Question Quiz which will be modified as I learn more python concepts

import textwrap


# Function to format all the text in this quiz
def text_format(text):
    return "\n".join(
        textwrap.fill(line, width=90)
        for line in text.splitlines()
    )



## Pre-defining some Variables ##
instructions = "Welcome to Magic Quiz Madness. Play and answer the questions if you dare... You might be left with some fascinating, mysterious powers by the end of this! There are 10 questions in this quiz, and they increase with difficulty throughout! So, get ready for this amazing quiz! For questions 1 - 5, you will be awarded 3 points each. Then for the questions 6-10, you will be awards 5 points each. There are 40 points up for grabs!\n"
permission_prompt = "Would you be comfortable with your name appearing on a leaderboard? Type 'yes' or 'no' to express your permission: "
score = 0
questions = 0


#Questions and Answers
questions_answers = {
    "1": {
        "question": "\nHow many days are in a leap year?",
        "answers": "\nA. 30 \nB. 31 \nC. 366 \n",
        "answer": "c"
    },

    "2": {
        "question": "\nWhich animal is known as the “King of the Jungle”?\n",
        "answers": "\nA. Tiger \nB. Lion \nC. Wolf \n",
        "answer": "b"
    },

    "3": {
        "question": "\nWhat is the capital city of Japan?\n",
        "answers": "\nA. Tokyo \nB. Hiroshima \nC. Nagasaki \n",
        "answer": "a"
    },

    "4": {
        "question": "\nWhich organ pumps blood around the human body?\n",
        "answers": "\nA. Heart \nB. Lungs \nC. Liver \n",
        "answer": "a"
    },

    "5": {
        "question": "\nWhat is the fastest land animal?\n",
        "answers": "\nA. Tiger \nB. Cheetah \nC. Jaguar \n",
        "answer": "b"
    },

    "6": {
        "question": "\nWhich scientist developed the theory of gravity after observing a falling apple?\n",
        "answers": "\nA. Aristotle N \nB. Albert Einstein \nC. Isaac Newton \n",
        "answer": "c"
    },

    "7": {
        "question": "\nIn mathematics, what is the value of π (pi) rounded to 2 decimal places?\n",
        "answers": "\nA. 3.23 \nB. 3.14 \nC. 1.51 \n",
        "answer": "b"
    },

    "8": {
        "question": "\nWhich country has the largest population in the world as of recent years?\n",
        "answers": "\nA. India \nB. China \nC. USA \n",
        "answer": "a"
    },

    "9": {
        "question": "\nWhat is the name of the deepest known part of the world's oceans?\n",
        "answers": "\nA. Java Trench \nB. Puerto Rico Trench \nC. Mariana Trench \n",
        "answer": "c"
    },

    "10": {
        "question": "\nHow tall is the tallest human ever born on Earth?\n",
        "answers": "\nA. 272 cm \nB. 259 cm \nC. 226 cm \n",
        "answer": "a"
    } 
}


## Start of the Quiz ##

# Getting name of the player
name = input("\nHello! Please enter you name or what you would be preferred to be called: ").title().strip()
print(f"Hello, {name}! \n\n")

#Printing instructions and asking for permission
print(text_format(instructions))
print()
permission = input(text_format(permission_prompt) + " ").lower().strip()
print()

while permission not in ["yes", "no"]:
        print("\nHmm, that isn't a valid option response. Make sure to express your response properly ('yes' or 'no').")
        permission = input("Answer: ").strip().lower()

#Asking if the player is ready
input('Are you ready? If so, press "enter" or "return" on your keyboard!')
print()


## QUESTIONS ##

question_number = 1
while question_number < 11:
    print(f"\nHere is Question {question_number}!")
    question = str(question_number)
    question = questions_answers[question]
    print(text_format(question["question"]))
    print(text_format(question["answers"]))
    user_answer = input("\nAnswer: ").strip().lower()
    correct_answer = question["answer"].upper()


    while user_answer not in ["a", "b", "c"]:
        print("\nInvalid answer. Make sure you only type the letter corresponding to your answer. ('a' or 'b' or 'c')")
        user_answer = input("Answer: ")

    if user_answer == question["answer"]:
        
        if question_number < 6:
            score += 3
        
        else:
            score += 5
        
        print(text_format(f"\nThat's correct, {name}! You have {score} points now!\n"))

    elif question_number < 10:
        print(text_format(f"\nSorry, that isn't correct, {name}. That's okay though, you have {10-question_number} questions remaining! Currently, you have {score} points.\n"))
        print(f"The correct answer was {correct_answer}.\n")

    else:
        print(text_format(f"Hmm, that isn't correct. But that's okay! That was a hard one! The correct answer was {correct_answer}.\n"))

    question_number += 1

print(f"Good job! The quiz is finished and you have {score} points!")