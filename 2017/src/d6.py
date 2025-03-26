# Day 6 of 2017
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def memory_realloc(banks):
    seen_config = list()
    seen_config.append('-'.join([str(b) for b in banks]))
    num_cycles = 0

    while True:
        num_cycles += 1
        max_val = np.max(banks)
        max_idx = np.argmax(banks)

        # annull the bank that is getting redistributed 
        banks[np.argmax(banks)] = 0

        # this is the amount that all indicess will increase
        all_idx_inc = max_val // len(banks)
        banks_inc = np.ones(len(banks), int) * all_idx_inc

        # this is num of indices after argmax that will increase by additional 1
        remaining_inc = max_val % len(banks)

        # increase to the end of the array
        banks_inc[max_idx+1: max_idx+1 + remaining_inc] += 1

        # start again from beginning if needed
        if max_idx + remaining_inc >= len(banks):
            banks_inc[:max_idx+1 + remaining_inc - len(banks)] += 1

        # the rest in one fell swoop
        banks += banks_inc

        new_config = '-'.join([str(b) for b in banks])

        if new_config in seen_config:
            return [num_cycles, len(seen_config) - seen_config.index(new_config)]
        else:
            seen_config.append(new_config)



# =============== TEST CASES ====================
test_banks = '0 2 7 0'
test_banks = np.array(list(map(int, test_banks.split())))

assert memory_realloc(test_banks) == [5, 4]

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d6.txt') as f:
    for row in f:
        banks = np.array(list(map(int, row.split())))

redistr_cycles, loop_size = memory_realloc(banks)


print('Part 1 solution:', redistr_cycles)
print('Part 2 solution:', loop_size)