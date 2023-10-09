# Pico code that talks to Pygame Zero

import board
import pwmio
import time
import digitalio
from analogio import AnalogIn
from adafruit_simplemath import map_range

import nonblocking_serialinput as nb_serialin # from circuitpython community bundle, also need ansi_escape_code folder

servo = pwmio.PWMOut(board.GP15, variable_frequency=True)
servo.frequency = 50 # hz

buttonpin = digitalio.DigitalInOut(board.GP14)
buttonpin.direction = digitalio.Direction.INPUT

potentiometerpin = AnalogIn(board.A0)

servo_angle = 90

# to be able to call input() without blocking the rest of the code
# must use the new my_input.print() instead of the regular print()
my_input = nb_serialin.NonBlockingSerialInput()

while True:
    my_input.update() # update the usb communication
    input_string = my_input.input() # grab any new data recieved
    if input_string is not None:
        my_input.print("got: "+input_string)
        if ("a" in input_string):
            servo_angle = servo_angle + 3
            if (servo_angle > 180):
                servo_angle = 180
        if ("s" in input_string):
            servo_angle = servo_angle - 3
            if (servo_angle < 0):
                servo_angle = 0

    # command the rc servo position
    servo_duty = int(map_range(servo_angle,0,180,65535*0.5/20,65535*2.5/20))
    servo.duty_cycle = servo_duty
    
    # print the potentiometer voltage
    my_input.print("B "+str(potentiometerpin.value)+",")
    
    # print if the button is pressed
    if (buttonpin.value == 0):
        my_input.print("A")
    time.sleep(0.05)
