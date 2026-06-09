# Room name
VIP_ROOM = "101"

# Names of Guests
guests = ["Alice","Bob"]

while True:
    # Current Guests
    print(f"\nCurrent guests: {guests}")
        
    # Ask user whether they want to add a new guest
    user_response = input("\n\nDo you want to add a new guest? ").strip().lower()

    while user_response not in ["yes", "no", "y", "n"]:
        print("\nHmm, that isn't a valid option response. Make sure to express your response properly ('yes' or 'no' or y/n).")
        user_response = input("Answer: ").strip().lower()

    # Ask user for the name of new user
    if user_response in ["y", "yes"]:
        new_guest = input("\nEnter name of new guest: ").strip().title()

        # Add the new guest 
        guests.append(new_guest)
        print(f"\nCurrent guests: {guests}")

    # Ask user whether they want to find a guest
    user_response = input("\n\nDo you want to search for a new guest? ").strip().lower()

    while user_response not in ["yes", "no", "y", "n"]:
        print("\nHmm, that isn't a valid option response. Make sure to express your response properly ('yes' or 'no' or y/n).")
        user_response = input("Answer: ").strip().lower()

    # Ask user for the name of the guest, if yes
    if user_response in ["y", "yes"]:
        search_name = input("\nEnter their name here: ").strip().title()

        # Try finding the guest
        try:
            # If found, output the name and room no. (index)
            search_name_number = guests.index(search_name)
            print(f"\nGuest found. {search_name} is in Room No.{search_name_number+1}.")

        except:
            # If not found, output that
            print("\nGuest not found.")

    # Ask user whether they want to help a guest checkout
    user_response = input("\n\nDo you want to help a guest checkout? ").strip().lower()

    while user_response not in ["yes", "no", "y", "n"]:
        print("\nHmm, that isn't a valid option response. Make sure to express your response properly ('yes' or 'no' or y/n).")
        user_response = input("Answer: ").strip().lower()

    # Ask user for the name of the guest, if yes
    if user_response in ["y", "yes"]:
        search_name = input("\nEnter their name here: ").strip().title()

        # Try finding the guest
        try:
            # If found, output the name and room no. (index) and remove them and check them out
            search_name_number = guests.index(search_name)
            print(f"\nGuest found. {search_name} is in Room No.{search_name_number+1}. Now checked out.")
            guests.remove(search_name)

        except:
            # If not found, output that
            print("\nGuest not found.")


    # POP the last remaining guest out of the list and store it in a variable called departed_guest
    # PRINT "Departed: " concatenated with departed_guest.

    if len(guests) == 1:
        departed_guest = guests[0]
        guests.pop()
        print(f"Departed: {departed_guest}")
        break

    else:
        # Ask user whether they want to keep going
        user_response = input("\n\nDo you want to keep going? ").lower().strip()

        while user_response not in ["yes", "no", "y", "n"]:
            print("\nHmm, that isn't a valid option response. Make sure to express your response properly ('yes' or 'no' or y/n).")
            user_response = input("Answer: ").strip().lower()

        # Break out of the loop if they don't want to continue
        if user_response in ["n", "no"]:
            break