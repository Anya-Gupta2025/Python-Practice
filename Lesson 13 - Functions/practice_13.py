"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing a function for calculating the circumference, 
# and calling each calculate function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# Calculate the area of a rectangle based on length and width from user
def calculate_area():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The area is {length * width } units².")


# Write a function here for calculating the circumference after getting length and width from user
def calculate_perimeter():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The perimeter is {length * 2 + 2 * width } units.")



# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Circumference Calculator")

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        
        # Call the function for calculating area here
        calculate_area()

    elif choice == "2":

        # Call the function for calculating circumference here
        calculate_perimeter()

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================

main()