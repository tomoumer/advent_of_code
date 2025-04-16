# Day 5 of 2018
from itertools import pairwise
# =========== CLASSES AND FUNCTIONS =============
def polymer_reaction(polymer):

    reacted = True
    
    while reacted:
        reacted = False
        # doing it a different way instead of zip!
        # instead of breaking and redoing, it would be better to flag the i-s
        # and then just skip one where there's 3 in a row
        for i, (l1, l2) in enumerate(pairwise(polymer)):
            if (l1 != l2) and (l1.lower() == l2.lower()):
                reacted = True
                break
        
        if reacted:
            polymer = polymer[:i] + polymer[i+2:]

    return polymer

def polymer_advanced_reaction(polymer):

    shortest_len = 1000000
    for remove_letter in set(polymer.lower()):
        polymer_pt2 = polymer_reaction(polymer.replace(remove_letter, '').replace(remove_letter.upper(), ''))
        shortest_len = min(shortest_len, len(polymer_pt2))

    return shortest_len


# =============== TEST CASES ====================
polymer = 'dabAcCaCBAcCcaDA'

polymer_pt1 = polymer_reaction(polymer)

assert len(polymer_pt1) == 10

shortest_len = polymer_advanced_reaction(polymer)
assert shortest_len == 4


# =============== PART 1 & 2 ====================

with open('./2018/inputs/d5.txt') as f:
    for row in f:
        polymer = row.strip()


polymer_pt1 = polymer_reaction(polymer)
shortest_len = polymer_advanced_reaction(polymer)


print('Part 1 solution:', len(polymer_pt1))
print('Part 2 solution:', shortest_len)