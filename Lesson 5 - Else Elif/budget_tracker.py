### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

import os

# Get the path of the folder where file of this programme is located
folder = os.path.dirname(os.path.abspath(__file__))

# Make full path to save.txt
file_path = os.path.join(folder, "save.txt")

# Some constant variables:
INSTRUCTIONS = "This programme can help you decide whether you can buy an item or not!"

SAVINGS = 20


# Open the save file and read the budget
file = open(file_path, "r")
budget = int(file.read())
file.close()


# Ask user for item name and save in variable
name = input("Hello, what is your name? ").title()
print()

# Print instructions and budget
print(f"Welcome to your Budget tracker, {name}! \n")
print(INSTRUCTIONS, "\n")
print(f"Your current budget is ${budget}. \n")

# Ask if they would like to add some money to thier budget
response = input("Did you earn any money that you would like to add to your budget (y/n)? ")
print()

#If the answer is invalid, prompt to enter the answer again until it's valid
while response != "y" and response != "n":
    print("Hmm, that isn't a valid option repsonse. Make sure to enter only the letter regarding your choice ('y' or 'n').")
    response = input("Answer: ").strip().lower()
print()

# If they bought the item and can afford it
if response == "y":
    
    # Ask for amount they would like to add to the budget
    amount_add = int(input("How much money would you like to add to the budget? ").replace("$", "").strip())
    print()

    # Add amount to budget
    budget += amount_add

    # Open save file in write mode
    file = open(file_path, "w")

    # Save the new budget
    file.write(str(budget))

    # Close file
    file.close()

    print(f"Your new remaining budget is ${budget}. \n")



#Ask user for the type of item
print("What kind of item are you looking to buy?")
print(" A. Food \n B. Clothing \n C. Home Essentials \n D. Something you need (not listed above) \n E. Other\n")

answer = input("Answer: ").strip().lower()

#If the answer is invalid, prompt to enter the answer again until it's valid
while answer != "a" and answer != "b" and answer != "c" and answer != "d" and answer != "e":
    print("Hmm, that isn't a valid option. Make sure to enter only the letter regarding your item.")
    answer = input("Answer: ").strip().lower()

print()


# Ask user for cost and save in variable
cost = input("What is the cost of your item? ").strip()


# Change the cost into an integer
cost = int(cost)


# Calculate the percentage of budget (cost / budget) * 100
percentage_budget = cost/budget * 100


# Tell your user the percentage of your budget
print()
print(f"This is {percentage_budget}% of your budget. \n")


# Check if percentage is 0 and say it's free if it is
if percentage_budget == 0:
    print("This item is free.\n")

# Check if it's over 100 and if it is tell them they don't have enough money
elif percentage_budget > 100:
     print("Hmm, it doesn't look like you have enough money for this item. \n")

# Check if it's over the allowed amount if they want saving and if it is, tell them it cuts into their savings budget aswell
elif percentage_budget > 100 - SAVINGS:
    print("This cuts into your savings account. Rethink this decision! \n")


# If their item option = E (i.e. something which might not be necessary to buy):
if answer == "e":

    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    if percentage_budget < 10:
        print("This is a small treat! Enjoy! \n")

    # Check if it is less than 30 percent and if it is tell them it's a big spend and should sleep on it
    elif percentage_budget < 30:
        print("Oh, well that might be a big spend considering the item... I think you should sleep on it! \n")

    # Otherwise, tell them it is quite expensive and they should find alternatives
    else:
        print("This is an expensive for the item it is! I think you should find an alternative or reconsider this purchase! \n")

# If their item option = D (i.e. something they need):
if answer == "d":

    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    if percentage_budget < 10:
        print("This is a good price! Enjoy! \n")

    # Check if it is less than 50 percent and if it is tell them it's a big spend and should sleep on it
    elif percentage_budget < 50:
        print("Oh, well that might be a big spend... I think you should sleep on it! \n")

    # Otherwise, tell them it is quite expensive and they should find alternatives
    else:
        print("This is an expensive for the item it is! I think you should find an alternative or reconsider this purchase! \n")


# If their item option = C (i.e. home essentials):
if answer == "c":

    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    if percentage_budget < 10:
        print("This is a good price! Enjoy! \n")

    # Check if it is less than 40 percent and if it is tell them it's a big spend and should sleep on it
    elif percentage_budget < 40:
        print("Oh, well that might be a big spend considering the item... I think you should sleep on it! \n")

    # Otherwise, tell them it is quite expensive and they should find alternatives
    else:
        print("This is an expensive for the item it is! I think you should find an alternative or reconsider this purchase! \n")
        

# If their item option = B (i.e. clothing):
if answer == "b":

    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    if percentage_budget < 10:
        print("This is a good price! Enjoy! \n")

    # Check if it is less than 35 percent and if it is tell them it's a big spend and should sleep on it
    elif percentage_budget < 35:
        print("Oh, well that might be a big spend considering that's it's just clothing... I think you should sleep on it! \n")

    # Otherwise, tell them it is quite expensive and they should find alternatives
    else:
        print("This is an expensive for the item it is! I think you should find an alternative or reconsider this purchase! \n")


# If their item option = A (i.e. food):
if answer == "a":

    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    if percentage_budget < 10:
        print("This is a good price! Enjoy! \n")

    # Check if it is less than 20 percent and if it is tell them it's a big spend and should rethink it
    elif percentage_budget < 20:
        print("Oh, well that might be a big spend considering that's it's just food... I think you should rethink this! \n")

    # Otherwise, tell them it is quite expensive and they should find alternatives
    else:
        print("This is an expensive for the item it is! I think you should find an alternative or reconsider this purchase! \n")

# Ask if they bought the item
buy = input("Did you buy this item? (y/n): ").strip().lower()

#If the answer is invalid, prompt to enter the answer again until it's valid
while buy != "y" and buy != "n":
    print("Hmm, that isn't a valid option repsonse. Make sure to enter only the letter regarding your choice ('y' or 'n').")
    buy = input("Answer: ").strip().lower()

print()

# If they bought the item and can afford it
if buy == "y" and cost <= budget:
    
    # Subtract cost from budget
    budget -= cost

    # Open save file in write mode
    file = open(file_path, "w")

    # Save the new budget
    file.write(str(budget))

    # Close file
    file.close()

    print(f"Your new remaining budget is ${budget}.")

# _______________________

# EXTENSION -- DONE
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT -- DONE
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 