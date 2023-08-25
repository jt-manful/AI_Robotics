#!/usr/bin/env python3

# Left motor is output_c, and right_motor is output_b
from ev3dev2.motor import LargeMotor, MoveTank, OUTPUT_C, OUTPUT_B

# initailize motors 
left_motor = LargeMotor(OUTPUT_C)
right_motor = LargeMotor(OUTPUT_B)


def driveStraight():
    pass

def turnLeft(angle, speed):
    pass


# Function takes an angle, a motor speed and a direction and causes the 
# bot to spin either left or right.
def spin(angle_deg, motor_speed, direction):
    tank = MoveTank(OUTPUT_B, OUTPUT_C)

    if not (0 >= motor_speed and motor_speed <= 1000):
        return -1
    
    if direction == 'right':
            tank.on_for_degrees(left_speed=motor_speed, right_speed=-motor_speed, degrees=angle_deg)
    elif direction == 'left':
        tank.on_for_degrees(left_speed=-motor_speed, right_speed=motor_speed, degrees=angle_deg)
    else:
         return -1