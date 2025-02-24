# Day 12 of 2015
import re
import json

# =========== CLASSES AND FUNCTIONS =============
def unpack_json(layer):
    global tot_sum
    if type(layer) == list:
        for elem in layer:
            unpack_json(elem)

    # note there's no ints in the keys, or anything else to unpact
    elif type(layer) == dict:
        if 'red' in layer.values():
            # these are the numbers that don't get counted anymore in part 2
            pass
        
        else:
            for elem in layer.values():
                unpack_json(elem)

    elif type(layer) == int:
        tot_sum += layer

# =============== TEST CASES ====================
test_cases = {
    '[1,2,3]': 6,
    '{"a":2,"b":4}': 6,
    '[[[3]]]': 3,
    '{"a":{"b":4},"c":-1}': 3,
    '{"a":[-1,1]}': 0,
    '[-1,{"a":1}]': 0,
    '[]': 0,
    '{}': 0
}

for items, value in test_cases.items():
    all_numbers = [int(x) for x in re.findall('-?\d+', items)]
    assert sum(all_numbers) == value

# ================= PART 1 ======================
with open('./2015/inputs/d12.txt') as f:
    for row in f:
        puzzle_input = row.strip()

all_numbers = map(int, re.findall('-?\d+', puzzle_input))

print('Part 1 solution:', sum(all_numbers))

# ================= PART 2 ======================
# so for the first part I just parsed it as a string .. now  I'm actually going to json
tot_sum = 0

with open('./2015/inputs/d12.json', 'r') as file:
    data = json.load(file)

unpack_json(data)

print('Part 2 solution:',tot_sum)