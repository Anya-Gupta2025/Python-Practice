### WHAT ANIMAL ARE YOU QUIZ ###
# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.

# Some variables:
a_score = 0
b_score = 0
c_score = 0
d_score = 0
response = False

# Function to tally up the points:
def tally_points(a):
    # Making variables global so that this function can modify them:
    global a_score, b_score, c_score, d_score, response

    response = False

    while response == False:
        if a == "a":
            a_score += 1
            response = True

        elif a == "b":
            b_score += 1 
            response = True

        elif a == "c":
            c_score += 1 
            response = True

        elif a == "d":
            d_score += 1
            response = True

        else:
            print("Invalid answer, try again. Make sure you answer is either 'a', 'b', 'c', 'd'.")
            a = input("Answer: ").lower() 


# Give instructions to the user
print()
print("Hello! Welcome to this quiz! Answer the next few questions in order to find out what animal you are! \n")


## 3 questions and 5 animals ##

# Ask your user a question about themselves, giving them 4 options
print("What kind of person are you?")
print(" a. Morning \n b. Afternoon \n c. Evening \n d. Night \n")

response_1 = input("Answer: ").lower()
print()

# Tally their score
tally_points(response_1)


# Ask the next question
print("What animal do you most find to most reasonate with you?")
print(" a. Fish \n b. Cat \n c. Dog \n d. Bird \n")

response_2 = input("Answer: ").lower()
print()

# Tally their score
tally_points(response_2)


#Ask the next question:

print("If you could choose a colour, what colour would you be?")
print(" a. Green \n b. Red \n c. Blue \n d. Yellow \n")

response_3 = input("Answer: ").lower()
print()

# Tally thier score
tally_points(response_3)


# Tell them their animal:

# If there is no clear option most selected, tell then they are aq Butterfly due to the way butterflies change from moth to the butterfly
if a_score < 2 and b_score < 2 and c_score < 2 and d_score < 2:
    print("You are a Butterfly.")
    print(a_score)
    print(b_score)
    print(c_score)
    print(d_score)

else:
    greatest = max(a_score, b_score, c_score, d_score)

    print()

    if greatest == a_score:
        print("You are a Shark.")

    elif greatest == b_score:
        print("You are a Lion.") 

    elif greatest == c_score:
        print("You are an Owl.") 

    else:
        print("You are a Duckling!")

print()