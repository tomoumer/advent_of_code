# Day 6 of 2015
import numpy as np
import matplotlib.pyplot as plt
import re

class LightGrid:

    def __init__(self):
        self.grid = np.zeros((1000,1000))

    def switch_lights(self, instructions):
        x_start, y_start, x_end, y_end = map(int, re.findall(r'\d+', instructions))

        if 'turn on' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = 1
        elif 'turn off' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = 0
        elif 'toggle' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = np.abs(self.grid[x_start: x_end+1, y_start: y_end+1] -1)
        else:
            raise('uh oh unknown instructions')
        
    def ancient_swithch_lights(self, instructions):
        x_start, y_start, x_end, y_end = map(int, re.findall(r'\d+', instructions))

        if 'turn on' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = self.grid[x_start: x_end+1, y_start: y_end+1] + 1
        elif 'turn off' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = np.maximum(0, self.grid[x_start: x_end+1, y_start: y_end+1] - 1)
        elif 'toggle' in instructions:
            self.grid[x_start: x_end+1, y_start: y_end+1] = self.grid[x_start: x_end+1, y_start: y_end+1] + 2
        else:
            raise('uh oh unknown instructions')

    def reset(self):
        self.grid = np.zeros((1000,1000))



# load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d6.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

my_awesome_lights = LightGrid()

# ================= PART 1 ======================
test_cases = {'turn on 0,0 through 999,999': 1000000,
              'toggle 0,0 through 999,0': 1000,
              'turn on 499,499 through 500,500': 4}

for instructions, total_lights in test_cases.items():
    my_awesome_lights.reset()
    my_awesome_lights.switch_lights(instructions)
    assert np.sum(my_awesome_lights.grid) == total_lights, f"problem with {instructions}"

my_awesome_lights.reset()
for instructions in puzzle_input:
    my_awesome_lights.switch_lights(instructions)


plt.figure(figsize=(8, 8))
plt.imshow(my_awesome_lights.grid, cmap='copper', aspect='equal') 
plt.axis('off')
plt.title('My Best Light Show')
plt.savefig('./2015/img/lights_d6.png', bbox_inches='tight', pad_inches=0)
plt.close()
# plt.show()

print('Part 1 solution:', int(np.sum(my_awesome_lights.grid)) )

# ================= PART 2 ======================
test_cases = {'turn on 0,0 through 0,0': 1,
              'toggle 0,0 through 999,999': 2000000}

for instructions, total_lights in test_cases.items():
    my_awesome_lights.reset()
    my_awesome_lights.ancient_swithch_lights(instructions)
    assert np.sum(my_awesome_lights.grid) == total_lights, f"problem with {instructions}"

my_awesome_lights.reset()
for instructions in puzzle_input:
    my_awesome_lights.ancient_swithch_lights(instructions)

plt.figure(figsize=(8, 8))
plt.imshow(my_awesome_lights.grid, cmap='copper', aspect='equal') 
plt.axis('off')
plt.title('My Best Light Show')
plt.savefig('./2015/img/lights_ancient_d6.png', bbox_inches='tight', pad_inches=0)
plt.close()

print('Part 2 solution:', int(np.sum(my_awesome_lights.grid)))
