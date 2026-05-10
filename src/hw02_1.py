# Complete Project Details: https://RandomNerdTutorials.com/raspberry-pi-digital-inputs-python/

# Import the Button and LED classes from the gpiozero library
from gpiozero import Button, LED
# Import pause to keep the program running
from signal import pause

# Create an LED object connected to GPIO pin 14
led = LED(14)
# Create a Button object connected to GPIO pin 4
button = Button(4)

# When the button is pressed, turn the LED on
button.when_pressed = led.on
# When the button is released, turn the LED off
button.when_released = led.off

# Keep the script running and waiting for button events
pause()