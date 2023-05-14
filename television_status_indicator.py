# Vergel, Chean Bernard Villanueva
# Televison Status Indicator

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
        self.tv_is_off = False

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
        print(f"The TV is {status}")
        if self.tv_is_on:
            print(f"The TV Channel: {self.tv_channel}")
            print(f"The Tv Volume: {self.tv_volume}")

# TestTV Class
class TestTV:
    def __init__(self):
        # Initialize two TV objects
        self.tv1 = TV()
        self.tv2 = TV()
    # Turn on TV1 and set the channel and volume
        # Turn on TV2 and set the channel and volume
        # Print the status of both TVs
# Create an instance of the test driver and run the test