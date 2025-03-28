# Day 10 of 2017
from collections import deque
import functools

# =========== CLASSES AND FUNCTIONS =============
def knot_hashing(my_list, lengths):

    # instead of marking the position, I'll be rotating
    # so I need to keep track how to get back to the origin (reverse of the rotation)
    total_rotation = 0
    skip_size = 0

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

    # rotate it back to the original position
    total_rotation = total_rotation % len(my_list)
    my_list.rotate(total_rotation)

    return my_list

# part 2
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
        print(hex(new_num))
        final_hex = final_hex + hex(new_num)[2:].zfill(2)

    return final_hex


# =============== TEST CASES ====================
test_list = deque([0, 1, 2, 3, 4])
test_lengths = [3, 4, 1, 5]

test_list = knot_hashing(test_list, test_lengths)
assert test_list.popleft() * test_list.popleft() == 12

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d10.txt') as f:
    for row in f:
        input_lengths = list(map(int, row.split(',')))
        ascii_lengths = row.strip()

my_list = deque([i for i in range(256)])
my_list = knot_hashing(my_list, input_lengths)
first_two_prod = my_list.popleft() * my_list.popleft()


my_list = deque([i for i in range(256)])
my_list = knot_the_knot_the_ascii_hashing_wtf(my_list, ascii_lengths)

final_hex = densify(my_list)

print('Part 1 solution:', first_two_prod)
print('Part 2 solution:', final_hex)