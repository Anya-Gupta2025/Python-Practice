# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# Import random module
import random

## Wild Pokemon ##
# Variables
NAME = "name"
HEALTH = 0
TYPE = "type"
DAMAGE = 0

# Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
pokemon_info = [
    {NAME: "Pikachu", HEALTH: 100},
    {NAME: "Squirtle", HEALTH: 80},
    {NAME: "Bulbasaur", HEALTH: 60},
    {NAME: "Mewtwo", HEALTH: 40}
]

# User Pokemon
# Create a multidimensional list that holds 4 pokemon attacks and their different damage
pokemon_attack_info = [
    {TYPE: "Punch", DAMAGE: 2},
    {TYPE: "Kick", DAMAGE: 4},
    {TYPE: "Water Blast", DAMAGE: 6},
    {TYPE: "Electric Shock", DAMAGE: 8}
]

# Create a variable to hold a randomised wild pokemon
random_pokemon = random.choice(pokemon_info)

# Create a current_health variable and set it to the max health of the random pokemon
current_health = random_pokemon[HEALTH]

# Tell the user what pokemon they're facing
print(f"\nHello! You are facing the pokemon {random_pokemon[NAME]}!")
print(f"\nThe current health of the pokemon is {current_health}.")

# Create a while loop that continues until current health <= 0
while current_health > 0:

    # Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    attack = input("\nWhat attack would you like to choose (type the number of the one you want)?" \
    "\n1. Punch" \
    "\n2. Kick" \
    "\n3. Water Blast" \
    "\n4. Electric Shock" \
    "\n\nAnswer: ").strip()

    # Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    while True:
        try:
            attack = int(attack)
            if attack < 1 or attack > 4:
                attack = input("\nInvalid input, please enter the number regarding your choice of attack: ")
            else:
                break
            
        except:
            attack = input("\nInvalid input, please enter the number regarding your choice of attack: ")
            continue


    # Using the number, get the attack damage value and minus it from current health
    current_health -= pokemon_attack_info[attack-1][DAMAGE]
    print(f"\nThe current health of the pokemon is {current_health}.")

# Tell the user they defeated the pokemon
print("\nYou defeated the pokemon!\n")

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.