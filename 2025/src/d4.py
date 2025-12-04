# Day 4 of 2025
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def digitize_grid(grid):
    digital_grid = []

    for row in grid:
        digital_row = []
        for symbol in row:
            if symbol == '.':
                digital_row.append(0)
            elif symbol == '@':
                digital_row.append(1)
            else:
                raise ValueError('unknown symbol')
        
        digital_grid.append(digital_row)

    return np.array(digital_grid)

def check_movable(grid):

    maxy = len(grid)
    maxx = len(grid[0])

    movable_s = []

    for j in range(maxy):
        for i in range(maxx):
            adjacent_s = 0
            current_s = grid[j, i]

            # only check if the current position is a roll
            if current_s == 0:
                continue

            adjacent_grid = grid[max(j-1, 0): min(j+1, maxy)+1,
                                 max(i-1, 0): min(i+1, maxx)+1]
            
            adjacent_s = np.sum(adjacent_grid) - current_s

            if adjacent_s < 4:
                movable_s.append([j, i])

    return movable_s

def remove_rolls(grid):

    # moved in current iteraction
    # total moved count all
    moved = 1
    total_moved = 0

    # this is for drawing
    grid_collection = [grid.copy()]

    while moved > 0:

        # for easier code, I'll redo the first pass here as well
        to_move = check_movable(grid)
        # how many will be moved
        moved = len(to_move)
        total_moved += moved
        for [j,i] in to_move:
            grid[j,i] = 0

        # for drawing at each step
        grid_collection.append(grid.copy())

    return total_moved, grid_collection



# =============== TEST CASES ====================
test_grid = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

test_grid = test_grid.strip()
test_grid = digitize_grid(test_grid.split('\n'))
test_movable = check_movable(test_grid)
assert len(test_movable) == 13
test_moved, _ = remove_rolls(test_grid)
assert test_moved == 43

# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2025/inputs/d4.txt') as f:
    for row in f:
        puzzle_input.append(row.strip())

grid = digitize_grid(puzzle_input)
movable = check_movable(grid)

moved, grid_collection = remove_rolls(grid)

print('Part 1 solution:', len(movable))
print('Part 2 solution:', moved)

# for i, grid in enumerate(grid_collection):
#     if i == 0:
#         name = 'Initial'
#     else:
#         name = 'Final'
#     plt.figure(figsize=(8, 8))
#     sns.heatmap(grid, cmap='Greys_r', square=True, cbar=False)
#     plt.axis('off')
#     plt.title(f'{name} grid of paper rolls')
#     plt.savefig(f'./2025/img/paper_rolls_{name.lower()}_d4.png', bbox_inches='tight', pad_inches=0.1)

from PIL import Image
import io

frames = []

for i, grid in enumerate(grid_collection): 
    # Create the plot
    plt.figure(figsize=(8, 8))
    sns.heatmap(grid, cmap='Reds_r', square=True, cbar=False)
    plt.axis('off')
    plt.title(f'Paper rolls at step {i}')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    
    frames.append(Image.open(buf).copy())
    
    plt.close() 
    buf.close()

frames[0].save(
    './2025/img/paper_rolls_d4.gif',
    save_all=True,
    append_images=frames[1:],
    duration=500,  # ms/frame
    loop=0  # 0 means loop 
)