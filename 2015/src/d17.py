# Day 17 of 2015
from itertools import combinations

# =========== CLASSES AND FUNCTIONS =============
def fill_up_eggnog(containers, required_fill):
    possible_combos = []
    for num_containers in range(1, len(containers) + 1):
        for chosen_containers in combinations(containers, num_containers):
            
            if sum(chosen_containers) == required_fill:
                possible_combos.append(chosen_containers)

    return possible_combos

def less_containers(possible_combos):

    num_containers = [len(x) for x in possible_combos]
    economic_combos = [x for x in possible_combos if len(x) == min(num_containers)]

    return economic_combos

# =============== TEST CASES ====================
test_containers = [20, 15, 10, 5, 5]
test_fill = 25

test_combos = [[15, 10], [20,5], [20,5], [15,5,5]]

possible_combos = fill_up_eggnog(test_containers, test_fill)
assert possible_combos.sort() == test_combos.sort()

economic_combos = less_containers(possible_combos)
assert len(economic_combos) == 3


# =============== PART 1 & 2 ====================
containers = []

with open('./2015/inputs/d17.txt') as f:
    for row in f:
        containers.append(int(row))

fill = 150
possible_combos = fill_up_eggnog(containers, 150)
economic_combos = less_containers(possible_combos)

print('Part 1 solution:', len(possible_combos))
print('Part 2 solution:', len(economic_combos))