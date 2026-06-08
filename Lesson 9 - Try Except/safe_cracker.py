# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
# Create a variable for the correct vault combination (e.g., "742").
vault_combination = "465"

# Create a variable to keep track of how many attempts the player has used (start at 0).
attempts = 0

# Function to check the number of digits correct in the answer
def num_checker(a, b):

    vault_combo = list(str(b))
    vault_1st = vault_combo[0]
    vault_2nd = vault_combo[1]
    vault_3rd = vault_combo[2]

    num_list = list(str(a))
    number_1st = num_list[0]
    number_2nd = num_list[1]
    number_3rd = num_list[2]

    score = 0

    if vault_1st == number_1st:
        score += 1
        print("\nYou have the first digit correct!")

    if vault_2nd == number_2nd:
        score += 1
        print("\nYou got the second digit correct!")

    if vault_3rd == number_3rd:
        score += 1
        print("\nYou got the third digit correct!")

    print(f"\nYou got {score} digits in the correct place in total.")

    score = 0

    if number_1st in str(b):
        score += 1

    if number_2nd in str(b):
        score += 1

    if number_3rd in str(b):
        score += 1
    
    print(f"\n{score} of your numbers are in the actual code (regardless of place).\n\n")




# INTRODUCE THE GAME
# Print a cool message explaining they are trying to hack a safe.
print("\nWelcome Hacker.\nYou are about to hack a safe by typing its combination (3 digits long). You have a limited ammount of time (10 attempts), so try your best!")


# Let them know that typing 'exit' will quit the game entirely.
print("\nAt any point, you can quit this mission entirely by simply typing 'exit'.")


# LOOP
# Create an infinite while loop
while True:

# Note: By using 'True', this loop will run forever unless we use 'break'!

    # Ask the user to enter the 3-digit combination (or type 'exit').
    # Save their input into a variable called 'user_input'.
    user_input = input("\nEnter your 3-digit combination here: ")


    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    # Check if 'user_input' is equal to the word 'exit'.
    if user_input.lower().strip() == "exit":
    #       If it is, print "Aborting mission..." and use 'break' to stop the loop!
        print("\nAborting Mission...")
        break

    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    # TODO: Check if their input is a valid number

    if len(user_input.strip()) != 3:
        print("Make sure you enter only 3 digit numbers please.")
        continue

    else:
        try:
            user_input = int(user_input.strip().lower())

        except:
            # If it's not, print "Error: Safe only accepts digits. Try again."
            print("\nError: Safe only accepts digits. Try again.")

            # Then, use 'continue' to skip the rest of the code and restart the loop.
            continue

    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    # If the code gets past Scenario B, it means they entered a valid 3-digit attempt!
    
    # Increase your attempts tracker variable by 1.
    attempts += 1


    # Check if 'user_input' matches the correct vault combination.
    if user_input == int(vault_combination):
        # If it does: Print "Vault unlocked! You found the treasure!" and 'break' out of the loop.
        print("\nVault unlocked! You found the treasure!")
        print(f"\nIt took you {attempts} attempts.\n")
        break

    # If it doesn't: Print a message telling them the combination failed.
    else:
        num_checker(user_input, vault_combination)

    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # Check if their attempts tracker has reached 10.
    # If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

        if attempts == 10:
            print("\nTime out. Mission failed. Alarm triggered! Security is on the way!\n")
            break

        elif attempts >= 7:
            print(f"\nOh no, you are running out of time! Hurry up, you only have {10-attempts} attempts remaining!\n")


# GAME OVER
# ---------------------------------------------------------------------
print("\n--- Game Over ---\n")



# =========================================
# EXTENSION -- DONE
# TODO Add a scenario D to your loop: Running out of time
    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # TODO: Check if their attempts tracker has reached 5.
    #       If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

# =========================================
# EXPERT
# Mastermind Version:
# Add a part that lets you check each digit (you'll need to use split()) and tells the user how many digits are correct in their guess