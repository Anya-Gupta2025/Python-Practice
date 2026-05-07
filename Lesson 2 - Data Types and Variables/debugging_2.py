# 3 Question Quiz - Debug all the errors, including any semantic errors.

INSTRUCTIONS = "This is a quick 3 part quiz. A question will be asked, and then you answer it. Let's begin!"
points = 0

name = input("Hi! What's your name? ").title()
print(f"Hello {name}!")
print(INSTRUCTIONS)

print("First question:")
answer_1 = int(input("How many millimetres in a centimetre? "))
if answer_1 == 10:
    print("That's correct, the answer is 10!")
    points += 1

else:
    print("Nope, the answer is 10!")

print()


print("Next Question:")
answer_2 = input("What is the capital of New Zealand? ").lower()
if answer_2 == "wellington":
    print("That's correct, the answer is Wellington. That was easy, wasn't it?")
    points += 1
else:
    print("Nope, the answer is Wellington.")

print()


print("Final Question!")
answer_3 = int(input("What is 3 x 6? "))
if answer_3 == 18:
    print("That's correct, the answer is 18!")
    points += 1
else:
    print("Nope, the answer is 18.")

print()


print(f"Quiz finished! You got {points} points.")