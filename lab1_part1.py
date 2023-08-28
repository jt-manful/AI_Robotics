#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
import math

# initailize motors
tank = MoveTank(OUTPUT_C, OUTPUT_B)

# global vars
WHEEL_CIRCUMFRENCE = 19.5
BASELINE = 15.15 #.17


# Distance is in centimeters
# Motor speed is between -1000 and 1000
def driveStraight(distance, speed):
    # Distance
    rotations_per_cent = 1/WHEEL_CIRCUMFRENCE
    rotation = distance * rotations_per_cent
    # Motor Speed
    motor_speed = (speed/1000)*100
    
    if not ( -1000<= speed and speed <= 1000):
        return -1
    
    tank.on_for_rotations(-motor_speed, -motor_speed, rotation)

def turn(angle, speed, direction):
   
    multiplier = (2*math.pi*BASELINE)/(WHEEL_CIRCUMFRENCE)
    motor_speed = (speed/1000)*100
    
    if not (0 <= motor_speed and motor_speed <= 1000):
        return -1
        
    if direction == 'left':
        tank.on_for_degrees(left_speed=0, right_speed=-motor_speed, degrees=angle*multiplier)
    elif direction == 'right':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=0, degrees=angle*multiplier)


# Function takes an angle, a motor speed and a direction and causes the 
# bot to spin either left or right.'
def spin(angle_deg, motor_speed, direction):
 
    # calculate actual turning angle 
    half_baseline = BASELINE /2
    multiplier = 2 * math.pi * half_baseline / WHEEL_CIRCUMFRENCE
    actual_rotational_degrees = angle_deg * multiplier

    motor_speed = (motor_speed/1000)*100

    if not (0 <=  motor_speed and motor_speed <= 1000):
        return -1
    
    if direction == 'right':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=motor_speed, degrees=actual_rotational_degrees)
    elif direction == 'left':
        tank.on_for_degrees(left_speed=motor_speed, right_speed=-motor_speed, degrees=actual_rotational_degrees)
    else:
         return -1


if __name__ == "__main__":
    # closed shape square
    # driveStraight(63, 500)
    # turn(90,500,'right')
    # driveStraight(63, 500)
    # turn(90,500,'right')
    # driveStraight(63, 500)
    # turn(90,500,'right')
    # driveStraight(63, 500)
    # turn(90,500,'right')
    
    # closed shape kite
    spin(40, 500, 'left')
    driveStraight(62, 500)
    turn(77,500,'right')
    driveStraight(50, 500)
    turn(106, 500,"right")
    driveStraight(50, 500)
    turn(77,500,'right')
    driveStraight(62, 500)
    turn(140,500, 'right')
