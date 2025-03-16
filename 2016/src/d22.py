# Day 22 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
def find_viable_pairs(storage_grid, max_x, max_y):

    checked_pairs = dict()

    for x_a in range(max_x + 1):
        for y_a in range(max_y + 1):
            for x_b in range(max_x + 1):
                for y_b in range(max_y + 1):

                    # no same points
                    if (x_a == x_b) and (y_a == y_b):
                        continue

                    # make sure I haven't already checked the pair
                    pair = tuple(sorted([(x_a, y_a), (x_b, y_b)]))
                    if pair in checked_pairs.keys():
                        continue

                    # has to have some data
                    if (storage_grid[(x_a),(y_a)]['used'] > 0) and (storage_grid[(x_a),(y_a)]['used'] <= storage_grid[(x_b),(y_b)]['avail']):
                        checked_pairs[pair] = 1
                    # check if the pair works in other direction
                    elif (storage_grid[(x_b),(y_b)]['used'] > 0) and (storage_grid[(x_b),(y_b)]['used'] <= storage_grid[(x_a),(y_a)]['avail']):
                        checked_pairs[pair] = 1
                    
                    else:
                        checked_pairs[pair] = 0

    num_viable = 0
    for val in checked_pairs.values():
        num_viable += val

    return num_viable


# ================= PART 1 ======================
storage_grid = dict()
max_x = 0
max_y = 0

with open('./2016/inputs/d22.txt') as f:
    for i, row in enumerate(f):
        if i <= 1:
            print(row.strip())
        else:
            # they are listed in incrementing y and then x once at end of row
            filesystem, size, used, avail, use_pct = row.strip().split()
            size = int(size.replace('T', ''))
            used = int(used.replace('T', ''))
            avail = int(avail.replace('T', ''))
            use_pct = int(use_pct.replace('%', ''))

            cluster = {'size': size, 'used': used, 'avail': avail, 'use_pct': use_pct}
            x = int(re.search('x(\d+)',filesystem).group(1))
            y = int(re.search('y(\d+)',filesystem).group(1))

            max_x = max(x, max_x)
            max_y = max(y, max_y)

            storage_grid[(x, y)] = cluster


num_viable = find_viable_pairs(storage_grid, max_x, max_y)

# 952
print('Part 1 solution:', num_viable)

# # ================= PART 2 ======================

storage_grid_img = ''
# start by finding the empty disk - there's only one
for y_a in range(max_y + 1):
    for x_a in range(max_x + 1):
        if storage_grid[(x_a),(y_a)]['size'] > 100:
            storage_grid_img = storage_grid_img + '# '
        elif storage_grid[(x_a),(y_a)]['used'] == 0:
            empty_cluster = [x_a, y_a]
            storage_grid_img = storage_grid_img + '_ '
        elif (x_a == 0) and (y_a == 0):
            storage_grid_img = storage_grid_img + 'X '
        elif (x_a == max_x) and (y_a == 0):
            storage_grid_img = storage_grid_img + 'G '
        else:
            # print(f"{storage_grid[(x_a),(y_a)]['used']}/{storage_grid[(x_a),(y_a)]['avail']}", end=' ')
            storage_grid_img = storage_grid_img + '. '

    storage_grid_img = storage_grid_img + '\n'

print('')
print(storage_grid_img)

# as ilustrated in the example, the disk is going to have to be moved around
total_moves = 0
# first to avoid the enormous disks
total_moves += 2
empty_cluster[0] -= 2
# next get all the way to the top row (the y=0)
total_moves += empty_cluster[1]
# then go the corner
total_moves += (max_x - empty_cluster[0])
# and then, each time we attempt to shift the data from y to y-1, the empty disk needs to "travel" around, so 5 moves
total_moves += (max_x -1) * 5

print('Part 2 solution:', total_moves)