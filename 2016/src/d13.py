# Day 13 of 2016
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def map_office(office_layout, od_fnr):
    y_len, x_len = office_layout.shape

    for y in range(y_len):
        for x in range(x_len):
            room_sum = x*x + 3*x + 2*x*y + y + y*y + od_fnr
            num_1s = bin(room_sum).count('1')
            
            if num_1s % 2 == 1:
                office_layout[y, x] = 1

def possible_moves(y, x, office_layout, step_nr):

    moves = []

    for step in [1, -1]:
        # check boundries first and then for walls
        if 0 <= y + step < office_layout.shape[0]:
            if office_layout[y + step, x] == 0:
                moves.append([(y + step, x), step_nr])

        if 0 <= x + step < office_layout.shape[1]:
            if office_layout[y, x + step] == 0:
                moves.append([(y, x + step), step_nr])

    return moves

def journey_through_office(start_x, start_y, end_x, end_y, office_layout):
    fastest_path = float('inf')
    step_nr = 0

    # starting room, 0 steps
    checked_rooms = {(start_y, start_x): step_nr}
    

    moving = possible_moves(start_y, start_x, office_layout, step_nr+1)
    queue = deque(moving)

    while queue:
        (y, x), step_nr = queue.popleft()

        # we arrived at wanted office
        if y == end_y and x == end_x:
            fastest_path = min(fastest_path, step_nr)
            continue

        if step_nr >= fastest_path:
            continue

        # found a faster path here
        if (y,x) in checked_rooms:
            if checked_rooms[(y,x)] <= step_nr:
                continue

        checked_rooms[(y,x)] = step_nr

        moving = possible_moves(y, x, office_layout, step_nr+1)
        queue.extend(moving)
    
    return fastest_path, checked_rooms

    

# =============== TEST CASES ====================
test_design_map = """.#.####.##
..#..#...#
#....##...
###.#.###.
.##..#..#.
..##....#.
#...##.###"""

test_design = []

for line in test_design_map.split('\n'):
    tmp_line = []
    for char in line:
        if char == '.':
            tmp_line.append(0)
        else:
            tmp_line.append(1)

    test_design.append(tmp_line)

test_design = np.array(test_design)

# first verify that I'm making the map correctly.
test_office = np.zeros((7,10))
test_od_fnr = 10

map_office(test_office, test_od_fnr)
assert (test_design == test_office).all()
assert journey_through_office(1, 1,  7, 4, test_office)[0] == 11


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d13.txt') as f:
    for row in f:
        od_fnr = int(row) # office designer favorite number

office = np.zeros((50,50))
map_office(office, od_fnr)
nr_steps, reached_locations = journey_through_office(1, 1, 31, 39, office)


print('Part 1 solution:', nr_steps)

# for plotting
office_explored = np.zeros((50,50)) 

num_reached_loc = 0
for (y,x), v in reached_locations.items():
    office_explored[y, x] = v
    if v <= 50:
        num_reached_loc += 1

# just to show better on map - otherwise it's step 0
office_explored[1,1] = -1

print('Part 2 solution:', num_reached_loc)

plt.figure(figsize=(8, 8))
sns.heatmap(office,  cmap='Greys', square=True, cbar=False)
sns.heatmap(office_explored, cmap='viridis_r', square=True, mask=np.where(office_explored == 0, 1,0))
plt.axis('off')
plt.title(f'Getting lost through the office!')
plt.savefig(f'./2016/img/office_lost_d13.png', bbox_inches='tight', pad_inches=0.1)