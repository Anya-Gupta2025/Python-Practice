# List of heroes
hero_data = {
    "Player1": {
        "class": "Warrior", 
        "health": 100, 
        "gear": ["shield", "sword"]
        }, 
    "Player2": {
        "class": "Mage", 
        "health": 65, 
        "gear": ["staff"]}
}

# Print hero data
print("\nCurrent Players: ")

# Run through the list of heroes
for i in range(len(hero_data)):
    print(f"\nPlayer {i+1}")

    if hero_data["Player"+str(i+1)]["class"] == "Warrior":
        print(f"Player {i+1} is a frontline fighter.")

    starting_weapon = hero_data["Player"+str(i+1)]["gear"][0]

    # Print the starting weapon for each player
    print(f"Starting weapon for Player {i+1}: {starting_weapon}")

# Update hero 2
hero_data["Player2"]["health"] = 75

# Print updated hero two
print(f"Updated Player 2 Data: {hero_data['Player2']}")

# IF the string "staff" is IN the list stored at hero_data "Player2" "gear"
# THEN print "Mage is fully equipped"
if "staff" in hero_data["Player2"]["gear"]:
    print("Mage is fully equipped\n")