# Day 22 of 2017
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def numpify_grid(grid_list, pad_amount):
    grid = []

    for row in grid_list:
        tmp_row = [0 if i == '.' else 1 for i in row]
        grid.append(tmp_row)

    grid = np.array(grid)
    grid = np.pad(grid, pad_amount, 'constant', constant_values=0)

    return grid

class Virus():

    def __init__(self, start_x, start_y, direction=[0, -1]):
        self.x = start_x
        self.y = start_y
        self.direction = direction
        self.infected = 0

    def infect_and_move(self, grid):
        current_node = grid[self.y, self.x]

        if current_node == 0:
            # left rotation
            rotation_matrix = np.array([[0, -1], [1, 0]])
            # infect
            grid[self.y, self.x] = 1
            self.infected += 1

        elif current_node == 1:
            # right rotation
            rotation_matrix = np.array([[0, 1], [-1, 0]])
            # uninfect
            grid[self.y, self.x] = 0

        else:
            raise('unknown node!')
        
        self.direction = np.matmul(self.direction, rotation_matrix)
        self.x += self.direction[0]
        self.y += self.direction[1]

    def mutated_infect_and_move(self, grid):
        current_node = grid[self.y, self.x]

        # now
        # 0 = clean
        # 1 = infected
        # 2 = weakened
        # 3 = flagged

        # clean
        if current_node == 0:
            # left rotation
            rotation_matrix = np.array([[0, -1], [1, 0]])
            self.direction = np.matmul(self.direction, rotation_matrix)
            # weaken
            grid[self.y, self.x] = 2
            

        # infected
        elif current_node == 1:
            # right rotation
            rotation_matrix = np.array([[0, 1], [-1, 0]])
            self.direction = np.matmul(self.direction, rotation_matrix)
            # flag
            grid[self.y, self.x] = 3

        # weakened
        elif current_node == 2:
            # same direction
            # infect
            grid[self.y, self.x] = 1
            self.infected += 1
            

        # flagged
        elif current_node == 3:
            # flip direction
            self.direction = -1 * self.direction
            # uninfect
            grid[self.y, self.x] = 0

        else:
            raise('unknown node!')
        
        
        self.x += self.direction[0]
        self.y += self.direction[1]
        

# =============== TEST CASES ====================

start_grid = ['..#',
'#..',
'...']

grid = numpify_grid(start_grid, 1000)

midpoint = len(grid) // 2
# print(start_grid)

virus_carrier = Virus(midpoint, midpoint)

for _ in range(10000):
    virus_carrier.infect_and_move(grid)

assert virus_carrier.infected == 5587

# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2017/inputs/d22.txt') as f:
    for row in f:
        puzzle_input.append(row.strip())


grid = numpify_grid(puzzle_input, 100)
midpoint = len(grid) // 2
virus_carrier = Virus(midpoint, midpoint)

for _ in range(10000):
    virus_carrier.infect_and_move(grid)


print('Part 1 solution:', virus_carrier.infected)

grid = numpify_grid(puzzle_input, 240)
midpoint = len(grid) // 2
virus_carrier = Virus(midpoint, midpoint)

for _ in range(10000000):
    virus_carrier.mutated_infect_and_move(grid)

print('Part 2 solution:', virus_carrier.infected)


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 8))
sns.heatmap(grid,  cmap='viridis', square=True, cbar=False)
plt.axis('off')
plt.title('Oh look ... pandemic!')
# plt.show()
plt.savefig(f'./2017/img/pandemic_d22.png', bbox_inches='tight', pad_inches=0.1)