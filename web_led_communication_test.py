# Spencer Bertsch
# Dartmouth College - Winter 2018
# IOT Short Course, R-Pi Programming Demo
# This program blinks an LED pseudo randomly 
#
# Import needed modules
import time
import RPi.GPIO as GPIO
import random
#### o_o
import web
#### -_-

led = 4     # connect the LED to this pin on the GPIO
pir = 17      # connect the PIR motion detector to this pin on the GPIO

# Set the mode for the pin
GPIO.setmode( GPIO.BCM )
# Set our LED, pin 4, to output
GPIO.setup( led, GPIO.OUT )
# Set out PIR motion detector, pin 17 to input
GPIO.setup( pir, GPIO.IN )

def led_on():
    print "> LED on"
    GPIO.output( led, 1 )

def led_off():
    print "> LED off"
    GPIO.output( led, 0 )

try:
    web.server_start()
    web.register( "<button>Turn LED on</button>", led_on )
    web.register( "<button>Turn LED off</button>", led_off )


# the program is finished, we put things back in their original state
print "> finishing"
web.server_stop()
led_off()
GPIO.cleanup()

