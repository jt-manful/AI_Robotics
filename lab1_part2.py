from lab1_part1 import driveStraight, turn, spin

#global vars
TURN_ANGLE = 90
MOTOR_SPEED = 50
LEFT = 'left'
RIGHT = 'right'

# open file 
file = open("navigation.txt", 'r')

directions_array = []

for line in file:
     directions_array = line.split(",")

array_count = 0
while array_count < len(directions_array):
    
    if directions_array[array_count] == 'stop':
         break
    if 'forward' in directions_array[array_count]:
        direction = directions_array[array_count].split(' ')[0]
        distance = int(directions_array[array_count].split(' ')[1])
        actual_distance = 44.0 * distance
        driveStraight(distance=actual_distance, speed=MOTOR_SPEED)

    if 'left' in directions_array[array_count]:
         turn(TURN_ANGLE, MOTOR_SPEED,LEFT)

    if 'right' in directions_array[array_count]:
         turn(TURN_ANGLE,MOTOR_SPEED,RIGHT)

    array_count += 1
        
     
