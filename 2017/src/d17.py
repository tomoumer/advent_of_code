# Day 17 of 2017
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def rotate_buffer(step_nr):

    cir_buffer = deque([0])

    for i in range(1, 2018):
        cir_buffer.rotate(-step_nr)
        cir_buffer.append(i)

    return cir_buffer

def crazy_rotate_buffer(step_nr):

    cir_buffer = deque([0])

    for i in range(1, 50000000):
        cir_buffer.rotate(-step_nr)
        cir_buffer.append(i)

    zero_index = cir_buffer.index(0)

    return cir_buffer[zero_index+1]


# =============== TEST CASES ====================
cir_buffer = rotate_buffer(step_nr=3)

# note because of how I'm rotating it, the last value is the newly inserted
# and the first value is the previous nr
assert cir_buffer[0] == 638

# =============== PART 1 & 2 ====================


with open('./2017/inputs/d17.txt') as f:
    for row in f:
        step_nr = int(row)

cir_buffer = rotate_buffer(step_nr=step_nr)
val_after_zero = crazy_rotate_buffer(step_nr=step_nr)

print('Part 1 solution:',cir_buffer[0])
print('Part 2 solution:', val_after_zero)