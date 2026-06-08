# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
# Create a variable for valid input and set it to false
valid_input = False

# GET INPUT
# Start a loop while the input is invalid
while valid_input == False:

    # Ask the user for their age and save it
    age = input("\nHello! How old are you? ")

    #TRY
    # Create a try statement
    try:
       
        # Change the input into an integer and resave it
        age = int(age)

        # Set the valid input variable to true
        valid_input = True

    # FAIL TO CONVERT TO INTEGER
    # Add an except statement
    except:
    
    # Tell the user their input was invalid
        print("\nHmm, that isn't a valid number.")

# Unindented = Loop has finished so the input must be valid now

# CHECK AGE
# Check if they are older than 18 and tell them they have access if they are
if age > 18:
    print("\nYou are over 18! You have access.")

    print("\n\nNow you can create your avatar!")

    character_class = input("\nWhat would be your character's class? (warrior or rogue) ").strip().lower()

    while character_class not in ["warrior", "rogue"]:
        character_class = input("\nInvalid answer. Try again: ")

    eye_colour = input("\nWhat would be your character's eye colour be? (brown, blue, green, hazel) ").strip().lower()

    while eye_colour not in ["brown", "blue", "green", "hazel"]:
        eye_colour = input("\nInvalid answer. Try again: ")
    
    
    hair_colour = input("\nWhat would be your character's hair colour be? (brown, black, blonde, white) ").strip().lower()

    while hair_colour not in ["brown", "black", "blonde", "white"]:
        hair_colour = input("\nInvalid answer. Try again: ")
    
    print(f"\nYour character is a {character_class} with {eye_colour} eyes and {hair_colour} hair!")
    


# Check if they are older than 13 and tell them they have partial access if they are.
elif age > 13:
    print("\nYou are over 13 but not over 18, so you ave been granted partial access.")

    print("\n\nNow you can create your avatar!")

    character_class = input("\nWhat would be your character's class? (warrior or rogue) ").strip().lower()

    while character_class not in ["warrior", "rogue"]:
        character_class = input("\nInvalid answer. Try again: ")
    
    print("\n\nNow you can create your avatar!")

    animal = input("\nWhat would be your character's animal be? (fox, stag, lion, tiger) ").strip().lower()

    while animal not in ["lion", "tiger", "stag", "fox"]:
        animal = input("\nInvalid answer. Try again: ")

    print(f"\nYour character is a {character_class} with {animal} as their pet!")

# Otherwise tell them access has been denied
else:
    print("\nSorry you aren't old enough. Access denied.")


# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)