### Python Quiz ###
# This is a 5-10 Question Quiz which will be modified as I learn more python concepts

import textwrap
import random

## Pre-deiffing some Variables ##

instructions = "Welcome to Magic Quiz Madness. Play and answer the questions if you dare... You might be left with some fascinating, mysterious powers by the end of this! There are 10 questions in this quiz, and they increase with difficulty throughout! So, get ready for this amazing quiz! For questions 1 - 5, you will be awarded 3 points each. Then for the questions 6-10, you will be awards 5 points each. There are 40 points up for grabs!"
INSTRUCTIONS = (textwrap.fill(instructions, width = 90))

permission_prompt = "Would you be comfortable with your name appearing on a leaderboard? Type 'yes' or 'no' to express your permission:"
PERMISSION_PROMPT = (textwrap.fill(permission_prompt, width = 90))

score = 0
questions = 0

#Questions and Answers
QUESTION_ONE = "How many days are in a leap year?"
ANSWER_ONE = 366

QUESTION_TWO = "Which animal is known as the “King of the Jungle”?"
ANSWER_TWO = "lion"

QUESTION_THREE = "What is the capital city of Japan?"
ANSWER_THREE = "Tokyo"

QUESTION_FOUR = "Which organ pumps blood around the human body?"
ANSWER_FOUR = "heart"

QUESTION_FIVE = "What is the fastest land animal?"
ANSWER_FIVE = "cheetah"

QUESTION_SIX = "Which scientist developed the theory of gravity after observing a falling apple?" 
ANSWER_SIX = "Isaac Newton"

QUESTION_SEVEN = "In mathematics, what is the value of π (pi) rounded to 2 decimal places?"
ANSWER_SEVEN = 3.14

QUESTION_EIGHT = "Which country has the largest population in the world as of recent years?"
ANSWER_EIGHT = "India"

QUESTION_NINE = "What is the name of the deepest known part of the world’s oceans?"
ANSWER_NINE = "Mariana Trench"

QUESTION_TEN = "How tall is the tallest human ever born on Earth (your guess will be tested against other people's guesses and you will get an email if you win this quiz!)?"
ANSWER_TEN = {"meters": 2.72, "centimeters": 272}


## Start of the Quiz ##

# Getting name of the player
name = input("Hello! Please enter you name or what you would be preffered to be called: ").title().strip()
print()
print(f"Hello, {name}! \n")

#Printing instructions and asking for permission
print(INSTRUCTIONS, "\n")
permission = input(PERMISSION_PROMPT + " ")
print()

#Asking if the player is ready
input('Are you ready? If so, press "enter" or "return" on your keyboard!')
print()


## QUESTIONS ##

# Question 1:
print("Here comes the first question!", QUESTION_ONE)
answer_1 = int(input("Type your answer here: ").strip())
print()
questions += 1

if answer_1 == ANSWER_ONE:
    score += 3
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_ONE}.")

print()

# Question 2:
print("Here comes the second question!", QUESTION_TWO)
answer_2 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_2 == ANSWER_TWO.lower():
    score += 3
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_TWO}.")

print()

# Question 3:
print("Get ready for the third question!", QUESTION_THREE)
answer_3 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_3 == ANSWER_THREE.lower():
    score += 3
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_THREE}.")

print()

# Question 4:
print("Okay! Here's a tricky one!", QUESTION_FOUR)
answer_4 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_4 == ANSWER_FOUR.lower():
    score += 3
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_FOUR}.")

print()

# Question 5:
fifth_instructions = "Now we are upto the fifth question! Last question before you get 5 points for each question! " + QUESTION_FIVE
fifth_instructions = (textwrap.fill(fifth_instructions, width = 90))
print(fifth_instructions)
answer_5 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_5 == ANSWER_FIVE.lower():
    score += 3
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_FIVE}.")

print()

# Question 6:
sixth_instructions = "Now we are moving into harder questions! Here's the 6th question: " + QUESTION_SIX
print((textwrap.fill(sixth_instructions, width = 90)))
answer_6 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_6 == ANSWER_SIX.lower():
    score += 5
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_SIX}.")

print()

# Question 7:
seventh_instructions = "Here's the next question!" + QUESTION_SEVEN
print((textwrap.fill(seventh_instructions, width = 90)))
answer_7 = float(input("Type your answer here: ").strip())
print()
questions += 1

if answer_7 == ANSWER_SEVEN:
    score += 5
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_SEVEN}.")

print()

# Question 8:
print("Okay! Here's a tricky one!", QUESTION_EIGHT)
answer_8 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_8 == ANSWER_EIGHT.lower():
    score += 5
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_EIGHT}.")

print()

# Question 9:
print("Here's the second-to-last question!", QUESTION_NINE)
answer_9 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_9 == ANSWER_NINE.lower():
    score += 5
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width = 90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width = 90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_NINE}.")

print()

# Question 10:
tenth_instructions = "Good job! We are now on the last question, question 10. Here it is:" + QUESTION_TEN
print((textwrap.fill(tenth_instructions, width = 90)))
answer_10 = input("Type your answer here: ").strip().lower()
print()
questions += 1

if answer_10 == ANSWER_TEN.lower():
    score += 5
    correct_message = f"That's correct, {name}! You have {score} points now!"
    correct_message = (textwrap.fill(correct_message, width =90))
    print(correct_message)
else:
    wrong_message = f"Sorry, that isn't correct, {name}. That's okay though, you have {10-questions} questions remaining! Currently, you have {score} points."
    wrong_message = (textwrap.fill(wrong_message, width =90))
    print(wrong_message, "\n")
    print(f"The correct answer was {ANSWER_TEN}.")

print()