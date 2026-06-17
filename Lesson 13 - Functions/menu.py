"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

import sys
from pathlib import Path

# Main Function and body of code:
def main():

    # Infinite loop until the user exits out
    while True:
        # Create a menu that will run three different programs based on user input.
        print("\nHello, welcome to a menu of my projects! There are 3 projects to choose from and explore!" \
        "\n\n1. Wordle" \
        "\n2. Country Guesser" \
        "\n3. Magic 8 Ball" \
        "\n4. Quit this Porgramme")

        user_choice = input("\nChoice (please enter the number): ")

        if user_choice == "1":
            # Add the parent folder to the search path
            root_dir = str(Path(__file__).resolve().parents[1])
            sys.path.append(root_dir)

            # Import the wordle
            from menu_programmes import wordle_4

            # Call the main function from wordle
            wordle_4.main()

        elif user_choice == "2":
            # Add the parent folder to the search path
            root_dir = str(Path(__file__).resolve().parents[1])
            sys.path.append(root_dir)

            # Import the wordle
            from menu_programmes import country_guesser2

            # Call the main function from chosen project
            country_guesser2.main()

        elif user_choice == "3":
            # Add the parent folder to the search path
            root_dir = str(Path(__file__).resolve().parents[1])
            sys.path.append(root_dir)

            # Import the wordle
            from menu_programmes import magic_8_ball2

            # Call the main function from the chosen project
            magic_8_ball2.main()

        elif user_choice == "4":
            break

        else:
            print("\n Invalid choice. Try again.")
            continue

            
main()

# TODO Each program will need to be its own function OR check out the EXPERT instructions below.



























#===============================
#===============================
# EXTENSION -- Kind of done?!
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()
#===============================
#===============================
# EXPERT -- Done!
# TODO Instead of bringing the code from other programs into this file, use import to import locally.
# You'll need to start by editing your other files so all their code is in functions, with a main() function too.
# NOTE Check this out for info on importing locally: https://github.com/Year-11-Programming/Python-Practice-Projects/wiki/Import-Locals