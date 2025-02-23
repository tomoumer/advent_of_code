# Day 3 of 2015
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# import sys
# import scipy

# =========== CLASSES AND FUNCTIONS =============
class Santa:
    
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        self.visited = {(x,y): 1}

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '>':
            self.x += 1
        elif direction == '<':
            self.x -= 1
        else:
            raise('unrecognized move!' )
        
        # once moved, the dict of visited houses needs to be updated
        current_coord = (self.x, self.y)
        if current_coord in self.visited:
            self.visited[current_coord] += 1
        else:
            self.visited[current_coord] = 1

        
    def radio_instructions(self, instructions):
        self.reset()
        for direction in instructions:
            self.move(direction)

    def reset(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visited = {(x,y): 1}

def plot_santa_journey(visited, who='Santa'):
    xs = [x for (x, y) in visited.keys()]
    ys = [y for (x, y) in visited.keys()]

    # grid boundries
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # I want it rectangular
    grid_dim = max(max_x - min_x + 1, max_y - min_y + 1)

    visited_array = np.zeros((grid_dim, grid_dim))
    for (x, y), value in visited.items():
        col = x - min_x
        row = max_y - y 
        visited_array[row, col] = value

    # print('dict size', sys.getsizeof(visited))
    # print('numpy array size', sys.getsizeof(visited_array))
    # print('sparse size', sys.getsizeof(scipy.sparse.csr_matrix(visited_array)))

    plt.figure(figsize=(8, 8))
    sns.heatmap(visited_array, cmap="viridis", square=True, mask=np.where(visited_array < 1, 1,0))
    plt.axis('off')
    plt.title(f'{who} Visited Houses')
    plt.savefig(f'./2015/img/{who}_d3.png', bbox_inches='tight', pad_inches=0)
    plt.close()

# =============== TEST CASES ====================

test_santa = Santa(0,0)
test_robo_santa = Santa(0,0)

test_cases = {'>': 2,
              '^>v<': 4,
              '^v^v^v^v^v': 2}

for instructions, num_houses in test_cases.items():
    test_santa.radio_instructions(instructions)
    assert len(test_santa.visited) == num_houses

# test 2
test_cases = {'^v': 3,
              '^>v<': 3,
              '^v^v^v^v^v': 11}

for instructions, num_houses in test_cases.items():
    test_santa.reset(0,0)
    test_robo_santa.reset(0,0)

    test_santa.radio_instructions(instructions[::2])
    test_robo_santa.radio_instructions(instructions[1::2])

    total_houses = test_santa.visited | test_robo_santa.visited
    assert len(total_houses) == num_houses


# ================= PART 1 ======================

santa = Santa(0,0)
robo_santa = Santa(0,0)


with open('./2015/inputs/d3.txt') as f:
    for row in f:
        all_instructions = row.strip()

# print('input values', len(all_instructions))

santa.radio_instructions(all_instructions)
plot_santa_journey(santa.visited, 'Santa_alone')
print('Part 1 solution:', len(santa.visited))


# ================= PART 2 ======================

santa.radio_instructions(all_instructions[::2])
robo_santa.radio_instructions(all_instructions[1::2])
plot_santa_journey(santa.visited, 'Santa_with_robot')
plot_santa_journey(robo_santa.visited, 'Santa_robot')

total_houses = santa.visited | robo_santa.visited
print('Part 2 solution:', len(total_houses))






