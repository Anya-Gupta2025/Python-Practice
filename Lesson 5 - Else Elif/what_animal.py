### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 

# Give instructions to the user
print("Hello! Wlecome to this quiz! Answer the next few questions in order to find out what animal you are!")


## 3 questions and 4 animals ##

# Ask your user a question about themselves, giving them 2 options

response_1 = input("Are you an early riser, or not? (Y = Yes, N = No): ").lower

# Check if they picked the first option
if response_1 == "y":
     # Ask the next question
    response_2 = input("Do you like being alone in your free time more than being with people? (Y = Yes, N = No): ").lower()

    # Check if they picked the first option
    if response_2 == "y":
        # Tell them they're animal 1
        print("You are a Koala!")

    # Otherwise
    else:
        # Tell them they're animal 2
        print("You are a Wolf!")

# Otherwise
else:
    # Ask the next question
    response_3 = input("Do you like listening more than talking? (Y = Yes, N = No): ").lower()

    # Check if they picked the first option
    if response_3 == "y":
        # Tell them they're animal 3
        print("You are a Lizard!")

    # Otherwise
    else:
        # Tell them they're animal 4 
        print("You are a Chicken!")


# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.