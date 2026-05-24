# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Give instructions
print("\nHello, this programme will check whether you are allowed to ride the roller coaster.")

# Ask for whether they have VIP pass
vip_access = input("\nDo you have a VIP pass? Express your answer as 'yes' or 'no' please. ").strip().lower()

#If the answer is invalid, prompt to enter the answer again until it's valid
while vip_access != "yes" and vip_access != "no":
    print("\nHmm, that isn't a valid option repsonse. Make sure to enter express your response properly ('yes' or 'no').")
    vip_access = input("Answer: ").strip().lower()

# Give access if they have VIP pass
if vip_access == "yes":
    print("\nYou are allowed to ride the roller coaster!")

# If they don't have VIP pass, ask for age and height and save it in a variable
else:
    age = int(input("\nHow old are you? "))
    height = int(input("\nWhat is your height (in cm please)? "))

    # Check if age is greater than 10 and height is greater than 150
    if age > 10 and height > 150:

        # If true, grant permission
        print("\nYou are allowed to ride the roller coaster!")
    
    # If not true, don't grant permission
    else:
        print("\nSorry, you are not allowed to ride the roller coaster!")



# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient