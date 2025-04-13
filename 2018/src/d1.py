# Day 1 of 2018

# =========== CLASSES AND FUNCTIONS =============
def find_repeating_frequency(freq_changes):

    current_frequency = 0
    explored_frequencies = [current_frequency]

    found_repeat = False
    while not found_repeat:

        for freq_change in freq_changes:
            current_frequency += freq_change

            if current_frequency in explored_frequencies:
                found_repeat = True
                break
            else:
                explored_frequencies.append(current_frequency)

    return current_frequency


# =============== TEST CASES ====================
# I actually don't want to do test cases here as they're in a 
# different format than puzzle input (separated by commas)

# =============== PART 1 & 2 ====================
freq_changes = []

with open('./2018/inputs/d1.txt') as f:
    for row in f:
        freq_changes.append(int(row.strip()))

first_repeat_frequency = find_repeating_frequency(freq_changes)

print('Part 1 solution:', sum(freq_changes))
print('Part 2 solution:', first_repeat_frequency)