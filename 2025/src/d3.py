# Day 3 of 2025

# =========== CLASSES AND FUNCTIONS =============
def find_max_joltage(batteries):
    
    max_joltage = max(batteries)
    num_batteries = len(batteries)
    max_joltage_idx = batteries.index(max_joltage)

    # can't be the last one
    if max_joltage_idx == num_batteries - 1:
        max_joltage = max(batteries[:-1])
        max_joltage_idx = batteries.index(max_joltage)
    
    max_joltage_2 = max(batteries[max_joltage_idx+1:])

    max_jotalge_value = int(max_joltage + max_joltage_2)

    return max_jotalge_value

def find_max_safety_override(batteries):

    # now there needs to be i spaces left
    max_jotalge_value = ''
    max_joltage_idx = -1

    for i in range(11,0,-1):
        max_joltage = max(batteries[max_joltage_idx+1 : -i])
        max_jotalge_value += max_joltage

        # because it's a subset, the index needs to be added
        max_joltage_idx += batteries[max_joltage_idx+1:].index(max_joltage) + 1

    # final one, to the end
    max_joltage = max(batteries[max_joltage_idx+1 : ])
    max_jotalge_value += max_joltage

    max_jotalge_value = int(max_jotalge_value)

    return max_jotalge_value

# =============== TEST CASES ====================
test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
output_joltage = 0
output_override = 0

for batterires in test_input.strip().split('\n'):
    output_joltage += find_max_joltage(batterires)
    output_override += find_max_safety_override(batterires)

assert output_joltage == 357
assert output_override == 3121910778619

# =============== PART 1 & 2 ====================
puzzle_input = []
output_joltage = 0
output_override = 0

with open('./2025/inputs/d3.txt') as f:
    for row in f:
        puzzle_input.append(row.strip())
        output_joltage += find_max_joltage(row.strip())
        output_override += find_max_safety_override(row.strip())

print('input rows', len(puzzle_input))


print('Part 1 solution:', output_joltage)
print('Part 2 solution:', output_override)



