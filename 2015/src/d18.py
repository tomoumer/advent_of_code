# Day 18 of 2015
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

# NOTE running this one takes a while because it creates a giff!

def check_neighbors(pos_x, pos_y, lights_config):

    neighbors_on = 0
    neighbors = {(x, y) for x in [pos_x-1, pos_x, pos_x+1] for y in [pos_y-1, pos_y, pos_y+1] 
                 if ((x,y) != (pos_x,pos_y))
                    and (x >= 0)
                    and (y >= 0)
                    and (x < lights_config.shape[0]) 
                    and (y < lights_config.shape[1])}
    
    for neighbor in neighbors:
        neighbors_on += lights_config[neighbor]

    return neighbors_on



# Oh hey it's the Conway's game of life!
def update_lights(lights_config, broken_corners=False):

    new_lights_config = lights_config.copy()

    for i in range(lights_config.shape[0]):
        for j in range(lights_config.shape[0]):

            neighbors_on = check_neighbors(i,j, lights_config)

            if (lights_config[i,j] == 0) and (neighbors_on == 3):
                new_lights_config[i,j] = 1
            elif (lights_config[i,j] == 1) and ((neighbors_on == 2) or (neighbors_on == 3)):
                new_lights_config[i,j] = 1
            else:
                new_lights_config[i,j] = 0

    if broken_corners:
        new_lights_config[0,0] = 1
        new_lights_config[0, lights_config.shape[0]-1] = 1
        new_lights_config[lights_config.shape[0]-1, 0] = 1
        new_lights_config[lights_config.shape[0]-1, lights_config.shape[0]-1] = 1

    return new_lights_config

def save_light_img(lights_config, n):
    plt.figure(figsize=(8, 8))
    plt.imshow(lights_config, cmap='copper', aspect='equal') 
    plt.axis('off')
    plt.title('BEST Game of LightShow')
    plt.savefig(f'./2015/img/lights_step{str(n).zfill(3)}_d18.png', bbox_inches='tight', pad_inches=0)
    plt.close()

def make_light_giff(giff_name):
    images = []
    all_images = os.listdir('./2015/img/')
    all_images = sorted(all_images)
    for filename in all_images:
        if filename.endswith('d18.png'):
            images.append(imageio.v3.imread('./2015/img/' + filename))
            os.remove('./2015/img/' + filename)
            imageio.mimsave(f'./2015/img/{giff_name}_d18.gif', images, format='GIF', duration=500) # duration in ms



# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d18.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append([1 if x =='#' else 0 for x in row.strip()])

lights_config = np.array(puzzle_input)

print('lights shape', lights_config.shape)


test_input_start = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

test_input_steps = []

test_input_steps.append("""..##..
..##.#
...##.
......
#.....
#.##..""")

test_input_steps.append("""..###.
......
..###.
......
.#....
.#....""")

test_input_steps.append("""...#..
......
...#..
..##..
......
......""")

test_input_steps.append("""......
......
..##..
..##..
......
......""")

test_lights = []

for row in test_input_start.split('\n'):
    test_lights.append([1 if x =='#' else 0 for x in row.strip()])

test_lights = np.array(test_lights)


for test_input_step in test_input_steps:
    calculated_lights = update_lights(test_lights)
    test_lights = []
    for row in test_input_step.split('\n'):
        test_lights.append([1 if x =='#' else 0 for x in row.strip()])

    test_lights = np.array(test_lights)

    assert (calculated_lights == test_lights).all()

# ================= PART 1 ======================

save_light_img(lights_config, 0)
for i in range(100):
    lights_config = update_lights(lights_config)
    save_light_img(lights_config, i+1)

make_light_giff('original_lightshow')

print('Part 1 solution:', lights_config.sum())

# ================= PART 2 ======================

test_input_start = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

test_lights = []

for row in test_input_start.split('\n'):
    test_lights.append([1 if x =='#' else 0 for x in row.strip()])

test_lights = np.array(test_lights)
test_lights[0,0] = 1
test_lights[0,test_lights.shape[0]-1] = 1
test_lights[test_lights.shape[0]-1, 0] = 1
test_lights[test_lights.shape[0]-1, test_lights.shape[0]-1] = 1

test_input_steps = []
test_input_steps.append("""#.##.#
####.#
...##.
......
#...#.
#.####""")

test_input_steps.append("""#..#.#
#....#
.#.##.
...##.
.#..##
##.###""")

test_input_steps.append("""#...##
####.#
..##.#
......
##....
####.#""")

test_input_steps.append("""#.####
#....#
...#..
.##...
#.....
#.#..#""")

test_input_steps.append("""##.###
.##..#
.##...
.##...
#.#...
##...#""")


for test_input_step in test_input_steps:
    calculated_lights = update_lights(test_lights, broken_corners=True)
    test_lights = []
    for row in test_input_step.split('\n'):
        test_lights.append([1 if x =='#' else 0 for x in row.strip()])

    test_lights = np.array(test_lights)

    assert (calculated_lights == test_lights).all()


puzzle_input = []

with open('./2015/inputs/d18.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append([1 if x =='#' else 0 for x in row.strip()])

lights_config = np.array(puzzle_input)
lights_config[0,0] = 1
lights_config[0,lights_config.shape[0]-1] = 1
lights_config[lights_config.shape[0]-1, 0] = 1
lights_config[lights_config.shape[0]-1, lights_config.shape[0]-1] = 1


save_light_img(lights_config, 0)
for i in range(100):
    lights_config = update_lights(lights_config, broken_corners=True)
    save_light_img(lights_config, i+1)

make_light_giff('broken_lightshow')

print('Part 2 solution:', lights_config.sum())