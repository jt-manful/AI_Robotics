#!/usr/bin/env python3

# imports
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sensor.lego import ColorSensor
import time
import math

# initailize parts
tank = MoveTank(OUTPUT_B, OUTPUT_C)
color_sensor = ColorSensor()
# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 14.6 
SPIN_ANG = 90
MOTOR_SPEED = 300
LEFT = 'left'
RIGHT = 'right'
TILE_DISTANCE = 50.50 


 #Distance is in centimeters
# Motor speed is between -1000 and 1000
def driveStraight(speed, distance):
    '''function takes in two params, distance and speed and causes the bot to drive
      either forward or backward in in straight line for a given distance at a certain speed'''
    # Distance
    rotations_per_cent = 1/WHEEL_CIRCUMFRENCE
    rotation = distance * rotations_per_cent
    # Motor Speed
    motor_speed = (speed/1000)*100
    
    if not ( -1000<= speed and speed <= 1000):
        return -1
    
    tank.on_for_rotations(motor_speed, motor_speed, rotation)
    


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


def spin(angle_deg, motor_speed, direction):
    '''function takes an angle, a motor speed and a direction and 
        causes the bot to spin either left or right a given angle for a given speed.'''
 
    # calculate actual turning angle 
    half_baseline = BASELINE /2
    multiplier = 2 * math.pi * half_baseline / WHEEL_CIRCUMFRENCE
    actual_rotational_degrees = angle_deg * multiplier

    motor_speed = (motor_speed/1000)*100

    if not (0 <=  motor_speed and motor_speed <= 1000):
        return -1
    
    if direction == 'right':
        tank.on_for_degrees(left_speed=motor_speed, right_speed=-motor_speed, degrees=actual_rotational_degrees)
    elif direction == 'left':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=motor_speed, degrees=actual_rotational_degrees)
    else:
         return -1


def color_guided_navigation():
    '''function: robot moves forward and turns based on color'''
    while not color_sensor.color == ColorSensor.COLOR_BLACK:
        if color_sensor.color == ColorSensor.COLOR_GREEN:
            spin(SPIN_ANG,MOTOR_SPEED/2,RIGHT)
            driveStraight(MOTOR_SPEED, TILE_DISTANCE)
        elif color_sensor.color == ColorSensor.COLOR_RED:
            spin(SPIN_ANG,MOTOR_SPEED/2,LEFT)
            driveStraight(MOTOR_SPEED, TILE_DISTANCE)
        else:
            driveStraight(MOTOR_SPEED, TILE_DISTANCE)



if __name__ == "__main__":
    #spin(90,300,RIGHT)
    color_guided_navigation()
    # while True:
    #     print(color_sensor.color_name)