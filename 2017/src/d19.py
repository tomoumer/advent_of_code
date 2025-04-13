# Day 19 of 2017
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def check_next_pipe(current_x, current_y, current_dir, pipes):
    next_y = current_y
    next_x = current_x

    if current_dir == 'u':
        next_y = current_y - 1
        if 0 <= next_y < len(pipes):
            next_pipe = pipes[next_y][current_x]
        else:
            next_pipe = ' ' # treat the out of borders same as empty spaces
            
    elif current_dir == 'd':
        next_y = current_y + 1
        if 0 <= next_y < len(pipes):
            next_pipe = pipes[next_y][current_x]
        else:
            next_pipe = ' ' # treat the out of borders same as empty spaces            

    elif current_dir == 'l':
        next_x = current_x - 1
        if 0 <= next_x < len(pipes[0]):
            next_pipe = pipes[current_y][next_x]
        else:
            next_pipe = ' ' # treat the out of borders same as empty spaces    
    
    else: # dir r
        next_x = current_x + 1
        if 0 <= next_x < len(pipes[0]):
            next_pipe = pipes[current_y][next_x]
        else:
            next_pipe = ' ' # treat the out of borders same as empty spaces    

    return next_x, next_y, next_pipe

def attempt_to_turn(current_x, current_y, new_dir1, new_dir2, pipes):
    # turn, assuming the + doesn't weirdly touch multiple pipes rather than connect just 2
    next_dir = new_dir1
    next_x, next_y, next_pipe = check_next_pipe(current_x, current_y, next_dir, pipes)
    if next_pipe != ' ':
        return next_x, next_y, next_dir
    
    next_dir = new_dir2
    next_x, next_y, next_pipe = check_next_pipe(current_x, current_y, next_dir, pipes)
    if next_pipe != ' ':
        return next_x, next_y, next_dir
    
    return -1, -1, 'done'


def move_to_next_pipe(current_x, current_y, current_dir, pipes):

    current_pipe = pipes[current_y][current_x]
    next_dir = current_dir

    next_x, next_y, next_pipe = check_next_pipe(current_x, current_y, current_dir, pipes)

    if next_pipe != ' ':
        return next_x, next_y, next_dir

    if current_pipe != '+':
        return -1, -1, 'done'
    
    # the + case, trying to turn
    else:
        if current_dir in ['d', 'u']:
            return attempt_to_turn(current_x, current_y, 'l', 'r', pipes)

        elif current_dir in ['l', 'r']:
            return attempt_to_turn(current_x, current_y, 'u', 'd', pipes)

# function to go through all the pipes until we can't
def be_mario(current_x, current_y, current_dir, pipes):

    # wtf thought Mario was collecting coins; guess Odyssey depleted his finances
    letters_collected = []
    steps_taken = [(current_y, current_x)]

    while True:
        current_x, current_y, current_dir = move_to_next_pipe(current_x, current_y, current_dir, pipes)
        current_pipe = pipes[current_y][current_x]
        # print(current_pipe)
        if current_dir == 'done':
            break
        elif current_pipe.isalpha():
            # add letter
            letters_collected.append(current_pipe)

        # only increase num steps if we're still traveling (i.e. not done)
        steps_taken.append((current_y, current_x))

    return letters_collected, steps_taken

# =============== TEST CASES ====================
test_pipes = [
'     |          ',
'     |  +--+    ',
'     A  |  C    ',
' F---|----E|--+ ',
'     |  |  |  D ',
'     +B-+  +--+ '
]

x_first = -1
y_first = 0
direction = 'd'
list_pipes = []

for pipe in test_pipes:
    if x_first == -1:
        x_first = pipe.find('|')

    list_pipes.append(list(pipe))

letters_collected, steps_taken = be_mario(x_first, y_first, direction, list_pipes)
assert ''.join(letters_collected) == 'ABCDEF'
assert len(steps_taken) == 38

# =============== PART 1 & 2 ====================
list_pipes = []
x_first = -1
y_first = 0
direction = 'd'

with open('./2017/inputs/d19.txt') as f:
    for row in f:
        if x_first == -1:
            x_first = row.find('|')

        list_pipes.append(list(row.replace('\n','')))

letters_collected, steps_taken = be_mario(x_first, y_first, direction, list_pipes)

print('Part 1 solution:', ''.join(letters_collected))
print('Part 2 solution:', len(steps_taken))


draw_pipes = np.zeros((len(list_pipes), len(list_pipes[0])))

for (x, y) in steps_taken:
    draw_pipes[x, y] = 1

plt.figure(figsize=(8, 8))
sns.heatmap(draw_pipes,  cmap='Purples', square=True, cbar=False)
plt.axis('off')
plt.title('Mario is Jealous!')
# plt.show()
plt.savefig(f'./2017/img/pipes_map_d19.png', bbox_inches='tight', pad_inches=0.1)