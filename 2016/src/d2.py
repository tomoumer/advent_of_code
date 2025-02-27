# Day 2 of 2016

# =========== CLASSES AND FUNCTIONS =============
def make_valid_indices(keypad_version):
    # added this function to handle any keypad config
    idx_version = []
    for i, row in enumerate(keypad_version):
        for j, _ in enumerate(row):
            # skip padding
            if keypad_version[i][j] != '':
                idx_version.append([i,j])

    return idx_version

def move_one(move, current_v, current_h, keypad_idx):


    match move:
        case 'U':
            if [current_v -1, current_h] in keypad_idx:
                current_v -= 1
        case 'D':
            if [current_v +1, current_h] in keypad_idx:
                current_v += 1
        case 'L':
            if [current_v, current_h -1] in keypad_idx:
                current_h -= 1
        case 'R':
            if [current_v, current_h +1] in keypad_idx:
                current_h += 1
        case _:
            raise('unknown move!')
    
    return current_v, current_h


def follow_directions(directions, keypad_version):

    code = ''
    if len(keypad_version) == 3: #original
        current_v = 1
        current_h = 1
    # start position changes
    else:
        current_v = 2
        current_h = 0

    keypad_idx = make_valid_indices(keypad_version)

    # print('start', current_v, current_h)
    # each line in directions produces a final digit
    for line in directions:
        for move in line:
            current_v, current_h = move_one(move, current_v, current_h, keypad_idx)
            # print('move', move, current_v, current_h)

        # at end of processing line
        code = code + keypad_version[current_v][current_h]

    return code


keypad = """
1 2 3
4 5 6
7 8 9
"""

keypad = [x.split(' ') for x in keypad.strip().split('\n')]
# with keypad, vertical is first, then horizontal
# also the vertical movement is inverted based on how I constructed the list
valid_key_idx = make_valid_indices(keypad)

actual_keypad = """
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""

# need to strip to get rid of empty commands
actual_keypad = [x.strip().split(' ') for x in actual_keypad.strip().split('\n')]

for line in actual_keypad:
    padding = [''] * ((5-len(line)) // 2)
    if len(line) < 5:
        line[:0] = padding
        line.extend(padding)

valid_actual_idx = make_valid_indices(keypad)


# =============== TEST CASES ====================
test_directions = """ULL
RRDDD
LURDL
UUUUD"""

test_directions = test_directions.split('\n')

# assert follow_directions(test_directions, keypad) == '1985'

assert follow_directions(test_directions, actual_keypad) == '5DB3'


# ================= PART 1 ======================
directions = []

with open('./2016/inputs/d2.txt') as f:
    for row in f:
        directions.append(row.strip())


code = follow_directions(directions, keypad) 
print('Part 1 solution:', code)

# ================= PART 2 ======================
code_new = follow_directions(directions, actual_keypad) 
print('Part 2 solution:', code_new)