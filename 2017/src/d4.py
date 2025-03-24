# Day 4 of 2017
from collections import Counter

# =========== CLASSES AND FUNCTIONS =============
def check_valid_pass(pass_candidate):

    pass_candidate = pass_candidate.split()

    if len(pass_candidate) != len(set(pass_candidate)):
        part_1 = False
    
    else:
        part_1 = True

    
    pass_candidate = [Counter(x) for x in pass_candidate]
    part_2 = True
    while pass_candidate:
        tmp_counter = pass_candidate.pop(0)
        if tmp_counter in pass_candidate:
            part_2 = False
            break

    return part_1, part_2
 

# =============== TEST CASES ====================
test_passes = {'aa bb cc dd ee': True,
'aa bb cc dd aa': False,
'aa bb cc dd aaa': True}

for test_pass, is_valid in test_passes.items():
    assert check_valid_pass(test_pass)[0] == is_valid

test_passes = {'abcde fghij' : True,
'abcde xyz ecdab': False,
'a ab abc abd abf abj': True,
'iiii oiii ooii oooi oooo':True,
'oiii ioii iioi iiio': False}

for test_pass, is_valid in test_passes.items():
    assert check_valid_pass(test_pass)[1] == is_valid


# =============== PART 1 & 2 ====================
num_valid_1 = 0
num_valid_2 = 0

with open('./2017/inputs/d4.txt') as f:
    for row in f:
        valid1, valid2 = check_valid_pass(row)
        num_valid_1 += valid1
        num_valid_2 += valid2


print('Part 1 solution:', num_valid_1)
print('Part 2 solution:', num_valid_2)