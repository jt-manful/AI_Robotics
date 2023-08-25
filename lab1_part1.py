#!/usr/bin/env python3

# Left motor is output_c, and right_motor is output_b
from ev3dev2.motor import MoveTank, LargeMotor, OUTPUT_C, OUTPUT_B
# multiplier = (circumference of turn) / (cicumference of wheel)
def turnLeft(angle, speed):
    tank = MoveTank(OUTPUT_B, OUTPUT_C)
    tank.on_for_degrees(left_speed=0, right_speed=speed, degrees=angle/multiplier)
    print('Done!')

def turnRight(angle,speed):
    tank = MoveTank(OUTPUT_B, OUTPUT_C)
    tank.on_for_degrees(left_speed=speed, right_speed=0, degrees=angle/multiplier)
    print('Done!')