# Day 11 of 2016
import re
from copy import deepcopy
from collections import deque
import random
from itertools import combinations, product

# =========== CLASSES AND FUNCTIONS =============
def check_if_stable(levels_to_check, current_configuration):
    is_stable = True

    for level in levels_to_check:

        if len(current_configuration[level]) < 2:
            continue
        else:
            generators = []
            microchips = []
            for component in current_configuration[level]:
                if component[1] == 'generator':
                    generators.append(component[0])
                else:
                    microchips.append(component[0])

            generators = set(generators)
            microchips = set(microchips)
            num_both = len(generators.intersection(microchips))
            num_gen = len(generators.difference(microchips))
            num_mic = len(microchips.difference(generators))

            if (num_mic > 0) and ((num_gen > 0) | (num_both > 0)):
                is_stable = False
                return is_stable
                
    return is_stable


def construct_valid_moves(current_elevator_level, current_configuration):
    # pick one element or two if they're available on that floor
    transport_elements = list(combinations(current_configuration[current_elevator_level], 1))

    if len(current_configuration[current_elevator_level]) > 1:
        transport_elements.extend(list(combinations(current_configuration[current_elevator_level], 2)))
    
    possible_levels = []
    if current_elevator_level < 4:
        possible_levels.append(1) 
    if (current_elevator_level == 2) & (len(current_configuration[1]) > 0):
        possible_levels.append(-1)
    elif (current_elevator_level == 3) & ((len(current_configuration[1]) > 0) | (len(current_configuration[2]) > 0)):
        possible_levels.append(-1)
    elif current_elevator_level == 4:
        possible_levels.append(-1)

    possible_moves = list(product(transport_elements, possible_levels))

    return possible_moves

def move_components_around(elevator_level, configuration):
    fastest_solution = float('inf')
    # deque is apparently faster than list, O(1) instead of O(n)
    queue = deque([(elevator_level, configuration, 0)])
    # Store checked configurations as (elevator_level, config_hash)
    checked_configurations = {}
    
    while queue:
        current_elevator_level, current_configuration, move_nr = queue.popleft()
        
        # Check if we've reached the target (all items on 4th floor)
        if len(current_configuration[1]) == 0 and len(current_configuration[2]) == 0 and len(current_configuration[3]) == 0:
            fastest_solution = min(fastest_solution, move_nr)
            # print('found one', fastest_solution)
            continue

        if move_nr >= fastest_solution:
            continue

        # Generate a hashable representation of the configuration
        config_hash = hash_configuration(current_elevator_level, current_configuration)
        
        # Check if we've seen this configuration before with a lower move count
        if config_hash in checked_configurations:
            if checked_configurations[config_hash] <= move_nr:
                continue

        checked_configurations[config_hash] = move_nr

        possible_moves = construct_valid_moves(current_elevator_level, current_configuration)

        for move in possible_moves:
           # Skip moving down with 2 elements (optimization)
            if len(move[0]) > 1 and move[1] == -1:
                continue
                
            new_elevator_level = current_elevator_level + move[1]
            new_configuration = deepcopy(current_configuration)
            
            # Move elements
            for element in move[0]:
                new_configuration[current_elevator_level].remove(element)
                new_configuration[new_elevator_level].append(element)
                
            # Check stability
            if check_if_stable([current_elevator_level, new_elevator_level], new_configuration):
                queue.append((new_elevator_level, new_configuration, move_nr + 1))
    
    return fastest_solution

def hash_configuration(elevator_level, configuration):
    # convert config to a tuple which is a hashable format.
    result = [elevator_level]
    for level in range(1,5):
        # Sort the components on each level for consistent hashing
        generators = []
        microchips = []
        for component in configuration[level]:
            if component[1] == 'generator':
                generators.append(component[0])
            else:
                microchips.append(component[0])

        generators = set(generators)
        microchips = set(microchips)

        # pairs of generator-microchip
        num_both = len(generators.intersection(microchips))
        num_gen = len(generators.difference(microchips))
        num_mic = len(microchips.difference(generators))
        level_str = f"{level}:{num_both},{num_gen},{num_mic}"

        # components = sorted(configuration[level])
        # level_str = f"{level}:" + ",".join(f"{comp[0]}-{comp[1]}" for comp in components)
        result.append(level_str)
    return tuple(result)

# =============== TEST CASES ====================
test_setup = ['The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
              'The second floor contains a hydrogen generator.',
              'The third floor contains a lithium generator.',
              'The fourth floor contains nothing relevant.']


test_configuration = {1: [],
                      2: [],
                      3: [],
                      4: []}

for i, test_floor in enumerate(test_setup):
    microchips = re.findall('([a-z]+)-compatible (microchip)', test_floor)
    if len(microchips) > 0:
        test_configuration[i+1].extend(microchips)

    generators = re.findall('([a-z]+) (generator)', test_floor)
    if len(generators) > 0:
        test_configuration[i+1].extend(generators)

nr_moves = move_components_around(elevator_level=1, configuration=test_configuration)
assert nr_moves == 11



# ================= PART 1 ======================
puzzle_input = []
configuration = {1: [],
                2: [],
                3: [],
                4: []}

with open('./2016/inputs/d11.txt') as f:
    for i, row in enumerate(f):
        microchips = re.findall('([a-z]+)-compatible (microchip)', row)
        if len(microchips) > 0:
            configuration[i+1].extend(microchips)

        generators = re.findall('([a-z]+) (generator)', row)
        if len(generators) > 0:
            configuration[i+1].extend(generators)


nr_moves_pt1 = move_components_around(elevator_level=1, configuration=configuration)

print('Part 1 solution:', nr_moves_pt1)


# ================= PART 2 ======================


configuration[1].extend([('elerium', 'generator'), ('elerium', 'microchip'), ('dilithium', 'generator'), ('dilithium', 'microchip')])


nr_moves_pt2 = move_components_around(elevator_level=1, configuration=configuration)

print('Part 2 solution:', nr_moves_pt2)