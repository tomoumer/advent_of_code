# Day 24 of 2017
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def make_bridges(components):

    bridge_parts = deque([[[0,0], components]])
    max_bridge_strength = 0

    # part 3
    longest_bridge = 0
    max_longest_bridge_strength = 0

    while bridge_parts:

        current_bridge, remaining_parts = bridge_parts.popleft()

        # add all possible extensions
        final_part = True
        for i, part in enumerate(remaining_parts):
            if current_bridge[-1] == part[0]:

                # there's a possible extension
                final_part = False
                bridge_parts.append([current_bridge + part, remaining_parts[:i] + remaining_parts[i+1:]])

            # invert the part if it doesn't fit one way
            elif current_bridge[-1] == part[1]:
                final_part = False
                bridge_parts.append([current_bridge + part[::-1], remaining_parts[:i] + remaining_parts[i+1:]])

        if final_part:
            max_bridge_strength = max(max_bridge_strength, sum(current_bridge))

        if final_part:
            if len(current_bridge) == longest_bridge:
                max_longest_bridge_strength = max(max_longest_bridge_strength, sum(current_bridge))
            else: # longer
                max_longest_bridge_strength = sum(current_bridge)

    return max_bridge_strength, max_longest_bridge_strength

# =============== TEST CASES ====================
tcps = ['0/2',
'2/2',
'2/3',
'3/4',
'3/5',
'0/1',
'10/1',
'9/10']

test_components = []
for tcp in tcps:
    test_components.append(list(map(int, tcp.split('/'))))

assert make_bridges(test_components) == (31, 19)

# =============== PART 1 & 2 ====================
components = []

with open('./2017/inputs/d24.txt') as f:
    for row in f:
        components.append(list(map(int, row.strip().split('/'))))

max_bridge_strength, max_longest_bridge_strength = make_bridges(components)

print('Part 1 solution:', max_bridge_strength)
print('Part 2 solution:', max_longest_bridge_strength)