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

# Set the mode for the pin
GPIO.setmode(GPIO.BCM)
# Set our LED, pin 7, to output
GPIO.setup(led, GPIO.OUT) #<-- OUTPUT, not an input! 
LED_state = 0

for i in range(0, 100):
    rand_num = random.random()/10
    time.sleep( rand_num )
    print("random number between 0 and 1: ", rand_num) 
    
    if LED_state==0:
        print "on"
        GPIO.output( led, 1 )
        LED_state = 1
    else:
        print "off"
        GPIO.output( led, 0 )
        LED_state = 0
    
# the program is finished, we put things back in their original state
GPIO.cleanup()


