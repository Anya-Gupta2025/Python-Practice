"""
PROGRAM: Geometry Helper
This program helps to calculate the area and perimeter of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing functions for calculating the area and perimeter 
# taking the user input and returning it, 
# and calling each function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# Write a function here for calculating the area of a rectangle using passed values. 
def rectangle_area(length, width):
    area = length * width

    # Return the result.
    return area


# ------->>>> Write a function here for calculating the perimeter using passed values. 
def rectangle_perimeter(length, width):
    perimeter = 2 * length + 2 * width

    #  ------->>>> Return the result.
    return perimeter

def display_result(message):
    print("\n------------------")
    print(message)
    print("------------------")

# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Perimeter Calculator")

    length = int(input("\nWhat is the length of your rectangle?").strip())
    width = int(input("\nWhat is the width of your rectangle?").strip())

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "1":
        
        # Call the function for calculating area here and save it into variable 'area'
        area = rectangle_area(length, width)

        display_result(f"The area of your rectangle is {area}².")

    elif choice == "2":

        # Call the function for calculating perimeter here and save it into variable 'perimeter'
        perimeter = rectangle_perimeter(length, width)

        display_result(f"The perimeter of your rectangle is {perimeter}.")

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================

main()