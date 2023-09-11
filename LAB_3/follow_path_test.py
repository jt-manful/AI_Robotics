
# !/usr/bin/env python3
# imports
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
import time
import math


# initailize motors
tank = MoveTank(OUTPUT_B, OUTPUT_C)

# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 14.6 
SPIN_ANG = 90
MOTOR_SPEED = 300
LEFT = 'left'
RIGHT = 'right'
TILE_DISTANCE = 50.50 


# Names of cardinal directions corresponding to the integers 0, 1, 2, 3, 4, 5, 6, 7
directions = ['east','south-east','south','south-west','west','noth-west','north','north-east']

# Computes the direction of pos2 relative to pos1, if pos2 is adjacent to pos1
# pos1 and pos2 are assumed to be tuples in the form (x,y)
# Direction is represented as an integer between 0 (corresponding to east) and
# 3 (corresponding to north)
# Throws an exception if pos2 is not adjacent to pos1
def relDirection(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    if x2==x1 and y2==y1+1:
        dir = 0
    elif x2==x1+1 and y2==y1+1:
        dir = 1
    elif x2==x1+1 and y2==y1:
        dir = 2
    elif x2==x1+1 and y2==y1-1:
        dir = 3
    elif x2==x1 and y2==y1-1:
        dir = 4
    elif x2==x1-1 and y2==y1-1:
        dir = 5
    elif x2==x1-1 and y2==y1:
        dir = 6
    elif x2==x1-1 and y2==y1+1:
        dir = 7
    else:
        raise ValueError(str(pos1)+" and " + str(pos2) + " are not neighbors,"\
                         +"so cannot compute relative direction between them.")
    return dir

# Assuming the robot starts at startPosition, facing the direction startOrientation,
# This function enables the robot to follow the path (a list of tuples representing
# positions) stored in the parameter path.
def followPath(startPosition, startOrientation, path):
    curPos = startPosition
    curDir = startOrientation

    for i in range(len(path)):
        nextPos = path[i]
        relDir = relDirection(curPos, nextPos)
        print("At pos " + str(curPos) + " facing direction " + str(curDir)
              + " (" + directions[curDir] + ")")
        print("Next pos is " + str(nextPos)
              + ", whose direction relative to the current pos is "
              + str(relDir) + " (" + directions[relDir] + ")")
        print()
              
        # TO DO: IF NECESSARY, TURN TO FACE IN THE CORRECT DIRECTION
        resultant_direction = curDir - relDir

        if resultant_direction == 1 or resultant_direction == -7:
            spin(45, MOTOR_SPEED, LEFT)
        if resultant_direction == -1 or resultant_direction == 7:
            spin(45, MOTOR_SPEED, RIGHT)
        if resultant_direction == 2 or resultant_direction == -6:
            spin(SPIN_ANG, MOTOR_SPEED, LEFT)
        if resultant_direction == 6 or resultant_direction == -2:
            spin(SPIN_ANG, MOTOR_SPEED, RIGHT)
        if resultant_direction == 4 or resultant_direction == -4:
            spin(180, MOTOR_SPEED, RIGHT)
    
        # TO DO: MOVE ONE CELL FORWARD INTO THE NEXT POSITION
        driveStraight(MOTOR_SPEED, TILE_DISTANCE)
        
        # Update the current position and orientation
        curPos = nextPos
        curDir = relDir



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

# Test the code
if __name__ == "__main__":
    testStartPos = (0,0)
    testStartOrientation = 0
    testPath = [(0,1),(1,1),(1,2),(2,2),(2,1),(2,0),(1,0)]

    followPath(testStartPos, testStartOrientation, testPath)
        
