# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# Import the 'random' module so we can pick a random index later.
import random


print("\nBeware! This game may great you with some snarky response so be prepared for that! :)\n")

# RESPONSES
# Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."
responses = ["Yes, definitely!", "Ask again later.", "Outlook not so good.", "That sounds like a great idea!", "I'm not sure about that one, the fate isn't clear.", "Nope! Definitely no!"]

# Split your responses into 2 lists. A common responses list and a rare responses list
responses_rare = ["Today is your lucky day! If you really hope it does, it will happen!", "Today seems to be a bit rough for you, just trust your heart."]

# Create a dictionary (or multiple lists) for different mood answers
mood_response = {
    "do i": "The answer may surprise you and disappoint you at the same time.",
    "will i": "I love how confidently you asked that.",
    "does": "Yes, but remember: You don't have to have everything figured out to move forward!",
    "think": "You are overthinking it, my dear. Instead spend some of that time thinking about your future."
}


# MAIN LOOP
# Create an infinite loop
while True:
    
    # Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    user_input = input("\nType your yes/no question here that you would like to know the answer to! Or type 'quit' to leave this game: ").strip().lower()
    
    # Check if the user wants to exit and break from the loop if they do.
    if user_input == "quit":
        break
        
    # RANDOM REPSONSE

    # Step A: Calculate the last valid index of your list. -> 5
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    random_index = random.randint(0,5)

    # Use random.random() or randint() to get a percentage
    rare_percentage = random.randint(0,100)
    
    
    # Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.
    chosen_fortune = responses[random_index]
    chosen_rare_fortune = responses_rare[random.randint(0,1)]

    # Print the result
    # Check if the number is lower than 0.8 and use the common list to give a response if it is
    if rare_percentage/100 < 0.4:
        print(f"\n{chosen_fortune}\n")
    
    # Otherwise use the rare list
    elif rare_percentage/100 < 0.8:
        print(f"\n{chosen_rare_fortune}\n")

    # Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.
    else:
        print()

        if "do i" in user_input:
            print(mood_response["do i"])

        elif "will i" in user_input:
            print(mood_response["will i"]) 

        elif "does" in user_input:
            print(mood_response["does"])

        else:
            print(mood_response["think"])

# Say goodbye to let them know the program has ended.
print("\nThank you for playing this game! See you next time!\n")


# ==================================================
# EXTENSION -- Done!
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list

# ===================================================
# EXPERT -- Done!
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.