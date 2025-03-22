# Day 1 of 2016
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
class WalkingMan():

    def __init__(self, orientation=[0,1], position=[0,0]):
        self.orientation = np.array(orientation)
        self.position = np.array(position)
        # part 2
        self.map = np.array([])
        self.positionhq = np.array([])

    def decypher_instructions(self, instructions):
        for instruction in instructions.split(','):
            instruction = instruction.strip()
            turn = instruction[0]
            walk = int(instruction[1:])
            self.turn_and_walk(turn, walk)

    def turn_and_walk(self, turn, walk):
        # turning using matrices
        if turn == 'L':
            rotation_matrix = np.array([[0, -1], [1, 0]])
        elif turn == 'R':
            rotation_matrix = np.array([[0, 1], [-1, 0]])
        else:
            raise('unknown rotation!')
        
        self.orientation = np.matmul(self.orientation, rotation_matrix)

        # update the grid as we walk
        for i in range(walk):
            self.position += self.orientation
            self.map[self.position[0]][self.position[1]] += 1
        
            if (self.map[self.position[0]][self.position[1]] > 1) and (self.positionhq.size == 0):
                self.positionhq = self.position.copy()

    def back_to_beginning(self, orientation=[0,1], position=[0,0]):
        self.orientation = np.array(orientation)
        self.position = np.array(position)
        self.map = np.array([])
        self.positionhq = np.array([])

    # I mean clearly, what else, Apple??
    def set_google_maps(self, grid):
        self.map = grid
        # have to re-center;
        self.position = np.array([len(grid) //2 , len(grid) // 2])     

# =============== TEST CASES ====================
test_walker = WalkingMan()


test_instructions = {'R2, L3': 5,
                     'R2, R2, R2': 2,
                     'R5, L5, R5, R3': 12}

for instructions, distance in test_instructions.items():
    test_walker.back_to_beginning()
    test_walker.set_google_maps(np.zeros((12,12)))
    test_walker.decypher_instructions(instructions)

    assert abs(test_walker.position[0] - 6) + abs(test_walker.position[1]- 6) == distance

# =============== PART 1 & 2 ====================

me_walking = WalkingMan()

with open('./2016/inputs/d1.txt') as f:
    for row in f:
        instructions = row.strip()
        total_steps = sum(list(map(int, re.findall('\d+', row))))


me_walking.set_google_maps(np.zeros((total_steps, total_steps)))
me_walking.decypher_instructions(instructions)

# needs adjustment because center is not 0,0
print('Part 1 solution:', abs(me_walking.position[0] - total_steps // 2) + abs(me_walking.position[1] - total_steps // 2))
print('Part 2 solution:', abs(me_walking.positionhq[0] - total_steps // 2) + abs(me_walking.positionhq[1]  - total_steps // 2))


# plot for fun!
borders = np.where(me_walking.map > 0)
xmin = borders[1].min() -3
xmax = borders[1].max() +3
ymin = borders[0].min() -3
ymax = borders[0].max() +3

plt.figure(figsize=(8, 8))
sns.heatmap(me_walking.map, cmap="viridis", square=True, mask=np.where(me_walking.map < 1, 1,0))
plt.axis('off')
plt.xlim(xmin,xmax)
plt.ylim(ymin, ymax)
plt.title(f'City Walking')
plt.savefig(f'./2016/img/city_walk_d1.png', bbox_inches='tight', pad_inches=0)
plt.close()
