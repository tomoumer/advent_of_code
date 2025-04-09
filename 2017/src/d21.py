# Day 21 of 2017
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def numpify_pattern(pattern):
    grid = []

    for row in pattern.strip().split('/'):
        tmp_row = [0 if i == '.' else 1 for i in row]
        grid.append(tmp_row)

    return np.array(grid)

# OMG THERE IS A ROT90 FUNCTION IN NUMPY???
def process_rules(rules):
    two_by_two = []
    three_by_three = []

    for rule in rules:
        pattern_from, pattern_to = rule.strip().split('=>')

        pattern_from = numpify_pattern(pattern_from)
        pattern_to = numpify_pattern(pattern_to)


        if pattern_from.shape[0] == 2:
            two_by_two.append([pattern_from, pattern_to])
            # do the rotations and save
            for _ in range(3):
                pattern_from = np.rot90(pattern_from)
                two_by_two.append([pattern_from, pattern_to])

        else:
            # for 3x3 also need to flip it, get different patterns
            three_by_three.append([pattern_from, pattern_to])            
            three_by_three.append([np.flipud(pattern_from), pattern_to])
            three_by_three.append([np.fliplr(pattern_from), pattern_to])

            # do the rotations and save
            for _ in range(3):
                pattern_from = np.rot90(pattern_from)
                three_by_three.append([pattern_from, pattern_to])
                three_by_three.append([np.flipud(pattern_from), pattern_to])
                three_by_three.append([np.fliplr(pattern_from), pattern_to])

            # there's going to be duplicates here but whatever!

    return two_by_two, three_by_three

def match_and_process(pattern, two_by_two, three_by_three):

    pattern_len = pattern.shape[0]

    if pattern_len % 2 == 0:
        num_blocks = pattern_len // 2
        transform_type = two_by_two
        s_size = 2
    else:
        num_blocks = pattern_len // 3
        transform_type = three_by_three
        s_size = 3


    new_pattern = np.array([])
    for i in range(num_blocks):
        tmp_row = np.array([])
        for j in range(num_blocks):

            # find the right transformation
            for transform in transform_type:

                # initially I had i and j inverted ...
                if (pattern[i*s_size:(i+1)*s_size, j*s_size:(j+1)*s_size] == transform[0]).all():
                    
                    # print('found match', transform)
                    tmp_row = np.concatenate((tmp_row, transform[1]), axis=1) if tmp_row.size else transform[1]
                    break
                    # print(tmp_row)
    
        new_pattern = np.concatenate((new_pattern, tmp_row), axis=0) if new_pattern.size else tmp_row
    
    return new_pattern


# =============== TEST CASES ====================

start_pattern = '.#./..#/###'

pattern = numpify_pattern(start_pattern)


test_rules = [
    '../.# => ##./#../...',
    '.#./..#/### => #..#/..../..../#..#'
]

two_by_two, three_by_three = process_rules(test_rules)

for _ in range(2):
    pattern = match_and_process(pattern, two_by_two, three_by_three)
    # print(pattern)

assert np.sum(pattern) == 12

# =============== PART 1 & 2 ====================

rules = []

with open('./2017/inputs/d21.txt') as f:
    for row in f:
        rules.append(row.strip())


start_pattern = '.#./..#/###'

pattern = numpify_pattern(start_pattern)
two_by_two, three_by_three = process_rules(rules)


for i in range(18):
    pattern = match_and_process(pattern, two_by_two, three_by_three)
    if i == 4:
        part_1 = np.sum(pattern)


print('Part 1 solution:', part_1)
print('Part 2 solution:', np.sum(pattern))