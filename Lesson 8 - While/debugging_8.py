import random

MAX_ATTEMPTS = 3

attempts = 0

system_status = "OFFLINE"
while attempts < MAX_ATTEMPTS and system_status == "OFFLINE":
    boot_code = input("\nEnter boot code (START): ")

    if boot_code.upper().strip() == "START":
        print("\nSystem booting...\n")
        system_status = "ONLINE"
        print(system_status)

    else:
        print("\nInvalid boot code.\n")
        rand_num = random.randint(1,10)

        if rand_num != 5:
            print("\nSomething went wrong")
        else:
            system_status = "ONLINE"
            print(system_status)

magic_num = random.randint(1, 8)
print(f"\nYour lucky number today is: {magic_num}!")

if magic_num < 5:
    print("\nThe number suggests you should eat something sweet today!\n")

else:
    print("\nThe number suggests you should eat something savoury today!\n")

happiness = input("Do you feel good today? (yes/n or no/n): ").strip().lower()

if happiness in ["yes", "y"]:
    print("\nAwesome! Have a great day!\n")

else:
    print("\nAww, I hope you have a great day! <3\n")


#========================================
# EXTENSION -- Done!
# Add a 'magic eight ball' program for once the system is booted
# Get the user to ask a yes/no question
# Randomise a number and use that number to give them a response