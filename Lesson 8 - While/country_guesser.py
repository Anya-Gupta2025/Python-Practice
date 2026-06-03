# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# Importing the random library
import random


# Instructions
print("\nWelcome to this country guessing game! You start will 20 points, and lose 1 point for every guess you get incorrect. If you reach 0 points, you lose the game. Start by entering any country!\n")
game_play = True

# VALUES
# Create a variable to store the correct country (e.g., "Italy").
countries = ["Mexico", "Spain", "India", "China", "South Korea", "Bolivia", "South Africa", "Cuba", "New Zealand", "North Korea", "Hungary"]

while game_play == True:

    # Game Start settings
    correct_country = random.choice(countries)
    score = 20
    
    # print(correct_country)


    # Create a variable to keep track of the user's current guess. 
    #       (Hint: Start it as an empty string "" so the loop runs at least once!)
    guessed_country = ""


    # LOOP
    # Start a 'while' loop. 
    # The loop should keep running AS LONG AS the user's guess 
    # is NOT EQUAL to the correct country.

    while guessed_country != correct_country and score > 0:

        # Ask the user for their guess and save it to your guess variable.
        #       (Remember: This changes the loop condition so it doesn't run forever!)
        guessed_country = input("\nType your guess here: ").strip().title()
        
        # (Optional) Add an 'if' statement inside the loop.
        #       If they guessed wrong, print an encouraging message or an extra hint.
        #       If they guessed right, the loop will automatically exit on the next check!
        if guessed_country == correct_country:
            print("\nGood job! You got it! :)\n")
            # GAME OVER / WINNING MESSAGE
            # Print a congratulatory message celebrating their win!
            print("\nYay! You win! Congratulations!\n")
        
        # Otherwise, tell them they didn't get the answer
        else:
            print("\n Hmm, that isn't the correct answer. \n")
        
        # Decrease score by 1 and tell them they lost if they reach 0 points
        score -= 1
        if score == 0:
            print("\nOh no, you have 0 points remaining. Sorry, you lose this game!\n")

    response = input("Would you like to play again (new country this time!)? Enter yes/y or no/n: ").strip().lower()

    if response in ["yes", "y"]:
        game_play = True
        
    else:
        game_play = False




# ================================================================
# EXTENSION -- Done
# Add an introduction
# Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT -- Done
# Make the game unique (use a list of countries and randomly select one)
# Add a play again option