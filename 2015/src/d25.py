# Day 25 of 2015
import re


def find_successive_number(row, col):

    nr_in_succession = sum(range(1,col+1)) + sum(range(col, col+row-1))
    return nr_in_succession

def calculate_next(current_nr):

    next_nr = (current_nr * 252533) % 33554393
    return next_nr

# # load in the actual puzzle input

with open('./2015/inputs/d25.txt') as f:
    for j, row in enumerate(f):
        print(row.strip())
        row_nr, col_nr = re.findall('\d+', row)


# ================= PART 1 ======================

assert find_successive_number(5,2) == 17
assert find_successive_number(3,3) == 13
assert find_successive_number(1,4) == 10
assert find_successive_number(2,5) == 20

nr_in_succession = find_successive_number(int(row_nr), int(col_nr))

current_nr = 20151125

for i in range(nr_in_succession-1):

    next_nr = calculate_next(current_nr)
    current_nr = next_nr


print('Part 1 solution:', current_nr)

# ================= PART 2 ======================
# hah theres no part 2, just needed 49 stars. DID IT REDDIT!

print('Part 2 solution:')