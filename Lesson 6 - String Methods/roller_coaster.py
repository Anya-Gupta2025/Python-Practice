# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Rides Dictionary and their requirements
rides = {
    "a": {
        "name": "Rollercoaster",
        "min_age": 10,
        "min_height": 150,
        "heart_condition_allow": "no"
    },

    "b": {
        "name": "Space Invaders",
        "min_age": 8,
        "min_height": 120,
        "heart_condition_allow": "no"
    },

    "c": {
        "name": "Fearfall",
        "min_age": 14,
        "min_height": 150,
        "heart_condition_allow": "no"
    }
}

# Give instructions
print("\nHello, this programme will check whether you are allowed to ride the ride you are unsure about.")

# Ask user for what ride they are unsure about
response = input("What ride are you unsure about? \nA. Rollercoaster \nB. Space Invaders \nC. Fearfall \n \nAnswer: ").strip().lower()

#If the answer is invalid, prompt to enter the answer again until it's valid
while response not in rides:
    print("\nHmm, that isn't a valid option repsonse. Make sure to enter just the letter regarding your ride: 'a', 'b', or 'c'!")
    response = input("Answer: ").strip().lower()

# Get selected ride information
ride = rides[response]

# Ask for whether they have VIP pass
vip_access = input("\nDo you have a VIP pass? Express your answer as 'yes' or 'no' please. ").strip().lower()

#If the answer is invalid, prompt to enter the answer again until it's valid
while vip_access not in ["yes", "no"]:
    print("\nHmm, that isn't a valid option repsonse. Make sure to express your response properly ('yes' or 'no').")
    vip_access = input("Answer: ").strip().lower()

# Give access if they have VIP pass
if vip_access == "yes":
    print(f"\nYou are allowed to ride the {ride['name']}!")

# If they don't have VIP pass, ask for heart condition, age, and height and save it in a variable
else:
    age = int(input("\nHow old are you? "))
    height = int(input("\nWhat is your height (in cm please)? "))
    heart_condition = input("\nDo you have a heart conidtion? ('yes' or 'no'): ").lower().strip()

    # Check whether they give a valid response for the heart condition part
    while heart_condition not in ["yes", "no"]:
        print("\nHmm, that isn't a valid option repsonse. Make sure to express your response properly ('yes' or 'no').")
        heart_condition = input("Answer: ").strip().lower()

    # Check all requirements now
    if (
        age > ride["min_age"]
        and height > ride["min_height"]
        and (
            ride["heart_condition_allow"]
            or heart_condition == "no"
        )
    ):
        print(f"\nYou are allowed to ride the {ride['name']}!")
    
    # If not true, don't grant permission
    else:
        print(f"\nSorry, you are NOT allowed to ride the {ride['name']}.")


# ------------------------------
# EXTENSION -- DONE
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT -- DONE
# Follow the same task (with extension), but use dictionaries to make the code more efficient