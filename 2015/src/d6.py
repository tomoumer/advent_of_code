# Day 6 of 2015
import numpy as np
import matplotlib.pyplot as plt
import re

# =========== CLASSES AND FUNCTIONS =============
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

def plot_lights(lights_grid, name=''):
    plt.figure(figsize=(8, 8))
    plt.imshow(lights_grid, cmap='copper', aspect='equal') 
    plt.axis('off')
    plt.title('My Best Light Show')
    plt.savefig(f'./2015/img/{name}_d6.png', bbox_inches='tight', pad_inches=0)
    plt.close()

# =============== TEST CASES ====================
test_lights = LightGrid()
test_cases = {'turn on 0,0 through 999,999': 1000000,
              'toggle 0,0 through 999,0': 1000,
              'turn on 499,499 through 500,500': 4}

for instructions, total_lights in test_cases.items():
    test_lights.reset()
    test_lights.switch_lights(instructions)
    assert np.sum(test_lights.grid) == total_lights

test_cases = {'turn on 0,0 through 0,0': 1,
              'toggle 0,0 through 999,999': 2000000}

for instructions, total_lights in test_cases.items():
    test_lights.reset()
    test_lights.ancient_swithch_lights(instructions)
    assert np.sum(test_lights.grid) == total_lights


# ================ PART 1 & 2 =====================
all_instructions = []

with open('./2015/inputs/d6.txt') as f:
    for row in f:
        all_instructions.append(row.strip())

my_awesome_lights = LightGrid()
my_even_awesomer_lights = LightGrid()

for instructions in all_instructions:
    my_awesome_lights.switch_lights(instructions) # part 1
    my_even_awesomer_lights.ancient_swithch_lights(instructions) # part 2

plot_lights(my_awesome_lights.grid, 'lights')
plot_lights(my_even_awesomer_lights.grid, 'lights_ancient')

print('Part 1 solution:', int(np.sum(my_awesome_lights.grid)) )
print('Part 2 solution:', int(np.sum(my_even_awesomer_lights.grid)))
