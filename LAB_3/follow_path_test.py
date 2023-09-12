#!/usr/bin/env python3

# imports
from planning_map import *
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
from ev3dev2.sound import Sound
import time
import math

# initailize motors
tank = MoveTank(OUTPUT_B, OUTPUT_C)

# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 14.6 
SPIN_ANG = 87
MOTOR_SPEED = 300
LEFT = 'left'
RIGHT = 'right'
TILE_DISTANCE = 50.50
START_OREINTATION = 0


# Names of cardinal directions corresponding to the integers 0, 1, 2, and 3
directions = ['east','south','west','north']

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
    elif x2==x1+1 and y2==y1:
        dir = 1
    elif x2==x1 and y2==y1-1:
        dir = 2
    elif x2==x1-1 and y2==y1:
        dir = 3
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
        
        # Robot feedback (sound)
        sound = Sound()
        str_en = "Turning to " + directions[relDir]
              
        # TO DO: IF NECESSARY, TURN TO FACE IN THE CORRECT DIRECTION
        resultant_direction = curDir - relDir
        if resultant_direction == 1 or resultant_direction == -3:
            sound.speak(str_en)
            spin(SPIN_ANG, MOTOR_SPEED, LEFT)
        if resultant_direction == -1 or resultant_direction == 3:
            sound.speak(str_en)
            spin(SPIN_ANG, MOTOR_SPEED, RIGHT)
        if resultant_direction == 2 or resultant_direction == -2:
            sound.speak(str_en)
            spin(180, MOTOR_SPEED, RIGHT)

        # TO DO: MOVE ONE CELL FORWARD INTO THE NEXT POSITION
        str_en = "Moving to " + str(path[i][0]) +" " + str(path[i][1])
        sound.speak(str_en)
        driveStraight(MOTOR_SPEED, TILE_DISTANCE)

        # Update the current position and orientation
        curPos = nextPos
        curDir = relDir
        
    sound.speak("I have arrived at my destination")



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
    world_map = wavefront_algorithm(world_map, goal)
    print_map(world_map)
    best_path = best_path(world_map, start)
    print("best path: ", best_path)
    followPath(start, START_OREINTATION, best_path)
        
