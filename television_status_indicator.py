# Vergel, Chean Bernard Villanueva
# Televison Status Indicator

# Import pyfiglet 
import pyfiglet
from termcolor import colored
from pyfiglet import Figlet

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

# Make a TV Class
class TV:
    def __init__(self):
       # Initialize TV attributes
        self.tv_is_on = True
        self.tv_channel = 1
        self.tv_volume = 1

    # Turn on the TV
    def turn_on(self):
        self.tv_is_on = True

    # Turn off the TV
    def turn_off(self):
        self.tv_is_on = False

    # Get the Channel of the TV
    def get_channel(self): 
        return self.tv_channel
    
    # Set the channel of the TV
    def set_channel(self, channel):
     maximum_channel = 120
     if self.tv_channel <= 1 and channel <= maximum_channel:
        self.tv_channel = channel

    # Get the Volume of the TV
    def get_volume(self, volume):
        return self.tv_channel
    
    # Set the volume of the TV
    def set_volume(self, volume):
      maximum_volume = 7
      if self.tv_volume <= 1 and volume <= maximum_volume:
        self.tv_volume = volume

    # Increases the channel number by 1, if it's not already at 120.
    def tv_channel_up(self):
      maximum_channel = 120
      if self.tv_channel < maximum_channel:
        self.tv_channel += 1

    # Decrease the channel number by 1, if it's  already at 120.
    def tv_channel_down(self):
      maximum_channel = 120
      if self.tv_channel > maximum_channel:
        self.tv_channel -= 1

    # Increase the volume level by 1, if it's not already at 7.
    def tv_volume_up(self):
       maximum_volume = 7
       if self.tv_volume < maximum_volume:
          self.tv_volume += 1

    # Decrease the volume level by 1, if it's  already at 7.
    def tv_volume_down(self):
       maximum_volume = 7
       if self.tv_volume > maximum_volume:
          self.tv_volume -= 1

    # Print the current status of the TV
    def print_status(self):
        if self.tv_is_on:
            status = "ON"
        else:
            status = "OFF"
        print(f"\033[1;32mThe TV is\033[0m {status}")
        if self.tv_is_on:
            print(f"\U0001F6D1 \033[1;33mThe TV Channel:\033[0m \033[0;31m\033[1m{self.tv_channel}\033[0m")
            print(f"\U0001F6D1 \033[1;34mThe TV Volume:\033[0m \033[0;31m\033[1m{self.tv_volume}")
            print(" ")

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
        print("\n\033[0;31m\033[4mTELEVISON STATUS INDICATOR\033[0m\n")
        print("\U0001F4CC \033[4m\033[1;35mTV1:\033[0m")
        self.tv1.print_status()

        print("\n\U0001F4CC \033[4m\033[1;35mTV2:\033[0m")
        self.tv2.print_status()

# Create an instance of the test driver and run the test
test = TestTV()
test.run_test()