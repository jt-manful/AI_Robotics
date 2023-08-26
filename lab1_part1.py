#!/usr/bin/env python3

# Left motor is output_c, and right_motor is output_b
from ev3dev2.motor import MoveTank, OUTPUT_C, OUTPUT_B
import math

# initailize motors 
tank = MoveTank(OUTPUT_C, OUTPUT_B)

# Distance is in centimeters
# Motor speed is between -1000 and 1000
def driveStraight(distance, speed):
    # Distance
    wheel_radius = 2.8 # centimeters
    wheel_circumference = 2 * math.pi * wheel_radius
    rotations_per_cent = 1/wheel_circumference
    rotation = distance * rotations_per_cent
    # Motor Speed
    motor_speed = (speed/1000) * 100
    
    tank.on_for_rotations(motor_speed, motor_speed, rotation)

def turn(angle, speed, direction):
    baseline = 16
    wheel_circumference = 19.5 
    multiplier = (2*math.pi*baseline)/(wheel_circumference)
    
    if not (0 <= speed and speed <= 1000):
        return -1
        
    if direction == 'left':
        tank.on_for_degrees(left_speed=0, right_speed=speed, degrees=angle*multiplier)
    elif direction == 'right':
        tank.on_for_degrees(left_speed=speed, right_speed=0, degrees=angle*multiplier)


# Function takes an angle, a motor speed and a direction and causes the 
# bot to spin either left or right.'
def spin(angle_deg, motor_speed, direction):
 
    # calculate actual turning angle 
    half_baseline = 8.0
    wheel_circumfrence = 19.5
    multiplier = 2 * math.pi * half_baseline / wheel_circumfrence
    actual_rotational_degrees = angle_deg * multiplier

    if not (0 <=  motor_speed and motor_speed <= 1000):
        return -1
    
    if direction == 'right':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=motor_speed, degrees=actual_rotational_degrees)
    elif direction == 'left':
        tank.on_for_degrees(left_speed=motor_speed, right_speed=-motor_speed, degrees=actual_rotational_degrees)
    else:
         return -1