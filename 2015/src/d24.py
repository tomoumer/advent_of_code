# Day 24 of 2015
from itertools import combinations
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def find_group(pkgs, group_weight):
    found_combo = False

    for i in range(1, len(pkgs)):
        for combo in combinations(pkgs, i):
            if sum(combo) == group_weight:
                found_combo = True
                break

        if found_combo:
            break

    remaining_pkgs = [pkg for pkg in pkgs if pkg not in combo]
    return combo, remaining_pkgs

def make_three_groups(pkgs, group_weight):

    group_1, remaining_pkgs = find_group(pkgs, group_weight)
    group_2, group_3 = find_group(remaining_pkgs, group_weight)

    qe = np.prod(group_1)

    if len(group_1) == len(group_2):
        qe = min(qe, np.prod(group_2))
    if len(group_1) == len(group_3):
        qe = min(qe, np.prod(group_3))

    return qe

def make_four_groups(pkgs, group_weight):

    group_1, remaining_pkgs = find_group(pkgs, group_weight)
    group_2, remaining_pkgs = find_group(remaining_pkgs, group_weight)
    group_3, group_4 = find_group(remaining_pkgs, group_weight)

    qe = np.prod(group_1)

    if len(group_1) == len(group_2):
        qe = min(qe, np.prod(group_2))
    if len(group_1) == len(group_3):
        qe = min(qe, np.prod(group_3))
    if len(group_1) == len(group_4):
        qe = min(qe, np.prod(group_4))

    return qe

# =============== TEST CASES ====================
test_pkgs = list(range(1,6)) + list(range(7,12))
# needs to be even
test_group_weight = sum(test_pkgs) / 3
assert make_three_groups(test_pkgs, test_group_weight) == 99

# part 2
test_group_weight = sum(test_pkgs) / 4
assert make_four_groups(test_pkgs, test_group_weight) == 44


# ================= PART 1 ======================
packages = []

with open('./2015/inputs/d24.txt') as f:
    for row in f:
        packages.append(int(row.strip()))

group_weight = sum(packages) / 3
qe = make_three_groups(packages, group_weight)

print('Part 1 solution:', qe)

# ================= PART 2 ======================

group_weight = sum(packages) / 4
qe = make_four_groups(packages, group_weight)


print('Part 2 solution:', qe)