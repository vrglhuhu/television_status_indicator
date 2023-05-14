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
        self.tv_is_on = False

    # Get the Channel of the TV
    def get_channel(self): 
        return self.tv_channel
    
    # Set the channel of the TV
    def set_channel(self, channel):
     if self.tv_channel >= 1 and channel <= 120:
        self.tv_channel = channel

    # Get the Volume of the TV
    def get_volume(self, volume):
        return self.tv_channel
    
    # Set the volume of the TV
    def set_volume(self, volume):
     if self.tv_volume >= 1 and volume <= 7:
        self.tv_volume = volume

    # Increases the channel number by 1, if it's not already at 100.
    # Decrease the channel number by 1, if it's not already at 1.
    # Increase the volume level by 1, if it's not already at 7.
    # Decrease the volume level by 1, if it's not already at 1.
    # Print the current status of the TV

# TestTV Class
     # Initialize two TV objects
    # Turn on TV1 and set the channel and volume
        # Turn on TV2 and set the channel and volume
        # Print the status of both TVs
# Create an instance of the test driver and run the test