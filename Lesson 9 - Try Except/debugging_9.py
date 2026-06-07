# Variable for the ATM Balance
atm_balance = 500

# Start of a forever loop
while True:

    # Ask user to enter withdrawal ammount
    user_input = input("\nEnter withdrawal amount (or 'exit' to quit): ")

    # Let the user quit, if they entered 'exit'
    if user_input.lower().strip() == "exit":
        break

    # Convert ammount into integer (use try except)
    try:
        ammount = int(user_input)
    
    except:
        print("\nError: Invalid Number. Try Again. \n")
        continue

    # Check if the ammount is less than or equal to 0, and if so, tell them its an invalid ammount
    if ammount <= 0:
        print("\nInvalid amount. Try again.")
        continue

    # Else if, the ammount is greater than the atm balance, tell them they have insuffifient funds
    elif ammount > atm_balance:
        print("\nInsufficient funds!")
        continue

    # IF ATM_BALANCE is equal to 0 THEN print "ATM Empty" and BREAK out of the loop
    if atm_balance == 0:
        print("\nATM empty.")
        break

    # Else, tell them that withdrawal of money was successful and their remaining balance
    else:
        atm_balance = atm_balance - ammount
        print(f"Withdrawal successful. Remaining balance: {atm_balance}")