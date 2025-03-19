# Day 24 of 2016
import numpy as np
from collections import deque
from itertools import combinations, permutations

# =========== CLASSES AND FUNCTIONS =============
def possible_moves(y, x, ducts_grid, step_nr):

    moves = []

    for step in [1, -1]:
        # check boundries first and then for walls
        # boundries really are not needed here
        if 0 <= y + step < ducts_grid.shape[0]:
            if ducts_grid[y + step, x] > -2:
                moves.append([(y + step, x), step_nr])

        if 0 <= x + step < ducts_grid.shape[1]:
            if ducts_grid[y, x + step] > -2:
                moves.append([(y, x + step), step_nr])

    return moves

# each one of these will find the very next closest location to visit
def find_next_location(start, stop, ducts_grid):
    fastest_path = float('inf')

    y, x = np.argwhere(ducts_grid == start)[0]
    y_stop, x_stop = np.argwhere(ducts_grid == stop)[0]

    step_nr = 0
    checked_spaces = {(y, x): step_nr}

    moving = possible_moves(y, x, ducts_grid, step_nr+1)
    queue = deque(moving)


    while queue:
        (y, x), step_nr = queue.popleft()

        # we arrived at the second place
        if (y == y_stop) and (x == x_stop):
            fastest_path = min(step_nr, fastest_path)
            continue
     

        if step_nr >= fastest_path:
            continue

        # found a faster path here
        if (y,x) in checked_spaces:
            if checked_spaces[(y,x)] <= step_nr:
                continue

        checked_spaces[(y,x)] = step_nr

        moving = possible_moves(y, x, ducts_grid, step_nr+1)
        queue.extend(moving)


    return fastest_path

def duct_it_up(ducts_grid):
    all_distances = {}

    visit_locations = list(range(np.max(ducts_grid) + 1))

    for start, stop in combinations(visit_locations, 2):
        step_nr = find_next_location(start, stop, ducts_grid)
        all_distances[(start, stop)] = step_nr

    # 0 is always first
    fastest_path = float('inf')
    final_fastest_path = float('inf')
    for i in  permutations(visit_locations[1:]):
        current_path = 0
        travel_path = [0] + list(i) + [0]
        for j in range(len(travel_path) - 1):
            point1 = travel_path[j]
            point2 = travel_path[j+1]

            if j == len(travel_path) - 2:
                fastest_path = min(fastest_path, current_path)

            if (point1, point2) in all_distances.keys():
                current_path += all_distances[(point1, point2)] 
            else:
                current_path += all_distances[(point2, point1)] 
        
        final_fastest_path = min(final_fastest_path, current_path)


    return fastest_path, final_fastest_path


# =============== TEST CASES ====================
test_ducts = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""

test_ducts_grid = []

for line in test_ducts.split('\n'):
    tmp_line = []
    for char in line:
        if char == '.':
            tmp_line.append(-1)
        elif char == '#':
            tmp_line.append(-2)
        else:
            tmp_line.append(int(char))


    test_ducts_grid.append(tmp_line)

test_ducts_grid = np.array(test_ducts_grid)

assert duct_it_up(test_ducts_grid)[0] == 14


# =============== PART 1 & 2 ====================
ducts_grid = []

with open('./2016/inputs/d24.txt') as f:
    for row in f:
        tmp_line = []
        for char in row.strip():

            if char == '.':
                tmp_line.append(-1)
            elif char == '#':
                tmp_line.append(-2)
            else:
                tmp_line.append(int(char))

        ducts_grid.append(tmp_line)

ducts_grid = np.array(ducts_grid)

shortest_path, shortest_path_complete = duct_it_up(ducts_grid) 

print('Part 1 solution:', shortest_path)
print('Part 2 solution:', shortest_path_complete)

# note .. maybe build a viz going through points