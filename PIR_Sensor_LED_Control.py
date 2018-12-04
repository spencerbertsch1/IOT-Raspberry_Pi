# Spencer Bertsch
# Dartmouth College - Winter 2018
# IOT Short Course, R-Pi Programming Demo
# This program blinks an LED pseudo randomly 
#

# Import needed modules
import time #<-- imports the time module
import RPi.GPIO as GPIO #<-- So we can use R-Pi GPIO Outs 
import random


#
led = 4     # connect the LED to this pin on the GPIO
pir = 17    # connect the PIR motion detector to this pin on the GPIO


# Set the mode for the pin
GPIO.setmode(GPIO.BCM)
# Set our LED, pin 7, to output
GPIO.setup(led, GPIO.OUT) #<-- OUTPUT, not an input!
# Set out PIR motion detector, pin 17 to input
GPIO.setup( pir, GPIO.IN )


try:
    while True: # we check the sensor forever with an infinite loop
        if GPIO.input(pir)==1:
            print "> motion detected"
            GPIO.output( led, 1 )
        else:
            GPIO.output( led, 0 )
        time.sleep( 0.1 ) # but we want to wait a little between each time we check
except KeyboardInterrupt: # when ctrl+c is pressed, turn LED off & the infinite loop stops
    pass

# the program is finished, we put things back in their original state
GPIO.cleanup()
