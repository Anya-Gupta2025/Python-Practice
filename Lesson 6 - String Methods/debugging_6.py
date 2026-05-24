### Programme to output flight details and waititng status ###

# Ask user whether they are a gold member or not
member_status = input("\nDo you have a gold member status? ('yes'/'no'): ")

#If the answer is invalid, prompt to enter the answer again until it's valid
while member_status != "yes" and member_status != "no":
    print("\nHmm, that isn't a valid option repsonse. Make sure to enter express your response properly ('yes' or 'no').")
    member_status = input("Answer: ").strip().lower()

# Ask user for seat row and save it as an integer
passenger_row = int(input("\nEnter your seat row: "))

# Ask user for whether they have valid tickets
has_ticket = input("\nDo you have a valid ticket? ('yes'/'no'): ")
print()

#If the answer is invalid, prompt to enter the answer again until it's valid
while has_ticket != "yes" and has_ticket != "no":
    print("\nHmm, that isn't a valid option repsonse. Make sure to enter express your response properly ('yes' or 'no').")
    has_ticket = input("Answer: ").strip().lower()

# If user doesn't have valid ticket, tell them they don't have access
if has_ticket.lower() == "no":
    print("Access Denied. Please ensure you have a valid ticket before boarding.")

# If user has a gold pass and has a set in business class (passenger row is less than 8), grant access and tell them to board now
elif passenger_row <= 8 and member_status == "yes":
    print("Welcome to priority boarding! Please make your way on board now.")

# If user has a gold pass or has a seat in business class, tell them to wait for the Gold Business Flyers before boarding
elif passenger_row <= 8 or member_status == "yes":
    print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")

# If user have a passenger row higher than 8, tell them to wait for general boarding
elif passenger_row > 8:
    print("Please wait for general boarding.")

# Ask user for destination
destination = input("\nEnter your destination code: ").upper().strip()
print()

# If destination is Auckland/Wellington, tell user their flight is delayed by 5 minutes
if destination == "AKL" or destination == "WLG":
    print("Flight is delayed 5 minutes.")

# If destination is not CHC, tell them their flight is on time
elif not destination == "CHC":
    print("Flight is on time.")

# Otherwise, tell user their flight has been cancelled
else:
    print("Flight has been cancelled.")
