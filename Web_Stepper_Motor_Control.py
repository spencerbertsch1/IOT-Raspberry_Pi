# Spencer Bertsch
# Dartmouth College - Winter 2018
# IOT Short Course, R-Pi Programming Demo
# This program allows the Pi to host a server which can be used to remotely turn a stepper motor
#
# Import needed modules
import time
import RPi.GPIO as GPIO
import random
import web
import stepper

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


stepper_left_total_steps = 0

def stepper_left_turn_clockwise( steps ):
    steps = int(steps)
    print "> stepper left " + str(steps) + " steps clockwise"
    stepper.actuate_left_motor( steps, True )
    global stepper_left_total_steps
    stepper_left_total_steps += steps
    return "Stepper motor left took " + str(stepper_left_total_steps) + " steps total"

def stepper_left_turn_counterclockwise( steps ):
    steps = int(steps)
    print "> stepper left " + str(steps) + " steps counter-clockwise"
    stepper.actuate_left_motor( steps, False )
    global stepper_left_total_steps
    stepper_left_total_steps -= steps
    return "Stepper motor left took " + str(stepper_left_total_steps) + " steps total"


try:
    web.server_start()
    web.register( "<button>Turn LED on</button>", led_on )
    web.register( "<button>Turn LED off</button>", led_off )

    web.arbitrary_html( "<br/>" )
    web.register( "<button>Stepper Left CW</button><input type=\"text\" placeholder=\"step_count\"/>", stepper_left_turn_clockwise )
    web.register( "<button>Stepper Left CCW</button><input type=\"text\" placeholder=\"step_count\"/>", stepper_left_turn_counterclockwise )


# the program is finished, we put things back in their original state
print "> finishing"
web.server_stop()
led_off()
GPIO.cleanup()
