# Day 5 of 2017

# =========== CLASSES AND FUNCTIONS =============
def trampoline_around(offsets):
    num_steps = 0
    jump_nr = 0

    while True:
        num_steps += 1

        tmp_jump = offsets[jump_nr]
        offsets[jump_nr] += 1
        jump_nr += tmp_jump

        if jump_nr >= len(offsets):
            break
            
    return num_steps

def trampoline_improved(offsets):
    num_steps = 0
    jump_nr = 0

    while True:
        num_steps += 1

        tmp_jump = offsets[jump_nr]
        if offsets[jump_nr] >= 3:
            offsets[jump_nr] -= 1
        else:
            offsets[jump_nr] += 1
        jump_nr += tmp_jump

        if jump_nr >= len(offsets):
            break
            
    return num_steps


# =============== TEST CASES ====================
test_offsets = [0, 3, 0, 1, -3]
assert trampoline_around(test_offsets) == 5

test_offsets = [0, 3, 0, 1, -3]
assert trampoline_improved(test_offsets) == 10

# =============== PART 1 & 2 ====================
offsets = []

with open('./2017/inputs/d5.txt') as f:
    for row in f:
        offsets.append(int(row.strip()))

num_steps1 = trampoline_around(offsets)

print('Part 1 solution:', num_steps1)

offsets = []

with open('./2017/inputs/d5.txt') as f:
    for row in f:
        offsets.append(int(row.strip()))

num_steps2 = trampoline_improved(offsets)

print('Part 2 solution:', num_steps2)