# Vergel, Chean Bernard Villanueva
# Television Status Indicator

# Import pyfiglet 
import pyfiglet
from termcolor import colored
from pyfiglet import Figlet

# Import the TV
from TV import TV

# Creating Header
print(" ")
print("\033[1;33m=\033[0m" * 60)
print("\033[1;34m=\033[0m" * 60)
welcome = Figlet(font= "digital")
welcome_output = (colored(welcome.renderText("Televison Status Indicator"), "green"))
print(welcome_output)
print("\033[1;35m=\033[0m" * 60)
print("\033[1;36m=\033[0m" * 60)
print("\n\033[40m\033[1;31mHi, I am Chean Bernard V. Vergel.\033[0m")

# Ask for the name of the user
name_user = input("\n\033[40m\033[0;35mHow about you what is your name? \033[0m")
print(f"\n\033[40m\033[0;32mHi, {name_user.title()}! I welcome you on this program. \033[0m")

# TestTV Class
class TestTV:
    def __init__(self):
        # Initialize two TV objects
        self.tv1 = TV()
        self.tv2 = TV()
        # Turn on TV1 and set the channel and volume
        self.tv1.turn_on()
        self.tv1.set_channel(30)
        self.tv1.set_volume(3)
        # Turn on TV2 and set the channel and volume
        self.tv2.turn_on()
        self.tv2.set_channel(3)
        self.tv2.set_volume(2)
        # Print the status of both TVs
        print("\n\033[0;31m\033[4mTELEVISON STATUS INDICATOR\033[0m")
        print("\U0001F4CC \033[4m\033[1;35mTV1:\033[0m")
        self.tv1.print_status()
        print("\n\U0001F4CC \033[4m\033[1;35mTV2:\033[0m")
        self.tv2.print_status()


        # Asking the user if they want to change the TV settings
        print("\033[0;31m\033[4mTELEVISON STATUS INDICATOR\033[0m")
        choice = input("\U0001F6A8\033[1;33mDo you want to change the TV settings?\033[0m (\033[40m\033[34mYES\033[0m or \033[40m\033[34mNO\033[0m): \033[0m")

        if choice.upper() == "YES":
            self.edit_settings()
        else:
            self.show_footer()

    # Defining the edit setting 
    def edit_settings(self):
     try:
        # Editing TV1 settings
        print("\n\033[0;34mEditing TV1 settings...\033[0m")
        channel = int(input("\033[40m\033[0;35mEnter the new channel for TV1: \033[0m"))
        self.tv1.set_channel(channel)
        volume = int(input("\033[40m\033[0;35mEnter the new volume for TV1: \033[0m"))
        self.tv1.set_volume(volume)

        # Editing TV2 settings
        print("\n\033[0;34mEditing TV2 settings...\033[0m")
        channel = int(input("\033[40m\033[0;35mEnter the new channel for TV2: \033[0m"))
        self.tv2.set_channel(channel)
        volume = int(input("\033[40m\033[0;35mEnter the new volume for TV2: \033[0m"))
        self.tv2.set_volume(volume)

        # Print the updated status of both TVs
        print("\n\U0001F4CC \033[4m\033[1;35mTV1:\033[0m")
        self.tv1.print_status()

        print("\n\U0001F4CC \033[4m\033[1;35mTV2:\033[0m")
        self.tv2.print_status()

        self.show_footer()

     except ValueError:
        print("\n\U0001F6D1\U0001F6E1\033[1;31mInvalid input! Please enter a valid number.\U0001F6D1\U0001F6E1\033[0m")
        self.edit_settings()

    def show_footer(self):
        print("\033[1;36m====================================================\033[0m")
        print("\033[0;31m\033[4mThank you for using the Television status indicator!\033[0m")
        print("\033[1;36m====================================================\033[0m\n")

# Create an instance of the test driver and run the test
TestTV()



