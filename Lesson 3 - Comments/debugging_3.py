### 3 Question Quiz ###
# This is a quiz where users are asked for answers and their answers are stored.

# Constant variabes which wouldn't change thoughout the programme
INSTRUCTIONS = "This is a quick 3 part quiz. A question will be asked, and then you answer it."


# Asks user for name and outputs a greeting and instructions
name = input("Hi! What's your name? ").title()
print(f"Hello, {name}!")
print(INSTRUCTIONS)

# First Question
print("First question:")
answer_1 = input("How many millimetres are in a centimetre? ")
print("The answer is 10!")

# Second Question
print("Next Question:")
answer_2 = input("What is the capital of New Zealand? ")
print("The answer is Wellington. That was easy, wasn't it?")

# Third Question
print("Final Question!")
answer_3 = input("What is 3 x 6? ")
print("The answer is 18!")