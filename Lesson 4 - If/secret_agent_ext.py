import random

### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable
name = input("Hello secret agent. Type you name here: ").title()
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
    colour = input("What is the special colour of this organisation? ").lower()
    print()

    country = input("Which country is our base located at?").title()
    print()

    if country == "New Zealand" and colour == "yellow":
        print("You are a true agent!")


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

        # Generating thier Spy ID:
        print()
        print("Now, we will create your spy ID! Answer the follow questions.")

        number = int(input("What is your favourite single-digit number?"))
        print()

        name_len = len(name)

        # Generating a random fruit
        fruits = ['apple', 'banana', 'orange', 'mango', 'apricot']
        rand_fruits = random.choice(fruits)

        # Generating a random animal
        animals = ['Koala', 'Frog', 'Shark', 'Whale', 'Parrot']
        rand_animals = random.choice(animals)

        # Outputting the Spy ID
        if name_len < 4:
            print(f"Your spy ID is: {rand_fruits}{number}3141")
        
        else:
            print(f"You Spy ID is: {rand_animals}{number}1618")
       
    # If they didn't know the base country and the colour, then we aren't sure about their identity:
    else:
        print("Hmm, we are unsure about who you are. Permission not granted.") 

# Wrong password instantly means no access
else:
    print("Wrong password, no access granted.")

print()

# Output a goodbye
print("Goodbye!")

