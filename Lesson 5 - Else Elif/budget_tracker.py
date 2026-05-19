### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

# Create a constant to hold your budget
BUDGET = 60
# Create a constant to hold your savings (percentage) goal
SAVINGS = 20

# Ask user for item name and save in variable
name = input("Hello, what is your name? ").title()
print()

print(f"Welcome to your Budget tracker, {name}! \n")

# Ask user for cost and save in variable
cost = input("What is the cost of your item? ").strip()

# Change the cost into an integer
cost = int(cost)

# Calculate the percentage of budget (cost / budget) * 100
percentage_budget = cost/BUDGET * 100

# Tell your user the percentage of your budget
print()
print(f"This is {percentage_budget}% of your budget. \n")

# Check if percentage is 0 and say it's free if it is
if percentage_budget == 0:
    print("This item is free.\n")

# Check if the percentage is less then 10 and say it's a small treat so enjoy
elif percentage_budget < 10:
    print("This is a small treat! Enjoy! \n")

# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
elif percentage_budget < 50 and percentage_budget < 100 - SAVINGS:
    print("Oh, well that's a major spend... I think you should sleep on it! \n")

# Check if it's over 100 and if it is tell them they don't have enough money
elif percentage_budget > 100:
    print("Hmm, it doesn't look like you have enough money for this item. \n")

# Otherwise, tell them it cuts into their savings budget aswell
else:
    print("This cuts into your savings account. Rethink this decision! \n")

# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 