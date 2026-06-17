# Pre-defined variables for security status and alarm sound

security_status = "LOCKED"

alarm_sound = "SIREN"

# Function to trigger alarm
def trigger_alarm():
    print(f"Alert! Sounding the {alarm_sound}")

# Function to check the system
def check_system():
    print("Checking home network stability...")

    if security_status == "LOCKED":
        print("All doors are secured.")
    else:
        trigger_alarm()


# PSEUDOCODE - Change the following pseudocode into code

# DEFINE a new function called reset_system
def reset_system():

    # INSIDE the function, print "System rebooting..."
    print("System rebooting...")

# The main body of code
def main():
    print(f"The current alarm sound is: {alarm_sound}")
    check_system()
    reset_system()

# Calling the main function
main()
