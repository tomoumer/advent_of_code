# Day 17 of 2017
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
# note because of how I'm rotating it, the last value is the newly inserted
# and the first value is the previous nr
def crazy_rotate_buffer(step_nr, test_only=True):

    cir_buffer = deque([0])

    for i in range(1, 50000000):
        cir_buffer.rotate(-step_nr)
        cir_buffer.append(i)

        if i == 2017:
            val_after_2017 = cir_buffer[0]
            if test_only:
                break

    zero_index = cir_buffer.index(0)

    return val_after_2017, cir_buffer[zero_index+1]

# =============== TEST CASES ====================
val_after_2017, _ = crazy_rotate_buffer(step_nr=3)

assert val_after_2017 == 638

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d17.txt') as f:
    for row in f:
        step_nr = int(row)

val_after_2017, val_after_zero = crazy_rotate_buffer(step_nr=step_nr, test_only=False)

print('Part 1 solution:', val_after_2017)
print('Part 2 solution:', val_after_zero)