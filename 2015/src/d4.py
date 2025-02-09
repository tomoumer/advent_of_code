# Day 4 of 2015

import hashlib

def get_md5_hex(string):

    encoded_string = string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    hex_digest = md5_hash.hexdigest()

    return hex_digest

def find_lowest_positive(string, num_zeros=5):
    i = 1
    while True:
        hex_digest = get_md5_hex(string + str(i))
        if (num_zeros == 5) & (hex_digest[:5] == '00000'):
            break
        if (num_zeros == 6) & (hex_digest[:6] == '000000'):
            break
        else:
            i += 1

    return i

puzzle_input = []

with open('./2015/inputs/d4.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

# ================= PART 1 ======================
test_cases = {'abcdef': 609043,
              'pqrstuv': 1048970}

for key, lowest_int in test_cases.items():
    assert find_lowest_positive(key) == lowest_int, f"the {key} did not match {lowest_int}"


print('Part 1 solution:', find_lowest_positive(puzzle_input[0]))

# ================= PART 2 ======================

print('Part 2 solution:', find_lowest_positive(puzzle_input[0], num_zeros=6))