# Print the answers to the following questions. Get the computer to do the math for you!

print()
print("This is an awesome which can calculate so many things! Here are some examples:")
print()

# What is 376 + 209 + 44439?
print("What is 376 + 209 + 44439?")
print(376 + 209 + 44439)
print()

# What is 2345678 - 678 - 1?
print("What is 2345678 - 678 - 1?")
print(2345678 - 678 - 1)
print()

# What is 345 divided by 34?
print("What is 345 divided by 34?")
print(345/34)
print()

# What is 567 * 34 * 3?
print("What is 567 * 34 * 3?")
print(567 * 34 * 3)
print()


# Print 'hello' 32 times.
print("Type hello 32 times:")
print("hello" * 32)
print()

# -------------------------

# EXTENSION

# What is 2345 / 766 rounded to the nearest whole number?
print("What is 2345 / 766 rounded to the nearest whole number?")
print((2345/766) // 1)
print()

# What is 456 to the power of 23?
print("What is 456 to the power of 23?")
print(456 ** 23)
print()

# What is the remainder if you divide 345 by 32?
print("What is the remainder if you divide 345 by 32?")
print(345%32)
print()

# --------------------------

# EXPERT (for those who already know some Python)
# Create a simple calculator
# GOAL: The user chooses Add, Subtract, Multiply or Divide, then inputs 2 numbers
#       The computer will output the result.
# (Optional) Make sure the user can only input numbers

print("This is a Python Calculator! Type in your operation (+, -, /, *) and your numbers in the following input sections!")
operator = input("Operator: ")
number_1 = float(input("Number 1: "))
number_2 = float(input("Number 2: "))

if operator == "*":
    print(number_1 * number_2)

elif operator == "/":
    print(number_1 * number_2)

elif operator == "-":
    print(number_1 - number_2)

elif operator == "+":
    print(number_1 + number_2)

else:
    print("Invalid operators!")