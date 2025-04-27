# Day 12 of 2018
import numpy as np
import matplotlib.pyplot as plt

# =========== CLASSES AND FUNCTIONS =============
def parse_notes(notes):
    dict_notes = dict()

    for note in notes:
        prev, next = map(str.strip, note.split('=>'))

        dict_notes[prev] = next

    return dict_notes

def grow_some_plants(notes, state, num_gen):

    start_pot = 0
    # print(state)
    
    # to track how the value changes over generations
    gen_pot_vals = []
    pot_vals = 0
    for i, pot in enumerate(state):
        if pot == '#':
            # have to offest the values depending
            pot_vals += (i+start_pot)

    gen_pot_vals.append(pot_vals)

    for _ in range(num_gen):
        first_hash = state.find('#')
        last_hash = state.rfind('#')
        # add three ... before first # to ensure the negative pots can grow too
        # same after last
        state = '...' + state[first_hash:last_hash+1] + '...' 

        # to know which (negative) value to start counting at
        start_pot += (first_hash - 3) 

        # determine which notes are going to be useful for this particular gen
        useful_notes = dict()
        for k_note in notes.keys():
            if k_note in state:
                useful_notes[k_note] = notes[k_note]

        new_state = []
        for i in range(len(state)):

            if i < 2:
                new_state.append('.')
            elif i > len(state) - 3:
                new_state.append('.')
            else:
                # get the appropriate context to evaluate based on note
                state_part = state[i-2:i+3]
                found_match = False
                for prev_note, next_note in useful_notes.items():
                    if state_part == prev_note:
                        new_state.append(next_note)
                        found_match = True
                        break

                # this is just for test since not all combinations are listed ..
                if not found_match:
                    new_state.append('.')

        state = ''.join(new_state)
        # print(state)

        pot_vals = 0
        for i, pot in enumerate(state):
            if pot == '#':
                # have to offest the values depending
                pot_vals += (i+start_pot)

        gen_pot_vals.append(pot_vals)
    

    return gen_pot_vals



# =============== TEST CASES ====================
initial_state = '#..#.#..##......###...###'

notes = ['...## => #',
'..#.. => #',
'.#... => #',
'.#.#. => #',
'.#.## => #',
'.##.. => #',
'.#### => #',
'#.#.# => #',
'#.### => #',
'##.#. => #',
'##.## => #',
'###.. => #',
'###.# => #',
'####. => #']

notes = parse_notes(notes)
pot_vals = grow_some_plants(notes, initial_state, 20)
assert pot_vals[20] == 325


# =============== PART 1 & 2 ====================
notes = []

with open('./2018/inputs/d12.txt') as f:
    for i, row in enumerate(f):
        if i == 0 :
            initial_state = row.split(':')[1].strip()
            
        elif i > 1:
            notes.append(row.strip())

notes = parse_notes(notes)
pot_vals = grow_some_plants(notes, initial_state, 10000)


# the increase becomes constant after a certain value
# specifically, it becomes 53
pot_diffs = np.diff(np.array(pot_vals))
# plt.plot(pot_diffs)
# plt.show()
# print(np.argwhere(pot_diffs==53))

# at 10000
vals_after_over9BILLION = pot_vals[-1] + 53 * (50000000000-10000)


print('Part 1 solution:', pot_vals[20])
print('Part 2 solution:', vals_after_over9BILLION)

