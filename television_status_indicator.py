# Vergel, Chean Bernard Villanueva
# Televison Status Indicator

# Make a TV Class
class TV:
    def __init__(self):
       # Initialize TV attributes
        self.tv_is_on = True
        self.tv_channel = 1
        self.tv_volume = 7

    # Turn on the TV
    def turn_on(self):
        self.tv_is_on = True

    # Turn off the TV
    def turn_off(self):
        self.tv_is_on = False
        
    # Get the Channel of the TV
    # Set the channel of the TV
    # Get the Volume of the TV
    # Set the volume of the TV
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