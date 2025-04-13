# Day 2 of 2017
from itertools import combinations

# =========== CLASSES AND FUNCTIONS =============
def row_checksum(row):

    row_values = list(map(int, row.split()))
    min_val = min(row_values)
    max_val = max(row_values)

    # part 2
    pairs = list(combinations(row_values, 2))

    for pair in pairs:

        if max(pair) % min(pair) == 0:
            break

    return (max_val - min_val), int(max(pair) / min(pair))

# =============== TEST CASES ====================
test_spreadsheet = {
    '5 1 9 5': 8,
    '7 5 3': 4 ,
    '2 4 6 8': 6}

for row, test_chk in test_spreadsheet.items():
    assert row_checksum(row)[0] == test_chk

test_spreadsheet = {
    '5 9 2 8': 4,
    '9 4 7 3': 3,
    '3 8 6 5': 2
}

for row, test_chk in test_spreadsheet.items():
    assert row_checksum(row)[1] == test_chk

# =============== PART 1 & 2 ====================
checksum_1 = 0
checksum_2 = 0

with open('./2017/inputs/d2.txt') as f:
    for row in f:
        chk1, chk2 = row_checksum(row)
        checksum_1 += chk1
        checksum_2 += chk2

print('Part 1 solution:', checksum_1)
print('Part 2 solution:', checksum_2)