#!/usr/bin/env python3

# imports
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
import time
import math

# initailize motors
tank = MoveTank(OUTPUT_B, OUTPUT_C)

# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 14.6 

# Distance is in centimeters
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

DISTANCE = 150 # METERS

if __name__ == "__main__":

    # driveStraight(100, 50)
    # driveStraight(200, 150)
    # time.sleep(15)
    # driveStraight(300, 150)
    # time.sleep(15)
    # driveStraight(400, 150)
    # time.sleep(15)
    # driveStraight(500, 150)
    # time.sleep(15)
    # driveStraight(600, 150)
    # time.sleep(15)
    # driveStraight(700, 150)
    # time.sleep(15)
    # driveStraight(800, 150)
    # time.sleep(15)
    driveStraight(900, 150)
    
   