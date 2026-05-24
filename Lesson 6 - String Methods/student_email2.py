# Create a student email creator that uses first and lat name plus id
import random

# Get input (first, last, id) and save in variables
# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)
first_name = input("\nHello! Enter your first name here: ").lower().strip()
last_name = input("\nEnter your last name here: ").lower().strip()
print()


# Make ID
id = str(len(first_name)) + str(len(last_name))
id = int(id)^2 + random.randint(10000000, 99999700)

# Find the first letter of first name
f_first_name = first_name[0]


# Output the final email address
print(f"\nYour Western Spring College email is: {last_name}{f_first_name}{id}@wsc.school.nz")


# Dividing the ID by 10 and saving it as a new number
id_int = int(id/10)

# Turning names into uppercase
upper_first_name = first_name.upper()
upper_last_name = last_name.upper()

# Output the password
print(f"\nYou password is: {upper_first_name}{upper_last_name}{id_int}\n")




# --------------------------------

# EXTENSION -- DONE
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10

# --------------------------------

# EXPERT -- DONE
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf@wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user