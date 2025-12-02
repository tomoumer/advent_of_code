# Day 1 of 2025
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def setup_dial(length=100, center=50):
    dq = deque([i for i in range(length)])
    dq.rotate(center)

    return dq

def rotate_and_check(rotations, dial):

    count_zero = 0
    count_pass_zero = 0

    for rotation in rotations:
        
        direction = rotation[0]
        value = int(rotation[1:])
        current_dial = dial[0]

        if direction == 'R':
            dir = -1
            next_zero = 100 - current_dial

        else:
            dir = 1
            next_zero = current_dial
            # adjust if we're already on 0
            if next_zero == 0:
                next_zero = 100

        # have to have enough moves
        if (value - next_zero) >= 0:
            count_pass_zero += (value - next_zero) // 100 + 1

        # for part 1, just rotate
        dial.rotate(dir * value)

        if dial[0] == 0:
            count_zero += 1

    return count_zero, count_pass_zero    


# =============== TEST CASES ====================
test_input = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

test_input = test_input.strip().split('\n')

dial_lock = setup_dial()
num_zero, num_pass_zero = rotate_and_check(test_input, dial_lock)
assert (num_zero, num_pass_zero) == (3, 6)

# =============== PART 1 & 2 ====================
puzzle_input = []
dial_lock = setup_dial()

with open('./2025/inputs/d1.txt') as f:
    for row in f:
        puzzle_input.append(row.strip())

# print('input rows', len(puzzle_input))

num_zero, num_pass_zero = rotate_and_check(puzzle_input, dial_lock)

print('Part 1 solution:', num_zero)
print('Part 2 solution:', num_pass_zero)