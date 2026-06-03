# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
# Import the 'random' module so you can generate a secret number.
import random

game_play = True

# INTRODUCE THE GAME
# Print a welcome message explaining that the number is between 1 and 100.
print("\nWelcome to this number guessing game! The secret number is an integer between 1 and 100 (inclusive), and you have to try and guess it (e.g. 23)!\n")

# Function to check the number
def number_checker(a):
    
    global secret_number
    # If the number is within 5 of the secret number, output a message
    if a < secret_number and secret_number - a <= 5:
        print("\nThat is very close but you guess is a bit too low! The secret number is 5 or less numbers away!\n")
        
    if a > secret_number and a - secret_number <= 5:
        print("\nThat is very close but you guess is a bit too high! The secret number is 5 or less numbers away!\n")

    # Create an 'if' statement to check if their guess is TOO LOW.
    #   If it is, print "Too low! Try a higher number."
    elif a < secret_number:
        print("\nToo low! Try a higher number!\n")


    # Create an 'elif' statement to check if their guess is TOO HIGH.
    #  If it is, print "Too high! Try a lower number."
    elif a > secret_number:
        print("\nToo high! Try a lower number!\n")


# Start of game loop
while game_play == True:
    # VARIABLES
    # Generate a random number between 1 and 100 and save it to 'secret_number'.
    secret_number = random.randint(1, 100)

    # Create a variable to keep track of the user's current guess.
    #       (Hint: Start it as 0 so it doesn't accidentally match the secret number!)
    guessed_number = 0


    # START THE GAME
    # Start a 'while' loop that keeps running AS LONG AS the 
    #       user's guess is NOT EQUAL to the secret_number.
    while guessed_number != secret_number:
        
        # Ask the user to guess a number. 
        #       (CRITICAL HINT: Remember to convert their input into an integer!)
        guessed_number = int(input("Type your guess here: ").strip())

    # Call the number checker function
    number_checker(guessed_number)

    # GAME OVER / WINNING MESSAGE
    # Print a big victory message telling them they got it right!
    print("\nCongratulations! You got the number!\n")

    response = input("\nWould you like to play again (new country this time!)? Enter yes/y or no/n: ").strip().lower()

    if response in ["yes", "y"]:
        game_play = True
            
    else:
        game_play = False

# ===========================================
# EXTENSION -- Done
# Create a play again option (you'll need to loop the whole code, including creating the random number)
# Add an extra condition that tells them if they are within 5 of the secret number

# ===========================================
# EXPERT -- Done
# Try to structure the program using defined functions