# Day 17 of 2015

from itertools import combinations

def fill_up_eggnog(containers, required_fill):
    possible_combos = []
    for num_containers in range(1, len(containers) + 1):
        for chosen_containers in combinations(containers, num_containers):
            # print('containers', chosen_containers, 'sum', sum(chosen_containers))
            
            if sum(chosen_containers) == required_fill:
                possible_combos.append(chosen_containers)

    return possible_combos


def less_containers(possible_combos):

    num_containers = [len(x) for x in possible_combos]
    economic_combos = [x for x in possible_combos if len(x) == min(num_containers)]

    return economic_combos


## the below I did not find a good way to differentiate between same values of fill
# def fill_up_eggnog(containers, required_fill, current_fill=0, used_containers=[]):
#     global possible_combos
#     # if used_containers is None:
#     #     used_containers = []
 

#     for i, container_vol in enumerate(containers):
#         new_fill = current_fill + container_vol
#         # print('used', used_containers, 'current container', container_vol, 'current fill', current_fill)

#         if new_fill > required_fill:
#             pass
#         elif new_fill == required_fill:
#             # if sorted(used_containers + [container_vol]) not in possible_combos:
#             #     possible_combos.append(sorted(used_containers + [container_vol]))
#             if (used_containers + [container_vol]) not in possible_combos:
#                 possible_combos.append(used_containers + [container_vol])
#         else:
#             fill_up_eggnog(containers[:i] + containers[i+1:], required_fill, new_fill, used_containers + [container_vol])



# # load in the actual puzzle input
containers = []

with open('./2015/inputs/d17.txt') as f:
    for j, row in enumerate(f):
        containers.append(int(row))

print('input rows', j+1)

# ================= PART 1 ======================
test_containers = [20, 15, 10, 5, 5]
test_fill = 25

# solution
test_combos = [[15, 10], [20,5], [20,5], [15,5,5]]

possible_combos = fill_up_eggnog(test_containers, test_fill)
assert possible_combos.sort() == test_combos.sort()

# part 2
economic_combos = less_containers(possible_combos)
assert len(economic_combos) == 3


fill = 150
possible_combos = fill_up_eggnog(containers, 150)
economic_combos = less_containers(possible_combos)

print('Part 1 solution:', len(possible_combos))

# ================= PART 2 ======================

print('Part 2 solution:', len(economic_combos))