### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable
name = input("Hello secret agent. Type you name here: ")
print()

# Ask for the password and save it in a variable
password = input(f"Hello {name}, enter your password to proceed: ")
print()

# Check if the password == 'Falcon'
if password == "Falcon":

    # Ouput that access has been granted and welcome user using their name
    print(f"You have been granted access, {name}! Welcome.")
    print()

    print("We will ask you more questions to further check your identity!")
    colour = input("What is the special colour of this organisation? ")

    

    # Ask for the user's age and save it in a variable
    age = input("How old are you? ")
    print()

    # Change the age into an integer
    age = int(age)

    # If the user's age is under 13, tell them they are a spy in training
    if age < 13:
        print("You will be put under training young agent!")

    # If their age is under 18, tell them they are a junior spy
    if age < 18:
        print("You are a junior spy!")

    # If their age is 18 or over, tell them they are a Field Agent
    if age >= 18:
        print("You are a Field Agent!")    

else:
    print("Wrong password, no access granted.")

print()

# Output a goodbye
print("Goodbye!")
# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)



# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...