# Day 3 of 2017
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def create_memory_grid(square_nr):
    # find out the needed grid size
    for grid_shape in range(1, 1000000, 2):
        if grid_shape**2 >= square_nr:
            break

    memory_grid = np.zeros((grid_shape, grid_shape), dtype=np.int64)
    
    return memory_grid

def next_memory_pos(current_y, current_x, current_dir, memory_grid):

    # always check to the left of current direction
    # example: going R, then the left is y-1
    match current_dir:
        case 'U':
            if memory_grid[current_y, current_x-1] == 0:
                current_x = current_x-1
                current_dir = 'L'
            else:
                current_y = current_y-1

        case 'D':
            if memory_grid[current_y, current_x+1] == 0:
                current_x = current_x+1
                current_dir = 'R'
            else:
                current_y = current_y+1

        case 'L':
            if memory_grid[current_y+1, current_x] == 0:
                current_y = current_y+1
                current_dir = 'D'
            else:
                current_x = current_x-1

        case 'R':
            if memory_grid[current_y-1, current_x] == 0:
                current_y = current_y-1
                current_dir = 'U'
            else:
                current_x = current_x+1

        case _:
            raise('unknown direction!')
        
    return current_y, current_x, current_dir

def calculate_pos_value(current_y, current_x, memory_grid):

    tmp_val = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (0 <= (current_y + j) < memory_grid.shape[1]) and (0 <= (current_x + i) < memory_grid.shape[0]):
                tmp_val += memory_grid[current_y + j, current_x + i]

    memory_grid[current_y, current_x] = tmp_val

def memory_unpack(square_nr):

    memory_grid = create_memory_grid(square_nr)
    current_x = memory_grid.shape[0] // 2
    current_y = memory_grid.shape[1] // 2

    # start in center
    current_dir = 'D'
    memory_grid[current_y, current_x] = 1

    is_valid = True
   
    for i in range(1, square_nr):
        current_y, current_x , current_dir = next_memory_pos(current_y, current_x, current_dir, memory_grid)
        if is_valid:
            calculate_pos_value(current_y, current_x, memory_grid)

            # dont need to keep calculating it - also, it very quickly explodes and overflows
            if memory_grid[current_y, current_x] > square_nr:
                first_larger = memory_grid[current_y, current_x]
                is_valid = False
        else:
            memory_grid[current_y, current_x] = -1

    return abs(current_x - memory_grid.shape[0] // 2) + abs(current_y - memory_grid.shape[1] // 2), first_larger, memory_grid


# =============== TEST CASES ====================
test_memory = {12: 3,
               23: 2,
               1024: 31}


for test_sq, val in test_memory.items():
    assert memory_unpack(test_sq)[0] == val
# 
# =============== PART 1 & 2 ====================

with open('./2017/inputs/d3.txt') as f:
    for row in f:
        square_nr = int(row.strip())

num_steps, first_larger, memory_grid = memory_unpack(square_nr)

print('Part 1 solution:', num_steps)
print('Part 2 solution:', first_larger)


positive_vals = np.where(memory_grid > 0)
# just until the part 2 solution
memory_grid = memory_grid[min(positive_vals[0]):max(positive_vals[0]+1), min(positive_vals[1]): max(positive_vals[1])+1]
# print(memory_grid)

plt.figure(figsize=(8, 8))
sns.heatmap(np.log(memory_grid),  cmap='Oranges', square=True, cbar=False)
plt.axis('off')
plt.title(f'Spiraling Memory Allocation!')
plt.savefig(f'./2017/img/spiral_memory_d3.png', bbox_inches='tight', pad_inches=0.1)
