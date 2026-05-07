# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Get input from the user and save it in a variable
# Change the value into an integer and resave in the variable
days = int(input("Number of days: "))

# The number of hours in a day
hours = 24 * days

# The number of minutes in an hour
minutes = 60 * hours

# Values - start by writing constants to hold:
# The number of seconds in a minute
# Calculate the number of seconds using * with the input and your constants. 
# Save it in a new variable.
seconds = 60 * minutes

# Output the answer
#print(f"There are {seconds} seconds in {days}.")

# ---------------------------------

# EXTENSION
# Also output how many total hours and how many total minutes in the days
print(f"There are {hours} hours, or {minutes} minutes, or {seconds} seconds in {days}.")

# Create another calculator that does the opposite (input is seconds, output is days)
secs = int(input("Number of seconds: "))

mins = secs/60
hrs = mins/60
days_number = hrs/24

print(f"There are {days_number} days in {secs} seconds.")

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.

response = "y"

while response == "y":
    convert = input("What would you like to convert (seconds, minutes, hours or days)?").lower().strip()
    converted = input(f"What would you convert {convert} into (seconds, minutes, hours, or days)?").lower().strip()
    value = int(input(f"How many {convert} do you want to convert to {converted} (please only enter a number)?"))

    units = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }

    seconds = value * units[convert]
    answer = seconds / units[converted]

    print(f"{value} {convert} = {answer} {converted}")

    response = input("Would you like to play again? (y = yes, n = no) ")

    