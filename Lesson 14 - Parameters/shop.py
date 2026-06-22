"""
PROGRAM: Game Shop
This program runs a game shop for items.
"""

# INSTRUCTIONS
# Code a game shop for players to buy and sell items

# Imports
import textwrap

# Some pre-defined variable:
NAME = "name"
PRICE = 0
budget = 450

# List of fruits and vegies
fruits_and_vegies = [
    {NAME: "Mango", PRICE: 5},
    {NAME: "Apple", PRICE: 2},
    {NAME: "Banana", PRICE: 1},
    {NAME: "Cauliflower", PRICE: 4},
    {NAME: "Broccoli", PRICE: 4},
    {NAME: "Carrot", PRICE: 2.50},
    {NAME: "Bag of Spinach", PRICE: 5},
    {NAME: "Orange", PRICE: 3.50},
    {NAME: "Dragonfruit", PRICE: 4.50}
]

# List of home essentials
home_essentials = [
    {NAME: "Soap", PRICE: 3},
    {NAME: "Bodywash", PRICE: 12},
    {NAME: "Shampoo", PRICE: 15.50},
    {NAME: "Conditioner", PRICE: 16.50},
    {NAME: "Hair Oil", PRICE: 19.75},
    {NAME: "Hair Gel", PRICE: 13.50},
    {NAME: "Mop", PRICE: 6.50},
    {NAME: "Broom", PRICE: 8.99},
    {NAME: "Bath Towel", PRICE: 12.99},
    {NAME: "Face Towel", PRICE: 6.99}
]

# List of Ready-To-Go Food Items
ready_to_go_food = [
    {NAME: "Maggi Instant Noodles", PRICE: 6.50},
    {NAME: "Spicy Ramen", PRICE: 7.50},
    {NAME: "Bar of Chocolate", PRICE: 6.99},
    {NAME: "Sushi (Veg)", PRICE: 16.50},
    {NAME: "Sushi (Non-veg)", PRICE: 17.50},
    {NAME: "Salad", PRICE: 6.50},
    {NAME: "Bread", PRICE: 5.99},
    {NAME: "Cheese Toastie", PRICE: 6.99},
    {NAME: "Tomato & Ham Sandwich", PRICE: 8.50}
]

# List of Snacks & Sweets
snacks_and_sweets = [
    {NAME: "Lollipop", PRICE: 1.50},
    {NAME: "Gummy Bears", PRICE: 2.99},
    {NAME: "Chocolate Bar", PRICE: 3.50},
    {NAME: "Potato Chips", PRICE: 4.50},
    {NAME: "Pretzels", PRICE: 3.99},
    {NAME: "Cookies", PRICE: 4.99},
    {NAME: "Popcorn", PRICE: 3.50},
    {NAME: "Protein Bar", PRICE: 4.99},
    {NAME: "Bag of Candy", PRICE: 3.99}
]

# List of Drinks
drinks = [
    {NAME: "Water Bottle", PRICE: 2.50},
    {NAME: "Soft Drink", PRICE: 3.99},
    {NAME: "Energy Drink", PRICE: 4.99},
    {NAME: "Orange Juice", PRICE: 4.50},
    {NAME: "Apple Juice", PRICE: 4.50},
    {NAME: "Iced Coffee", PRICE: 5.99},
    {NAME: "Sports Drink", PRICE: 4.99},
    {NAME: "Milk", PRICE: 3.99}
]

# List of Categories
shop_categories = [
    fruits_and_vegies,
    home_essentials,
    ready_to_go_food,
    snacks_and_sweets,
    drinks
]

# List of Category names
category_names = [
    "Fruits & Veggies",
    "Home Essentials",
    "Ready-To-Go Food",
    "Snacks & Sweets",
    "Drinks"
]

# List of all items
all_items = fruits_and_vegies + home_essentials + ready_to_go_food + snacks_and_sweets + drinks

# Function for buying
def buy_item():
    print()

# Function for printing all items
def print_all():
    print(f"\n\n======= All Items =======")
    for i in range(4):
        print_category(i)

# Function for printing only one category
def print_category(index):
    category = shop_categories[index]
    print(f"\n\n=== {category_names[index]} ===\n")

    for item in category:
        print(f"{item[NAME]}: ${item[PRICE]}")

    print()

# Function for printing the bill

# Function for checking budget and signaling if spending goes over the budget

# Function to format all the text in this quiz
def text_format(text):
    x = "\n".join(
        textwrap.fill(line, width=90)
        for line in text.splitlines()
    ) + " "
    return x

# Main
def main():
    # Instructions and choice menu
    print(text_format(f"\nWelcome to Anya's Shop! You have a budget of ${budget}. There are several categories you can shop from!"))
    print("1. Fruits & Veggies" \
    "\n2. Home Essentials" \
    "\n3. Ready-To-Go Food" \
    "\n4. Snacks & Sweets" \
    "\n5. Drinks" \
    "\n6. Display all items together\n")

    # Ask user for input
    choice = input(text_format("Please choose your option using the number assigned to it (e.g. 1 for Fruits & Veggies):"))

    # Try to turn the choice into integer, if not, return error
    while True:
        try:
            choice = int(choice)
        except:
            print("\nInvalid response. Try again.")
            choice = input(text_format("Please choose your option using the number assigned to it (e.g. 1 for Fruits & Veggies):"))
            continue

        if 1 <= choice <= 5:
            print_category(choice - 1)
            break
        
        elif choice == 6:
            print_all()
            break

        else:
            choice = input(text_format("Please choose your option using the number assigned to it (e.g. 1 for Fruits & Veggies):"))

main()


#===============================
#===============================
# EXTENSION
# Display extra info for each item (on top of price): attack, defence, item_description, etc.