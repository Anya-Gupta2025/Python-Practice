# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# Create an empty list called 'shopping_cart' to hold item names.
shopping_cart = []

# Create an empty list called 'price_list' to hold item prices.
price_list = []


# MAIN
# Info for user
info = "\nHello! Welcome to this programme where you can make your own shopping list and with the prices as well!\n"

# Output info for user:
print(info)

# Budget

while True:
    budget = input("\nWhat is your budget for this? ").strip().lower()
    try:
        budget = int(budget)
        break

    except:
        print("\nInvalid response.\n")


# Create an infinite while loop
while True:

    # Current cart/shopping list
    print(f"\n\nYour current cart looks like this: {shopping_cart}")

    # Current prices
    print(f"\nYour current prices looks like this: {price_list}")


    # Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable
    user_action = input("\nWhat would you like to do (make sure to enter the number corresponding with the option you chose)? "
    "\n1. Add item to cart" \
    "\n2. Remove item from cart" \
    "\n3. Clear cart and restart" \
    "\n4. View total and checkout" \
    "\n\nAnswer: ").strip().lower()


    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    # Check if option 1
    if user_action == "1":
        # Ask user for the name of the item
        item_name = input("\nWhat is the name of your item you waqnt to add? ").strip().title()

        # Add it to shopping list
        shopping_cart.append(item_name)

        # Add user for price of item
        item_price = input("\nWhat is the price of this item? ").strip()

        # Change price into a float
        while True:
            try:
                item_price = int(item_price)
                break
        
            except:
                print("\nInvalid answer.\n")
                item_price = input("\nTry again:")

        # Add price to price list
        price_list.append(item_price)

        # Budget check:
        total_cost = sum(price_list)
        
        if total_cost > budget:
            print("\nOh no, you have gone over the budget! Try removing some items!\n")

        else:
            print("\nYou are under your budget!")

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # Else check if option 2
    elif user_action == "2":

        # Ask user for the name of the item they want to remove
        item_name = input("\nWhat is the name of your item you want to remove? ").strip().title()

        # Use .index() to get the index of the item and save in variable
        while True:
            try:
                item_index = shopping_cart.index(item_name)
                break
            
            except:
                print("\nInvalid item.\n")
                item_name = input("\nWhat is the name of your item you want to remove? ").strip().title()


        # Remove the item from cart
        shopping_cart.pop(item_index)

        # Remove the price (using its index) from the price list
        price_list.pop(item_index)

        # Budget check
        total_cost = sum(price_list)

        if total_cost > budget:
            print("\nOh no, you have gone over the budget! Try removing some items!\n")

        else:
            print("\nYou are under your budget!")


    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    # Else check if option 3
    elif user_action == "3":
        # Use the .clear() method on both lists to empty them out.
        shopping_cart.clear()
        price_list.clear()

        # Tell them their cart is empty.
        print("\nYour shopping cart and price list is empty!\n")


    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    # Else check if option 4
    elif user_action ==  "4":

        # Budget check
        total_cost = sum(price_list)

        if total_cost > budget:
            print("\nOh no, you have gone over the budget, try removing some items!\n")
            continue
        
        # Display the results
        print(f"\nYour total comes to: ${total_cost}.")

        # Bill
        print(f"\nHere is your bill:\n")

        i = 0

        while i < len(shopping_cart)-1:
            print(f"{shopping_cart[i]}: ${price_list[i]}")
            i += 1

        
        print("Well done! You are under your budget!")

        # Exit the loop (to exit the program)
        break

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
    # Otherwise
    else:
        # Tell them that option isn't valid
        print("\nInvalid response.\n")

# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.