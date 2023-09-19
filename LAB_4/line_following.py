#!/usr/bin/env python3

# imports
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor.lego import  ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
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
OFFSET = 0
TIME = 0.2


# initailizations
tank = MoveTank(OUTPUT_B, OUTPUT_C)
color_sensor = ColorSensor()
button = Button()
sound = Sound()
#sonar = UltrasonicSensor()



threshold_val=0
input_val = 0
target_dist = 15
integral = 0
last_error = 0
maxspeed_allowed = 700
Kp = 0.1
Kd = 0.1
Ki = 0

# calibration routine
def calibration():
    calibration = True
    while calibration:
        str_en = "Calibration starting"
        sound.speak(str_en)

        str_en = "Place the robot on a white surface and press enter button to record the value "
        sound.speak(str_en)

        while not button.enter:
            white_val = color_sensor.reflected_light_intensity
           
            time.sleep(0.1) # sleep for 5 seconds after recording value

        print("white val", white_val)
        str_en = "Place the robot on a black surface and press enter button to record the value "
        sound.speak(str_en)

        while not button.enter:
            black_val = color_sensor.reflected_light_intensity
            time.sleep(0.1) # sleep for 5 seconds after recording value

        print("black val", black_val)
        threshold_val = int((white_val + black_val)/2)
        print("threshold value", threshold_val)

        str_en = "Press enter to confirm calibration complete "
        sound.speak(str_en)
        while not button.enter:
            pass
        str_en = "Calibration complete"
        sound.speak(str_en)
        calibration =  False
    return threshold_val

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
# bang bang switches abruptly between two states
# input: light sensor reading
# sensor light sensor 
# output: motor speed ??
# error: is desired - actual
# controller: ev3
def bang_bang_control(k_b_b, input, threshold):
    motor_speed = 0
    error = threshold - input
    motor_speed = k_b_b * (error) + OFFSET
    return motor_speed


# line following routine based on bang bang
def line_following_routine(input_val, motor_speed):
    while True:
        if input_val < threshold_val:
            turn(TURN_ANG, motor_speed, LEFT)
        elif input_val > threshold_val:
            turn(TURN_ANG, motor_speed, RIGHT)
        time.sleep(0.1)


def pid():
    while True:
        cur_distance = sonar.distance_centimeters
        cur_error = target_dist - cur_distance
        integral = integral + cur_error
        correction = (cur_error)*Kp + (integral)*Ki + (cur_error - last_error)*Kd
        output = correction*(maxspeed_allowed)
        tank.on_for_seconds(left_speed = output, right_speed = output, seconds=TIME)
        last_error = cur_error


if __name__ == "__main__":
    threshold_val = calibration()
    # BANG BANG
    # while True:        
    #     input_val = color_sensor.reflected_light_intensity
    #     bang_motor_speed = abs(bang_bang_control(k_b_b= 20, input=input_val, threshold=threshold_val))
    #     line_following_routine(bang_motor_speed)

    # PID - EXTRA
        