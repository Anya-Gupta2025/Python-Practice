### This is a Step Tracker ###


#Intro:
print("---- Daily Step Tracker ----")

# Ask user for goal of steps, if not , set it to 5000:
daily_goal = 5000

response = input("Do you have a goal for you steps today? Type y/n to signal response: ").lower()

if response == "y":
    daily_goal = input("Awesome! What is your goal? ")
    daily_goal = int(daily_goal)
else:
    print("That's okay! For now, your goal is 5000.")

# Ask for the number of steps the user walked and save it in a variable:
steps = input("How many steps did you walk today? ")
steps = int(steps)

# Check for goal and produce answer accordingly
if steps > 10000:
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")

if steps < daily_goal:
    print("Good start, but try to walk a bit more tomorrow!")

if steps == daily_goal:
    print("Bullseye! You hit your goal exactly!")

if steps == 0:
    print("Did you forget your phone today? You have 0 steps!")

# Signal the app closing
print("Tracker closing...")