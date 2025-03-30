# Day 14 of 2017
from collections import deque
import functools
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
# the know algo from day 10
def knot_the_knot_the_ascii_hashing_wtf(my_list, ascii_lengths):

    ascii_suffix = [17, 31, 73, 47, 23]
    total_rotation = 0
    skip_size = 0

    lengths = []
    for ascify in ascii_lengths:
        lengths.append(ord(ascify))
    lengths = lengths + ascii_suffix

    for i in range(64):
        # print('loop i', i)

        for length in lengths:
            if length < len(my_list):
                my_list = deque(list(my_list)[0:length][::-1] + list(my_list)[length:])
            
            # reverse the whole thing
            else:
                my_list.reverse()

            rotate_by = length + skip_size
            my_list.rotate(-rotate_by)

            total_rotation += rotate_by
            skip_size += 1

        # ascii_lengths = ','.join(map(str, lengths))

    # rotate it back to the original position
    total_rotation = total_rotation % len(my_list)
    my_list.rotate(total_rotation)

    return my_list

def densify(my_list):
    # still a deque at this point
    my_list = list(my_list)
    final_hex = ''

    for i in range(16):
        # chunk the list in 16 parts
        sublist = my_list[i*16: (i+1)*16]
        # bitwise xor the list
        new_num = functools.reduce(lambda x, y: x ^ y, sublist)
        # turn to hex and remove the leading 0x
        final_hex = final_hex + hex(new_num)[2:].zfill(2)

    return final_hex


def create_grid(hash_key):
    final_grid = []

    for j in range(128):
        my_list = deque([i for i in range(256)])
        my_list = knot_the_knot_the_ascii_hashing_wtf(my_list, f'{hash_key}-{j}')
        hex_value = densify(my_list)

        final_bin = ''
        for hex_part in hex_value:
            decimal_value = int(hex_part, 16)
            final_bin = final_bin + bin(decimal_value)[2:].zfill(4)

        final_grid.append([int(bin) for bin in final_bin])

    return np.array(final_grid)


def find_regions(grid):
    ones = np.argwhere(grid == 1)

    # to flag the ones that have been groupped already
    grouped = []
    group_nr = 0

    for [x, y] in ones:
        # print(x,y)
        if [x,y] in grouped:
            continue
        
        follow_group = deque([[x,y]])
        group_nr += 1
        
        # this is the part that checks how far the group extends
        while follow_group:

            [x,y] = follow_group.popleft()

            if [x,y] in grouped:
                continue

            grouped.append([x,y])

            if x < grid.shape[0] -1:
                if grid[x+1, y] == 1:
                    # note this next line is not needed, just for drawing later
                    grid[x+1, y] = group_nr
                    follow_group.append([x+1, y])
            if x > 0:
                if grid[x-1, y] == 1:
                    grid[x-1, y] = group_nr
                    follow_group.append([x-1, y])
            
            if y < grid.shape[1] -1:
                if grid[x, y+1] == 1:
                    grid[x, y+1] = group_nr
                    follow_group.append([x, y+1])
            if y > 0:
                if grid[x, y-1] == 1:
                    grid[x, y-1] = group_nr
                    follow_group.append([x, y-1])

    return group_nr, grid


# =============== TEST CASES ====================

test_grid = create_grid('flqrgnkx')
assert np.sum(test_grid) == 8108
group_nr = find_regions(test_grid)[0]
assert group_nr == 1242

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d14.txt') as f:
    for row in f:
        puzzle_key = row.strip()

real_grid = create_grid(puzzle_key)

print('Part 1 solution:', np.sum(real_grid))

group_nr, real_grid = find_regions(real_grid)

print('Part 2 solution:', group_nr)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 8))
sns.heatmap(real_grid,  cmap='viridis', square=True, cbar=False, mask=np.where(real_grid == 0, 1, 0))
plt.axis('off')
plt.title('Disk Fragmentation weeeee!')
# plt.show()
plt.savefig(f'./2017/img/disk_fragmented_d14.png', bbox_inches='tight', pad_inches=0.1)

