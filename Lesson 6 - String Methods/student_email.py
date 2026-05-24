# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables
# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)
first_name = input("\nHello! Enter your first name here: ").lower().strip()
last_name = input("\nEnter your last name here: ").lower().strip()
print()
id = input("\nEnter your ID here: ")


# Output the final email address
print(f"\nYour email is: {first_name}{last_name}{id}@gmail.com")

# Turning the ID into integer
id_int = int(id)

# Dividing the ID by 10 and saving it as a new number
id_int = int(id_int/10)

# Turning names into uppercase
upper_first_name = first_name.upper()
upper_last_name = last_name.upper()

# Output the password
print(f"\nYour password is: {upper_first_name}{upper_last_name}{id_int}")




# --------------------------------

# EXTENSION -- DONE
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user