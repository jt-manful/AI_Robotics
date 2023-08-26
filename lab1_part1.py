#!/usr/bin/env python3

# Left motor is output_c, and right_motor is output_b
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B
import math

# initailize motors 
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)
tank = MoveTank(left_motor_port=OUTPUT_C, right_motor_port=OUTPUT_B)

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

def turnLeft(angle, speed):
    pass


# Function takes an angle, a motor speed and a direction and causes the 
# bot to spin either left or right.'
def spin(angle_deg, motor_speed, direction):
 
    # calculate actual turning angle (confirm calculations with joel)
    baseline = 12.1 
    distance_travelled = (2 * math.pi * baseline) / 360
    actual_rotational_degrees = 0


    if not (0 >= motor_speed and motor_speed <= 1000):
        return -1
    
    if direction == 'right':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=motor_speed, degrees=actual_rotational_degrees)
    elif direction == 'left':
        tank.on_for_degrees(left_speed=motor_speed, right_speed=-motor_speed, degrees=actual_rotational_degrees)
    else:
         return -1