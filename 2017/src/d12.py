# Day 12 of 2017
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def parse_pipe(program_pipe, program_dict):

    program_from, programs_to = program_pipe.split('<->')
    programs_to = list(map(int, programs_to.split(',')))

    program_dict[int(program_from)] = programs_to

def explore_pipes(program_dict):
    groups = []

    for start_id in range(0, len(program_dict)):
        # check if the current id is already in one of the existing groups
        is_in_group = False
        for group in groups:
            if start_id in group:
                is_in_group = True
                continue

        if is_in_group:
            continue

        connected = [start_id]

        # this one to indicate where to go next
        plumbing_queue = deque([start_id])

        while plumbing_queue:

            current_id = plumbing_queue.popleft()

            for program_id in program_dict[current_id]:
                if program_id not in connected:
                    connected.append(program_id)
                    plumbing_queue.append(program_id)

        groups.append(connected)
        
    return groups

# =============== TEST CASES ====================
test_programs = ['0 <-> 2',
'1 <-> 1',
'2 <-> 0, 3, 4',
'3 <-> 2, 4',
'4 <-> 2, 3, 6',
'5 <-> 6',
'6 <-> 4, 5']

test_program_dict = {}

for program_pipe in test_programs:
    parse_pipe(program_pipe, test_program_dict)

test_groups = explore_pipes(test_program_dict)

assert len(test_groups[0]) == 6
assert len(test_groups) == 2

# =============== PART 1 & 2 ====================

program_dict = {}

with open('./2017/inputs/d12.txt') as f:
    for row in f:
        parse_pipe(row, program_dict)

groups = explore_pipes(program_dict)

print('Part 1 solution:', len(groups[0]))
print('Part 2 solution:', len(groups))