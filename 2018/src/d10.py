# Day 10 of 2018
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========== CLASSES AND FUNCTIONS =============
def create_starting_sky(points):
    min_x = 9999
    min_y = 9999
    max_x = 0
    max_y = 0

    stars_pos = []
    start_vel = []

    for point in points:
        pos_x, pos_y, vel_x, vel_y = list(map(int, re.findall('-?\d+', point)))

        min_x = min(pos_x, min_x)
        min_y = min(pos_y, min_y)
        max_x = max(pos_x, max_x)
        max_y = max(pos_y, max_y)

        stars_pos.append([pos_y, pos_x])
        start_vel.append([vel_y, vel_x])

    # shift so that all of the position values are positive
    stars_pos = np.array(stars_pos) + np.array([np.abs(min_y), np.abs(min_x)])
    max_x = max_x - min_x
    max_y = max_y - min_y
    start_vel = np.array(start_vel)

    star_sky = np.zeros((max_y + 1, max_x + 1))
    for star in stars_pos:
        star_sky[star[0], star[1]] = 1
        
    return stars_pos, start_vel, star_sky

def find_message(stars_pos, start_vel, star_sky):
    # hypothesis: the message is going to be the most compact
    # i.e. the differences between min x and max x, as well as min y and max y
    # are going to be the smallest (think entrophy)
    min_coords = np.min(stars_pos, axis=0)
    max_coords = np.max(stars_pos, axis=0)

    prev_extent_coords = min_coords - max_coords

    for i in range(100000):

        stars_pos += start_vel

        min_coords = np.min(stars_pos, axis=0)
        max_coords = np.max(stars_pos, axis=0)

        new_extent_coords = min_coords - max_coords

        if (np.abs(new_extent_coords[0]) <= np.abs(prev_extent_coords[0])) \
            and (np.abs(new_extent_coords[1]) <= np.abs(prev_extent_coords[1])):

            prev_extent_coords = new_extent_coords
            continue

        else:
            # reverse one step, we went too far
            stars_pos -= start_vel

            new_sky = np.zeros((len(star_sky), len(star_sky[0])))

            for star in stars_pos:
                new_sky[star[0], star[1]] = 1
            break
    
    # to show just the message part
    # i is the wait time
    return new_sky[min_coords[0]:max_coords[0], min_coords[1]:max_coords[1]], i


# =============== TEST CASES ====================
points = ['position=< 9,  1> velocity=< 0,  2>',
'position=< 7,  0> velocity=<-1,  0>',
'position=< 3, -2> velocity=<-1,  1>',
'position=< 6, 10> velocity=<-2, -1>',
'position=< 2, -4> velocity=< 2,  2>',
'position=<-6, 10> velocity=< 2, -2>',
'position=< 1,  8> velocity=< 1, -1>',
'position=< 1,  7> velocity=< 1,  0>',
'position=<-3, 11> velocity=< 1, -2>',
'position=< 7,  6> velocity=<-1, -1>',
'position=<-2,  3> velocity=< 1,  0>',
'position=<-4,  3> velocity=< 2,  0>',
'position=<10, -3> velocity=<-1,  1>',
'position=< 5, 11> velocity=< 1, -2>',
'position=< 4,  7> velocity=< 0, -1>',
'position=< 8, -2> velocity=< 0,  1>',
'position=<15,  0> velocity=<-2,  0>',
'position=< 1,  6> velocity=< 1,  0>',
'position=< 8,  9> velocity=< 0, -1>',
'position=< 3,  3> velocity=<-1,  1>',
'position=< 0,  5> velocity=< 0, -1>',
'position=<-2,  2> velocity=< 2,  0>',
'position=< 5, -2> velocity=< 1,  2>',
'position=< 1,  4> velocity=< 2,  1>',
'position=<-2,  7> velocity=< 2, -2>',
'position=< 3,  6> velocity=<-1, -1>',
'position=< 5,  0> velocity=< 1,  0>',
'position=<-6,  0> velocity=< 2,  0>',
'position=< 5,  9> velocity=< 1, -2>',
'position=<14,  7> velocity=<-2,  0>',
'position=<-3,  6> velocity=< 2, -1>']

stars_pos, start_vel, star_sky = create_starting_sky(points)
star_sky, wait_time = find_message(stars_pos, start_vel, star_sky)

# plt.figure(figsize=(8, 8))
# sns.heatmap(star_sky,  cmap='viridis', square=True, cbar=False)
# plt.axis('off')
# plt.title('THE MESSAGE!')
# plt.show()

# =============== PART 1 & 2 ====================
points = []

with open('./2018/inputs/d10.txt') as f:
    for row in f:
        points.append(row.strip())

stars_pos, start_vel, star_sky = create_starting_sky(points)

star_sky, wait_time = find_message(stars_pos, start_vel, star_sky)

plt.figure(figsize=(8, 8))
sns.heatmap(star_sky,  cmap='cividis', square=True, cbar=False)
plt.axis('off')
plt.title('THE MESSAGE!')
# plt.show()
plt.savefig(f'./2018/img/the_message_d10.png', bbox_inches='tight', pad_inches=0.1)


# part 1 is the plot
# print('Part 1 solution:')
print('Part 2 solution:', wait_time)