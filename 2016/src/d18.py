# Day 18 of 2016
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def first_row(grid, input_str):
    for i, symbol in enumerate(input_str):
        if symbol == '.':
            grid[0, i] = 0
        else:
            grid[0, i] = 1


def find_traps_in_room(grid):

    # rows, skipping the start one
    for j in range(1, grid.shape[0]):

        for i in range(grid.shape[1]):

            if i == 0:
                left = 0
            else:
                left = grid[j-1, i-1]
            if i == grid.shape[1] -1:
                right = 0
            else:
                right = grid[j-1, i+1]

            center = grid[j-1, i]

            if (left == 1) and (center == 1) and (right == 0):
                new_val = 1
            elif (right == 1) and (center == 1) and (left == 0):
                new_val = 1
            elif (left == 1) and (center == 0) and (right == 0):
                new_val = 1
            elif (right == 1) and (center == 0) and (left == 0):
                new_val = 1
            else:
                new_val = 0

            grid[j, i] = new_val


# =============== TEST CASES ====================
test_floor = np.zeros((10,10))

first_row(test_floor, '.^^.^.^^^^')
find_traps_in_room(test_floor)
assert test_floor.shape[0] * test_floor.shape[1] - np.sum(test_floor) == 38

# =============== PART 1 & 2 ====================

with open('./2016/inputs/d18.txt') as f:
    for row in f:
        start_row = row.strip()

floor = np.zeros((40, len(start_row)))

first_row(floor, start_row)
find_traps_in_room(floor)


print('Part 1 solution:', int(floor.shape[0] * floor.shape[1] - np.sum(floor)))

crazy_floor = np.zeros((400000, len(start_row)))

first_row(crazy_floor, start_row)
find_traps_in_room(crazy_floor)

print('Part 2 solution:', int(crazy_floor.shape[0] * crazy_floor.shape[1] - np.sum(crazy_floor)))

plt.figure(figsize=(4, 12))
sns.heatmap(crazy_floor, cmap='RdBu_r', cbar=False)
plt.axis('off')
plt.title('Floor is Lava!')
# plt.show()
plt.savefig(f'./2016/img/avoiding_traps_d18.png', bbox_inches='tight', pad_inches=0)