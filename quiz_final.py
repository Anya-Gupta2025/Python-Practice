### Python Quiz ###
# This is a 10 Question Quiz which will be modified as I learn more python concepts

import textwrap
import os

## To Make a Leaderboard ##

# Get the path of the folder where file of this programme is located
folder = os.path.dirname(os.path.abspath(__file__))

# Make full path to leaderboard.txt
file_path = os.path.join(folder, "leaderboard.txt")

# Open the leaderboard file
file = open("leaderboard.txt", "r")

# Predefining some things:
user = ''
points = 0
leaderboard = {}

# Loading the leaderboard and saving it:
def loading_leaderboard():
    for line in file:
        user, points = line.strip().split(",")
        leaderboard[user] = int(points)

loading_leaderboard()

# Closing the file
file.close()



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


# Questions and Answers
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

# Validating response if it isn't "yes" or "no"
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

    # If user got the answer correct, then award them some points
    if user_answer == question["answer"]:
        
        if question_number < 6:
            score += 3
        
        else:
            score += 5
        
        # Tell user how many points they have
        print(text_format(f"\nThat's correct, {name}! You have {score} points now!\n"))

    # If user got the question wrong, tell them the correct answer
    else:
        print(f"The correct answer was {correct_answer}.\n")

        # If user get the answer answer wrong and there are questions remaining, output a message to encourage them keep going
        if question_number < 10 and question_number != 9:
            print(text_format(f"\nSorry, that isn't correct, {name}. That's okay though, you have {10-question_number} questions remaining! Currently, you have {score} points.\n"))

        # If there is only one question remain, make sure to say "question" not "questions"
        elif question_number == 9:
            print(text_format(f"\nSorry, that isn't correct, {name}. That's okay though, you have {10-question_number} question remaining! Currently, you have {score} points.\n"))

        # If it was the last question, just output some encouragement
        else:
            print(text_format(f"\nHmm, that isn't correct. But that's okay! That was a hard one!\n"))

    question_number += 1
    print()

print(f"\nGood job! The quiz is finished and you have {score} points!\n")

user = name
points = score

## Update the leaderboard ##
# This should happen only if the user gave permission
if permission == "yes":
    # Writing into the file
    file = open("leaderboard.txt", "a")
    file.write(f"{user},{points}\n")

    # Closing the file
    file.close()

    # Opeingin the file in read mode
    file = open("leaderboard.txt", "r")

    # Rereading the file
    loading_leaderboard()

    # Closing the file
    file.close()

    # Rank the users
    sorted_leaderboard = sorted(leaderboard.items(), key = lambda item: item[1], reverse = True)

    # Print Leaderboard
    print("\n\nLEADERBOARD:")
    for user, points in sorted_leaderboard:
        print(user, points)
    
    print()
        