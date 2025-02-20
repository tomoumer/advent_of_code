# Day 19 of 2015
import re
import random


def create_new_molecules(replacements, molecule):
    possible_molecules = set()
    for orig, repl_list in replacements.items():

        for i in re.finditer(orig, molecule):

            for repl in repl_list:
                new_molecule = molecule[:i.start()] + repl + molecule[i.end():]
                possible_molecules.add(new_molecule)

    return possible_molecules


def deconstruct_molecule(reverse_replacements, current_molecule, final_molecule, step=0):
    global shortest_solution
    
    if step > shortest_solution:
        return
    
    random.shuffle(reverse_replacements)

    for repl in reverse_replacements:
        matched = False
        new_molecule = ''

        for i in re.finditer(repl[1], current_molecule):
            matched = True # if there's at least one
            step += 1
            new_molecule = current_molecule[:i.start()] + repl[2] + current_molecule[i.end():]

            if new_molecule == final_molecule:
                if step < shortest_solution:
                    shortest_solution = step

            else:
                deconstruct_molecule(reverse_replacements, new_molecule, final_molecule, step)
                
            if matched:
                return

    

replacements = dict()
reverse_replacements = []
with open('./2015/inputs/d19.txt') as f:
    for j, row in enumerate(f):
        puzzle_input = row.strip()
        if puzzle_input == '':
            pass
        elif len(puzzle_input) > 20:
            molecule = puzzle_input
        else:
            orig, rep = map(str.strip, puzzle_input.split('=>'))
            if orig not in replacements.keys():
                replacements[orig] = []

            reverse_replacements.append([len(rep) - len(orig), rep, orig])
            replacements[orig].append(rep)

print('replacements', len(replacements))


reverse_replacements = sorted(reverse_replacements, key=lambda x: x[0], reverse=True)
# print(reverse_replacements)



# ================= PART 1 ======================

test_replacements = {'H': ['HO', 'OH'],
                     'O': ['HH']}

test_molecule1 = 'HOH'
test_molecule2 = 'HOHOHO'

assert len(create_new_molecules(test_replacements, test_molecule1)) == 4
assert len(create_new_molecules(test_replacements, test_molecule2)) == 7

new_molecules = create_new_molecules(replacements, molecule)

print('Part 1 solution:', len(new_molecules))

# ================= PART 2 ======================

test_reverse_replacements = [[0, 'H', 'e'],
                        [0, 'O', 'e'],
                        [1, 'HO', 'H'],
                        [1, 'OH', 'H'],
                        [1, 'HH', 'O']]


shortest_solution = 10
for i in range(100):
    deconstruct_molecule(test_reverse_replacements, 'HOH', 'e')
assert shortest_solution == 3

shortest_solution = 10
for i in range(100):
    deconstruct_molecule(test_reverse_replacements, 'HOHOHO', 'e')
assert shortest_solution == 6


shortest_solution = 2*len(molecule)
for i in range(1000):
    deconstruct_molecule(reverse_replacements, molecule, 'e')

print('Part 2 solution:', shortest_solution)

