# Initialize map
world_map = [[0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

start = (6, 0)
goal = (3, 1)

def neighboring_cells(curPos, world_map):
    '''The function  as a parameter: a tuple representing the current position,
      and return a list of tuples representing the neighboring cells. '''
   
    neighboring_cells = []
    map_y = len(world_map[0])
    map_x = len(world_map)
    curPos_x, curPos_y = curPos

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue  
            new_x, new_y = curPos_x + x, curPos_y + y
            if 0 <= new_x < map_x and 0 <= new_y < map_y and world_map[new_x][new_y] != 1:
                neighboring_cells.append((new_x, new_y))

    return neighboring_cells




def best_path(wavefront_map, startLoc):
    '''function takes as a parameter the wavefront map and the start location
    and returns a list of tuples representing the best path from the start location to the goal location.'''
    
    
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
    # path.append(goal)
    
    return path


def print_map(map):
    '''function takes as a parameter a 2D array representing the map and prints it to the screen.'''
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
    '''function takes as a parameter a 2D array representing the map
    and a tuple representing the goal location and returns a 2D array representing the wavefront map.'''
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