# Initialize map
world_map = [[0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0]]

start = (2, 1)
goal = (3, 4)


def neighboring_cells(curPos, world_map):
    '''The function  as a parameter: a tuple representing the current position,
      and return a list of tuples representing the neighboring cells. '''
   
    neighboring_cells = []
    map_y = len(world_map[0])
    map_x = len(world_map)
    curPos_x, curPos_y = curPos

    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x == 0 and y == 0 or x == 1 and y == 1 
                or x == -1 and y == -1 
                or x == -1 and y == 1
                or x == 1 and y == -1):
                continue  
            new_x, new_y = curPos_x + x, curPos_y + y
            if 0 <= new_x < map_x and 0 <= new_y < map_y and world_map[new_x][new_y] != 1:
                neighboring_cells.append((new_x, new_y))

    return neighboring_cells




def best_path(wavefront_map, startLoc):
    ''' given a completed wavefront plan will repeatedly determine the next cell to traverse to,
        by examining its neighboring cells to see which has the lower non-obstacle value.
        It should add the coordinates of this cell to a list and also print them to the screen
        (or play an audio representation), with an appropriate pause between each print statement 
        to enable a human reader to follow what is happening.  The code stops when it adds the coordinates
        of the goal cell to the list, and then it returns the list.  To test this code, you can manually
        populate a 2D array with the values that would be generated by a wavefront planner.'''
    
    nearby_cells = []
    min_cell_value = wavefront_map[startLoc[0]][startLoc[1]]
    path = []
    while goal not in nearby_cells:
        nearby_cells = neighboring_cells(startLoc, wavefront_map)
        
        for cell in nearby_cells:
            cell_x, cell_y = cell
            cur_cell_value = wavefront_map[cell_x][cell_y]
            if cur_cell_value < min_cell_value:
                min_cell_value = cur_cell_value
                next_cell = cell
                
        path.append(next_cell)
        startLoc = next_cell
    
    return path


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            # Check if the current coordinates are within the bounds of the array
            if i < len(map) and j < len(map[0]):
                print(map[i][j], end=" ")
            else:
                # If not, print an empty space
                print(" ", end=" ")
        print() 



def wavefront_algorithm(world_map, goalLoc):
    map_x = len(world_map)
    map_y = len(world_map[0])
    x_goal, y_goal = goalLoc


    world_map[x_goal][y_goal] = 2
    frontier = []
    explored_set =set()
    frontier.append((x_goal, y_goal)) 
    

    while frontier:
        current_cell = frontier.pop(0)
        explored_set.add((x_goal,  y_goal))
        x_cur = current_cell[0]
        y_cur = current_cell[1]
        # print("on the frontier: ",current_cell)
        # neighbours can use the neighbouring cells function.
        neighbors = neighboring_cells(current_cell, world_map) # check all cells
        # print("its neighbours: ", neighbors)
        for neighbour in neighbors:
            if neighbour not in explored_set:
                world_map[neighbour[0]][neighbour[1]] = world_map[x_cur][y_cur] + 1
                
                frontier.append ((neighbour[0],  neighbour[1]))
                explored_set.add((neighbour[0],  neighbour[1]))
        # print_map(world_map)

    return world_map



# if __name__ == "__main__":
#     # print(neighboring_cells((1,3), world_map1))
#     world_map = wavefront_algorithm(world_map, goal)
#     print_map(world_map)
#     best_path = best_path(world_map, start)
#     print("best path: ", best_path)