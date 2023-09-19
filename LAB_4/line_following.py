#!/usr/bin/env python3

# imports
from ev3dev2.motor import MoveTank, ColorSensor, OUTPUT_C, OUTPUT_B
from ev3dev2.sound import Sound
from ev3dev2.button import Button
import time
import math


# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 14.6 
TURN_ANG = 90
MOTOR_SPEED = 200
LEFT = 'left'
RIGHT = 'right'
TILE_DISTANCE = 50.50
DIAGONAL_DISTANCE = 71.5


# initailizations
tank = MoveTank(OUTPUT_B, OUTPUT_C)
color_sensor = ColorSensor()
button = Button()
sound = Sound()
white_val, black_val = 0
threshold_val, input_val = 0
calibration = True

# calibration routine
def calibration():
    while calibration:
        str_en = "Calibration starting!!"
        sound.speak(str_en)

        str_en = "Place the robot on a white surface and press enter button to record the value "
        sound.speak(str_en)

        if button.enter:
            white_val = color_sensor.reflected_light_intensity
            time.sleep(0.1) # sleep for 5 seconds after recording value

        str_en = "Place the robot on a white surface and press enter button to record the value "
        sound.speak(str_en)

        if button.enter:
            black_val = color_sensor.reflected_light_intensity
            time.sleep(0.1) # sleep for 5 seconds after recording value

        threshold_val = math.avg(white_val, black_val)
        print("threshold value", threshold_val)

        str_en = "Press enter to confirm calibration complete "
        sound.speak(str_en)
        if button.enter:
            str_en = "Calibration complete"
            sound.speak(str_en)
            calibration =  False


# line following routine
def line_following_routine():
    while True:
        input_val = color_sensor.reflected_light_intensity
            
        if input_val < threshold_val:
            turn(TURN_ANG, MOTOR_SPEED, LEFT)
        elif input_val > threshold_val:
            turn(TURN_ANG, MOTOR_SPEED, RIGHT)

        time.sleep(0.1)

# turning code
def turn(angle, speed, direction):
    '''function takes an angle, a motor speed and a direction and 
        causes the bot to spin either left or right a given angle for a given speed.'''
   
    multiplier = (2*math.pi*BASELINE)/(WHEEL_CIRCUMFRENCE)
    motor_speed = (speed/1000)*100
    
    if not (0 <= motor_speed and motor_speed <= 1000):
        return -1
        
    if direction == 'left':
        tank.on_for_degrees(left_speed=0, right_speed=motor_speed, degrees=angle*multiplier)
    elif direction == 'right':
        tank.on_for_degrees(left_speed=motor_speed, right_speed=0, degrees=angle*multiplier)


# bang-bang control
def bang_bang_control():
    pass