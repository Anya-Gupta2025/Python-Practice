### Create a packing checklist based on input

# Tell the user what this program is about
print()
print("Hello! This will help you prepare for a trip by giving you a check-list of items!\n")

name = input("Please enter your name here: ").title()
print(f"Hello {name}!\n")

# Ask the user for the current temperature and save it
temp = input("What is the current temperature? ")

# Change the temperature input into an integer
temp = int(temp)

# If the temperature is below 15, tell them to pack a jacket
if temp < 15:
    print("You should put on a jacket or at least pack it!\n")
    items = ["jacket"]

# If the temperature is above 15, tell them to pack sunscreen
else: 
    print("Oh! You might be up for a warm/hot day, make sure to pack some sunscreen!\n")

# Ask the user their destination (beach or mountains)
destination = input("Where are you going? Is it to the beach or the mountains? ").lower()

# If beach, tell them to pack a towel
if destination == "beach":
    print("Amazing! You should pack a towel then!")

# If mountains, tell them to pack hiking boots
if destination == "mountains":
    print("Awesome, you should pack hiking boots then!")

# Ask user for how long they are staying
time = input("How long are you planning on staying there? Is it overnight, or just a day trip? ").lower()

# If overnight, tell them to book a place to stay or pack some tents
if time == "overnight":
    print("Awesome! Make sure to book a place to stay or pack some camping gear!\n")

# If just a day trip, tell user to make sure they have fuel in their trnasport
else:
    print("Ok then, you should make sure you have enough fuel in your transport or just make sure you have a way to get there and back!\n")
# ___________________________

# EXTENSION

# Add some more conditions (eg. one day or overnight? solo or with others?)

# ____________________________

# EXPERT (for those who already know Python)

# Create a packing checklist (start with something similar to the main program) then 
# display all items to pack with a X or O for packed or not. 
# Allow the user to select an item to change its status.