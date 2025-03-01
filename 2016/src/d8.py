# Day 8 of 2016
import numpy as np
import re
import matplotlib.pyplot as plt

# =========== CLASSES AND FUNCTIONS =============
class PowerDisplayTech:

    def __init__(self, dim_tall, dim_wide):
        self.grid = np.zeros((dim_tall, dim_wide))
        self.row_len = dim_wide
        self.col_len = dim_tall

    def process_instruction(self, instruction):
        num1, num2 = list(map(int, re.findall('\d+', instruction)))

        if 'rect' in instruction:
            self.turn_on(num1, num2)
        elif 'column' in instruction:
            self.rotate_col(num1, num2)
        elif 'row' in instruction:
            self.rotate_row(num1, num2)
        else:
            raise('unknown instruction')
            

    def turn_on(self, x, y):
        self.grid[:y,:x] = 1
        # print(self.grid)

    def rotate_row(self, y, num):
        temp_row = self.grid[y,:].copy()
        new_row = np.zeros(self.row_len)
        
        # after rotating, the indices of 1
        ones_index = [(i + num) % self.row_len for i in np.where(temp_row == 1)]
        new_row[ones_index] = 1

        self.grid[y,:] = new_row
        # print(self.grid)

    def rotate_col(self, x, num):
        temp_col = self.grid[:,x].copy()
        new_col = np.zeros(self.col_len)
        
        # after rotating, the indices of 1
        ones_index = [(i + num) % self.col_len for i in np.where(temp_col == 1)]
        new_col[ones_index] = 1

        self.grid[:,x] = new_col


# =============== TEST CASES ====================
test_display = PowerDisplayTech(3,7)


test_instructions = {'rect 3x2': '###....\n###....\n.......',
                     'rotate column x=1 by 1': '#.#....\n###....\n.#.....',
                     'rotate row y=0 by 4': '....#.#\n###....\n.#.....',
                     'rotate column x=1 by 1  ': '.#..#.#\n#.#....\n.#.....'}
# note had to add a few spaces to last instruction to make it a different key ...


for test_instruction, test_result in test_instructions.items():
    # this whole block here is to split into rows and then
    # transform the test instructions into np.arrays for comparison

    test_result = test_result.split('\n').copy()
    test_array = []
    for row in test_result:
        test_array.append([1 if x=='#' else 0 for x in row])
    test_array = np.array(test_array)

    test_display.process_instruction(test_instruction) 

    assert (test_display.grid == test_array).all()

# ================= PART 1 ======================
real_display = PowerDisplayTech(6,50)


with open('./2016/inputs/d8.txt') as f:
    for row in f:
        real_display.process_instruction(row.strip())



print('Part 1 solution:', int(np.sum(real_display.grid)))


# this isn't really the display, but I'm padding it to look nicer
real_display.grid = np.vstack([real_display.grid, np.zeros((2, real_display.grid.shape[1]))])
real_display.grid = np.vstack([np.zeros((2,real_display.grid.shape[1])), real_display.grid])
real_display.grid = np.hstack([real_display.grid, np.zeros((real_display.grid.shape[0], 2))])
real_display.grid = np.hstack([np.zeros((real_display.grid.shape[0], 2)), real_display.grid])


# ================= PART 2 ======================
plt.figure(figsize=(6, 2))
plt.imshow(real_display.grid, cmap='cividis', aspect='equal') 
plt.axis('off')
# plt.title('Display')
plt.savefig(f'./2016/img/card_display_d8.png', bbox_inches='tight', pad_inches=0)
plt.close()
print('Part 2 solution: see figure!')