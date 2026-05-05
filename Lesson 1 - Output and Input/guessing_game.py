### Create a 3-part guessing game ###

print()
print("Hello! Welcome to Anya's Guessing Game! You will be given 3 hints in total in this, and after each hint, you can guess the word! Remember the answer is a singular word!\n")

word = "name"

# Give your user the first hint and wait for input

print("Your first clue is: This is unique for everyone, but some people may have the same one occasionally.")
guess = input("Guess: ").lower()

if guess==word:
    point = 3
    print("That's correct! You win! You got", point, "points!")

# Give your user the second hint and wait for input
else:
    print("That's not correct! Don't worry, here's your second clue: You can find this on your ID card.")
    guess = input("Guess: ").lower()

    if guess==word:
        point = 2
        print("That's correct! You win! You got ", point, " points!")

    # Give your user the final hint and wait for input
    else:
        print("That's not correct! Don't worry, here's your third and final clue: You use it less often than others use it.")
        guess = input("Guess: ").lower()

        # Tell your user the answer
        if guess==word:
            point = 1
            print("That's correct! You win! You got ", point, " points!")

        else:
            print("Sorry, that isn't correct! The word was: Name")

    # ------------------------------

    # EXTENSION
    # Create another guessing game


    # ------------------------------

    # EXPERT (for those who already know some Python)
    # Your 3-part guessing game should have:
    # + An introduction
    # + A conclusion
    # + It should check if the user is correct and stop giving hints if they are
    # + It should give points based on how quickly the user got it correct