# Day 23 of 2017
import re

# =========== CLASSES AND FUNCTIONS =============
def extract_value(val, registers):
    if re.match('-?\d+', val):
        val = int(val)
    else:
        val = registers[val]

    return val

def assemble_away(instructions, debug=True):
    registers = {key: 0 for key in 'abcdefgh'}
    if not debug:
        registers['a'] = 1
    instruction_in = 0

    num_mul = 0

    while True:
        if (instruction_in < 0) | (instruction_in >= len(instructions)):
            break

        if not debug:
            # basically, checking for nonprimes, after b and c have been loaded
            if (instruction_in >= 9):
                for b in range(registers['b'], registers['c']+1, 17):
                    if any(b % d == 0 for d in range(2, int(b**0.5))):
                        registers['h'] += 1
                
                return registers['h']

        instruction = instructions[instruction_in]
        instruction_in += 1

        command, x, y = instruction.split()
        y = extract_value(y, registers)

        match command:

            case 'set':
                registers[x] = y

            case 'sub':
                registers[x] -= y

            case 'mul': 
                registers[x] *= y
                num_mul += 1

            case 'jnz': #X Y'
                x = extract_value(x, registers)
                if x != 0:
                    # note the -1 is because I increment instruction in each loop
                    instruction_in = instruction_in -1 + y

    if debug:
        return num_mul


# =============== PART 1 & 2 ====================
instructions = []

with open('./2017/inputs/d23.txt') as f:
    for row in f:
        instructions.append(row.strip())

num_mul = assemble_away(instructions)

reg_h = assemble_away(instructions, debug=False)

print('Part 1 solution:', num_mul)
print('Part 2 solution:', reg_h)
