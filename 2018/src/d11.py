# Day 11 of 2018
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def find_cell_value(y, x, grid_serial):

    rack_id = x +10

    power_level = rack_id * y
    power_level += grid_serial
    power_level *= rack_id

    power_level =  str(power_level)

    if len(power_level) >= 3:
        power_level = int(power_level[-3])
        
    else:
        power_level = 0

    power_level -= 5

    return power_level

def generate_square(side_size, grid_serial):
    grid = np.zeros((side_size, side_size))

    for j in range(side_size):
        for i in range(side_size):
            grid[j, i] = find_cell_value(j+1, i+1, grid_serial)

    return grid

def parse_3by3(grid):

    max_power = 0

    for j in range(len(grid)-2):
        for i in range(len(grid)-2):
            if max_power < np.sum(grid[j:j+3, i:i+3]):
                max_power = np.sum(grid[j:j+3, i:i+3])
                max_pwr_coord = [j+1,i+1]

    return max_power, max_pwr_coord

def parse_any(grid):
    max_power = 0

    for size in range(1, 300):
        for j in range(len(grid)-(size-1)):
            for i in range(len(grid)-(size-1)):
                if max_power < np.sum(grid[j:j+size, i:i+size]):
                    max_power = np.sum(grid[j:j+size, i:i+size])
                    max_pwr_coord = [j+1,i+1, size]


    return max_power, max_pwr_coord
            

# =============== TEST CASES ====================
assert find_cell_value(5,3,8) == 4
assert find_cell_value(79,122,57) == -5
assert find_cell_value(196,217,39) == 0
assert find_cell_value(153,101,71) == 4

grid = generate_square(300, 18)
max_power, max_pwr_coord = parse_3by3(grid)
assert max_power == 29
assert max_pwr_coord == [45, 33]

max_power, max_pwr_coord = parse_any(grid)
assert max_power == 113
assert max_pwr_coord == [269, 90, 16]


# =============== PART 1 & 2 ====================

with open('./2018/inputs/d11.txt') as f:
    for row in f:
        grid_serial = int(row.strip())

grid = generate_square(300, grid_serial)
max_power, max_pwr_coord = parse_3by3(grid)

print(f'Part 1 solution: {max_pwr_coord[1]},{max_pwr_coord[0]}')

max_power, max_pwr_coord = parse_any(grid)

print(f'Part 2 solution: {max_pwr_coord[1]},{max_pwr_coord[0]},{max_pwr_coord[2]}')