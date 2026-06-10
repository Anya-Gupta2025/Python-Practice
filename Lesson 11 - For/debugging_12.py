# List of banned items
banned_items = ["slingshot","laser"]

# List of items in the inventory
inventory = ["apple","slingshot","book","laser"]

# Empty list for the items which have been confiscated
confiscated = []

# Scan inventory for confiscable goods
print(f"\nScanning inventory: (inventory)")

# Check each item in inventory using for loop
for item in inventory:
    if item in banned_items:
        print(f"\nAlert! Found banned item: {inventory[0]}")
        confiscated.append(item)
        inventory.remove(item)

print(f"\nScan complete. Total flag matches: {len(confiscated)}")
if len(confiscated) > 0:
    print("\nItems confiscated:")

    # FOR the number of items in the confiscated list (use index)
    for item in confiscated:
        # PRINT the item listed with a number (eg. 1. Laser)
        print(f"{confiscated.index(item)+1}. {item.title()}")

print()