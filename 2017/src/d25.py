# Day 25 of 2017
import re
from collections import deque

# =========== CLASSES AND FUNCTIONS =============

def build_instructions(blueprints):

    states = dict()
    for line in blueprints:

        strp_line = line.strip()
        if 'Begin' in strp_line:
            start_state = strp_line[-2]
        elif 'Perform' in strp_line:
            diag_check = int(re.search('\d+', strp_line).group())

        # so the logic here is to build a dictionary for each state
        # and then the two options are a nested dictionary
        if 'In state' in strp_line:
            current_state = strp_line[-2]
            states[current_state] = dict()

        elif 'If' in strp_line:
            current_value = int(strp_line[-2])
            states[current_state][current_value] = []

        elif 'Write' in strp_line:
            states[current_state][current_value].append(int(strp_line[-2]))

        elif 'Move' in strp_line:
            if 'right' in strp_line:
                states[current_state][current_value].append(1)
            else:
                states[current_state][current_value].append(-1)

        elif 'Continue' in strp_line:
            states[current_state][current_value].append(strp_line[-2])

        else:
            pass

    return start_state, diag_check, states
        
def run_diagnostics(current_state, diag_check, states):

    current_pos = 0
    tape = deque([0])

    for _ in range(diag_check):
        current_value = tape[current_pos]
        tmp_val, tmp_dir, tmp_state = states[current_state][current_value]

        # change the tape value
        tape[current_pos] = tmp_val
        # increase or decrease the position
        current_pos += tmp_dir
        # change state
        current_state = tmp_state

        # extend the tape as needed
        if current_pos >= len(tape):
            tape.append(0)
        elif current_pos < 0:
            current_pos = 0
            tape.appendleft(0)
    
    return sum(tape)

# =============== TEST CASES ====================
test_blueprint = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
"""


start_state, diag_check, test_states = build_instructions(test_blueprint.split('\n'))
assert run_diagnostics(start_state, diag_check, test_states) == 3

# ================= PART 1 ======================
blueprint = []

with open('./2017/inputs/d25.txt') as f:
    for row in f:
        blueprint.append(row.strip())

start_state, diag_check, states = build_instructions(blueprint)
checksum = run_diagnostics(start_state, diag_check, states)

print('Part 1 solution:', checksum)