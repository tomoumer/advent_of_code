# Day 2 of 2018
from itertools import groupby

# =========== CLASSES AND FUNCTIONS =============
def count_letters_on_box(box_ids):
    num_double = 0
    num_triple = 0

    for box_id in box_ids:
        # this is so that I only count multiple doubles in same id once
        has_double = False
        has_triple = False

        # print(box_id)
        for k, g in groupby(sorted(box_id)):
            # print(k, list(g))
            len_group = len(list(g))


            if len_group == 2:
                has_double = True
            elif len_group == 3:
                has_triple = True

        num_double += has_double
        num_triple += has_triple

    # print(num_double, num_triple)
    return num_double * num_triple

def find_correct_box_ids(box_ids):

    different_idx_letter = -1

    # this could also be done using combinations ..
    for i, box_id in enumerate(box_ids):
        for box_id2 in box_ids[i+1:]:

            for j in range(len(box_id)):

                if box_id[j] != box_id2[j]:
                    # if there's already one letter different
                    if different_idx_letter != -1:
                        different_idx_letter = -1
                        break
                    else:
                        different_idx_letter = j

            if different_idx_letter != -1:
                break
        if different_idx_letter != -1:
            break
    
    return box_id[:different_idx_letter] + box_id[different_idx_letter+1:]


# =============== TEST CASES ====================
box_ids = ['abcdef',
'bababc',
'abbcde',
'abcccd',
'aabcdd', 
'abcdee',
'ababab']

assert count_letters_on_box(box_ids) == 12

box_ids = ['abcde',
'fghij',
'klmno',
'pqrst',
'fguij',
'axcye',
'wvxyz']

assert find_correct_box_ids(box_ids) == 'fgij'


# =============== PART 1 & 2 ====================
box_ids = []

with open('./2018/inputs/d2.txt') as f:
    for row in f:
        box_ids.append(row.strip())


checksum = count_letters_on_box(box_ids)
correct_boxids = find_correct_box_ids(box_ids)

print('Part 1 solution:', checksum)
print('Part 2 solution:', correct_boxids)