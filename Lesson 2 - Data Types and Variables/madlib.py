import textwrap
import random

# Create a short Madlib: Get input from your user (a bunch of words), 
# then output a madlib using those words.

# Ask user for a name and save it in a variable
name = input("What is your name? ").title()

# Ask user for an animal and save it in a variable
animal = input("Give the name of a random animal: ").lower()

# Ask user for a colour and save it in a variable
colour = input("Type in the name of a random colour: ").lower()

# Ask user for an object and save it in a variable
object = input("Name a random object: ").lower()

# Print your madlib using the 4 variables above.
story = (f"{name} was walking down the road when she saw a {animal} by the road. It was so cute, yet so little. It was just a little friend, right? Nope! The {animal} jumped onto {name} and started turning a shade of {colour} while also pulling out a scary looking weapon. But when {name} looked closer, they realised it was just a hoax! Nothing else... But where did this little devil get such a unique weapon from? I wonder...")
final_story = textwrap.indent((textwrap.fill(story, width=90)), " " * 8)
print()
print(final_story)
print()

# ----------------------------

# EXTENSION
# Research about 'print formatting in python'. 
# Use what you learn to rewrite your madlib into easier to read code.
#DONE

# ----------------------------

# EXPERT (for those who already know some Python)
# Create a randomised madlib game
# GOAL: Just like above except...
#       Write 4-6 different madlibs and randomise which one is output.

# Ask user for a name and save it in a variable
name = input("What is your name? ").title()

# Ask user for an animal and save it in a variable
animal = input("Give the name of a random animal: ").lower()

# Ask user for a colour and save it in a variable
colour = input("Type in the name of a random colour: ").lower()

# Ask user for an object and save it in a variable
object = input("Name a random object: ").lower()

# Writing all the stories (2, 3, 4, 5, and 6 are written by Gemini)
stories = [f"{name} was walking down the road when she saw a {animal} by the road. It was so cute, yet so little. It was just a little friend, right? Nope! The {animal} jumped onto {name} and started turning a shade of {colour} while also pulling out a scary looking weapon. But when {name} looked closer, they realised it was just a hoax! Nothing else... But where did this little devil get such a unique weapon from? I wonder...", f"The famous Chef {name} was nervous. The secret ingredient for the Royal Soup was a rare, {colour} {object}, but it had been stolen! Suddenly, a tiny {animal} scurried across the kitchen floor. 'Aha!' shouted {name}, 'I shall cook for the king using only my wits!' It turned out the {animal} was actually a world-class food critic in disguise.", f"On a dark and {colour} night, {name} was struck by a glowing {object} that fell from the sky. The next morning, {name} woke up with the incredible ability to communicate with every {animal} in the city. Armed with nothing but a {object}, they became the hero known as 'The {colour} Guardian,' protecting the world from evil.", f"The museum was silent until {name} accidentally tripped over a {colour} display case. Inside was the Ancient {object} of Doom! Suddenly, a ghostly {animal} floated through the wall and began to howl. {name} grabbed the {object} and ran as fast as possible, only to realize the {animal} just wanted to play fetch.", f"Roses are red, violets are {colour}, I found a {object}, and gave it to you! But {name} didn't realize that this wasn't just any ordinary gift. As soon as the {object} touched their hand, a wild {animal} burst through the window! It seems the {object} was actually a legendary artifact that the {animal} had been guarding for centuries. Now, {name} has to decide: return the {colour} treasure, or start a new life as a professional poem-writing outlaw."]

# Choosing a random number
final_story = random.choice(stories)

# Formatting final sotry and printing it
final_story = textwrap.indent((textwrap.fill(final_story, width=90)), " " * 8)

print()
print(final_story)
print()