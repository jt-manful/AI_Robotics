
# Initialize map
world_map = [[0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0]]

world_map2 = [[9, 8, 7, 6, 5],
             [10, 9, 1, 1, 4],
             [11, 10, 1, 4, 3], 
             [12, 1, 4, 3, 2]]
 
start = (2, 1)
goal = (3, 4)

# Given the coordinates of a cell, you will want to be able 
# to quickly compute the coordinates of its (up to) four neighboring cells.  
# You should write a function to do this. 
#  The function can take as a parameter a tuple representing the
#  current position, and it can return a list of tuples representing the neighboring cells. 



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


def next_move(wavefront_map, startLoc):
    ''' given a completed wavefront plan will repeatedly determine the next cell to traverse to,
        by examining its neighboring cells to see which has the lower non-obstacle value.
        It should add the coordinates of this cell to a list and also print them to the screen
        (or play an audio representation), with an appropriate pause between each print statement 
        to enable a human reader to follow what is happening.  The code stops when it adds the coordinates
        of the goal cell to the list, and then it returns the list.  To test this code, you can manually
        populate a 2D array with the values that would be generated by a wavefront planner.'''
    
    nearby_cells = []
    min_cell_value = wavefront_map[startLoc[0]][startLoc[1]]
    path = [startLoc]
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
if __name__ == "__main__":
    # print(neighboring_cells(start, world_map2))
    print(next_move(world_map2, start))