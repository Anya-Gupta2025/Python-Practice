# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# Import random so you can randomise the word
import random

# VALUES
# Create a list of at least 5 different 5-letter words
words = ["salad", "audio", "crust", "shape", "flick", "stray"]

# Create a variable called play and set it to True
game_play = True

# INTRODUCTION
# Tell your user how to play wordle (make sure they know they must input 5 letter words)
print("\nHello! Welcome to Wordle! In this game, you have to try and guess a 5-letter word by putting in your guesses." \
"\nMake sure all of your guesses are 5-letters long!")

# MAIN
# Create a while loop that runs if play is true
while game_play == True:

    # Create word variable and store a random word from your list (using random.choice)
    wordle_word = random.choice(words)

    # Guess counter
    guess = 1

    # While loop to keep the game going until they reach 6 guesses:
    while guess <= 6:

        # USER INPUT
        # Get user's first guess and save it into a variable
        user_guess = input(f"\n{guess}. Guess: ").lower().strip()

        # Create a while loop if the guess is not 5 characters long
        while len(user_guess) != 5:
            # Tell them it's not 5 letters and to try again
            print("Sorry, that isn't a 5-letter word. Try again.")
            user_guess = input(f"\n{guess}. Guess: ").lower().strip()
        # Check if they got it correct and if they did, tell them so and then break the loop
        if user_guess == wordle_word:
            print(f"\nThat's correct! The word was {wordle_word}. You are a mastermind! You got the world in {guess} guesses!")
            break

        # Create a for loop that loops 5 times
        else:
            # Create a list for guess check output
            guess_check = []

            for i in range(5):
                # Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
                if user_guess[i] == wordle_word[i]:
                    guess_check.append(user_guess[i])

                # Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
                elif user_guess[i] in wordle_word:
                    print(f"\nLetter {i+1} ({user_guess[i]} in {user_guess}) is in the word but you have it in the wrong place!")

                # Else tell them that letter is wrong
                else:
                    guess_check.append("_")
            print()
            print("".join(guess_check))

            # Increase guess number by 1
            guess += 1

    # Ask if they want to play again. If they don't, set play to false.
    response = input("Would you like to play this game again? Enter yes/y or no/n: ").strip().lower()

    if response in ["yes", "y"]:
        game_play = True
            
    else:
        game_play = False


# ==========================================================
# EXTENSION -- Done!
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions