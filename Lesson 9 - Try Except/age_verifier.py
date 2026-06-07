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

    # TODO Ask the user for their age and save it
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
    
    # TODO Tell the user their input was invalid
        print("\nHmm, that isn't a valid number.")

# Unindented = Loop has finished so the input must be valid now

# CHECK AGE
# Check if they are older than 18 and tell them they have access if they are
if age > 18:
    print("\nYou are over 18! You have access.")

# TODO Check if they are older than 13 and tell them they have partial access if they are.
elif age > 13:
    print("\nYou are over 13 but not over 18, so you ave been granted partial access.")

# TODO Otherwise tell them access has been denied
else:
    print("\nSorry you aren't old enough. Access denied.")


# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)