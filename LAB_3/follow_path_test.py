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
              
        # TO DO: IF NECESSARY, TURN TO FACE IN THE CORRECT DIRECTION
        # TO DO: MOVE ONE CELL FORWARD INTO THE NEXT POSITION

        # Update the current position and orientation
        curPos = nextPos
        curDir = relDir


# Test the code
if __name__ == "__main__":
    testStartPos = (0,0)
    testStartOrientation = 0
    testPath = [(0,1),(1,1),(1,2),(2,2),(2,1),(2,0),(1,0)]

    followPath(testStartPos, testStartOrientation, testPath)
        
