#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.on_for_degrees(left_speed=-50, right_speed=50, degrees=360)
print('Done!')