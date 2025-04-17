# Day 6 of 2018
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def create_areas(grid, coordinates):

    # for each point now need to find the sum of distances
    # this is for part 2
    grid_2 = deepcopy(grid)
    if len(grid) < 100:
        # for test
        total_dist = 32
    else:
        total_dist = 10000

    # fill the grid based on shortest distance
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            # if grid[row, col] > 0:
            #     continue
            # # determine closest
            # else:
            min_dist = 99999
            tmp_total_dist = 0
            for i, [x, y] in enumerate(coordinates):

                tmp_dist = np.abs(row - y) + np.abs(col - x)
                tmp_total_dist += tmp_dist
                # print(x, col, y, row, tmp_dist)

                # two coordinates are equidistant from this point
                if tmp_dist == min_dist:
                    grid[row, col] = 0

                elif tmp_dist < min_dist:
                    grid[row, col] = i+1
                    min_dist = tmp_dist
            # part 2
            if tmp_total_dist < total_dist:
                grid_2[row, col] = -1

    return grid, grid_2

def get_largest_finite_area(grid, num_coords):
    max_area = 0
    for i in range(num_coords):

        y_coords, x_coords = np.where(grid==i+1)
        
        # if the coord area touches the edge anywhere that means it will go infinite
        if (min(x_coords) == 0) or (max(x_coords) == len(grid[0]) -1):
            continue
        elif (min(y_coords) == 0) or (max(y_coords) == len(grid) -1):
            continue

        else:
            max_area = max(max_area, len(grid[grid==i+1]))

    return max_area


def build_grid(text_coordinates):

    coordinates = []
    max_x = 0
    max_y = 0
   

    for coord in text_coordinates:
        x, y = map(int, coord.split(','))
        # to know the extend of grid we need
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        # min_x = min(x, min_x)
        # min_y = min(y, min_y)
        
        coordinates.append([x, y])

    # NOTE: +1 because 0 indexed and another to not have them at edge
    grid = np.zeros((max_y + 2, max_x + 2))

    for i, [x,y] in enumerate(coordinates):
        grid[y, x] = i+1

    # make the areas
    grid_1, grid_2 = create_areas(grid, coordinates)

    # finally, count the area for any coord that is not on the edge
    max_area = get_largest_finite_area(grid_1, len(coordinates))

    # for part 2, just 
    max_region = len(grid_2[grid_2 == -1])


    return max_area, max_region, grid_2



# =============== TEST CASES ====================
coordinates = ['1, 1',
'1, 6',
'8, 3',
'3, 4',
'5, 5',
'8, 9']

max_area, max_region, _ = build_grid(coordinates)
assert max_area == 17
assert max_region == 16

# =============== PART 1 & 2 ====================
coordinates = []

with open('./2018/inputs/d6.txt') as f:
    for row in f:
        coordinates.append(row.strip())


max_area, max_region, grid_2 = build_grid(coordinates)

print('Part 1 solution:', max_area)
print('Part 2 solution:', max_region)

plt.figure(figsize=(8, 8))
sns.heatmap(grid_2,  cmap='cividis', square=True, cbar=False, mask=np.where(grid_2==0, 1, 0))
plt.axis('off')
plt.title('Equidistant area')
# plt.show()
plt.savefig(f'./2018/img/equidistant_area_d6.png', bbox_inches='tight', pad_inches=0.1)