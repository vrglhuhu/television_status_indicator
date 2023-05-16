# Vergel, Chean Bernard Villanueva
# Television Status Indicator

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
     if 1 <= channel <= maximum_channel:
        self.tv_channel = channel

    # Get the Volume of the TV
    def get_volume(self, volume):
        return self.tv_volume
    
    # Set the volume of the TV
    def set_volume(self, volume):
      maximum_volume = 7
      if 1 <= volume <= maximum_volume:
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
            print(f"\U0001F6D1 \033[1;34mThe TV Volume:\033[0m \033[0;31m\033[1m{self.tv_volume}\033[0m ")
            print(" ")

# Create an instance of the TV
TV()
