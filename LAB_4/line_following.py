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
TURN_ANG = 10
MOTOR_SPEED = 200
LEFT = 'left'
RIGHT = 'right'



# initailizations
tank = MoveTank(OUTPUT_B, OUTPUT_C)
#color_sensor = ColorSensor()
button = Button()
sound = Sound()
sonar = UltrasonicSensor()
threshold_val= 0 # light sensor



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
def bang_bang_control(k_b_b, input, threshold, offset):
    motor_speed = 0
    error = threshold - input
    motor_speed = k_b_b * (error) + offset
    return motor_speed


# line following routine based on bang bang
def line_following_routine(motor_speed):
    while True:
        input_val = color_sensor.reflected_light_intensity
        print("Sensor input", input_val)
        if input_val < threshold_val:
            print("turing ", LEFT)
            turn(TURN_ANG, motor_speed, LEFT)
        elif input_val > threshold_val:
            print("input: ", input_val, " ", "threshold: ", threshold_val)
            print("turing ", RIGHT)
            turn(TURN_ANG, motor_speed, RIGHT)
        time.sleep(0.1)

# line following routine based on P-control
def p_control(Kp, target_dist, offset):
   while True:
        cur_distance = sonar.distance_centimeters
        print("Distance from object: ", cur_distance)
        cur_error = target_dist - cur_distance
        output = cur_error*Kp + offset
        tank.on(left_speed = output, right_speed = output)


def pd_control(Kp, Kd, target_dist, offset):
    while True:
        cur_distance = sonar.distance_centimeters
        print("Distance from object: ", cur_distance)        
        cur_error = target_dist - cur_distance
        integral = integral + cur_error
        correction = (cur_error)*Kp + (cur_error - last_error)*Kd + offset
        output = correction
        tank.on(left_speed = output, right_speed = output)
        last_error = cur_error

# EXTRA
def pid_control(Kp, Ki, Kd, target_dist, offset):
    while True:
        cur_distance = sonar.distance_centimeters
        print("Distance from object: ", cur_distance)
        cur_error = target_dist - cur_distance
        integral = integral + cur_error
        correction = (cur_error)*Kp + (integral)*Ki + (cur_error - last_error)*Kd + offset
        output = correction
        tank.on(left_speed = output, right_speed = output)
        last_error = cur_error


if __name__ == "__main__":
    # threshold_val = calibration()
    # BANG BANG
    # while True:        
    #     threshold_val = 58
    #     bang_motor_speed = abs(bang_bang_control(k_b_b= 5, input=input_val, threshold=threshold_val))
    #     line_following_routine(bang_motor_speed)

    # PID - EXTRA
    p_control()
        