# Day 8 of 2017

# =========== CLASSES AND FUNCTIONS =============
def process_instruction(instruction, registers, max_reg):
    reg1, val_change, value1, stmt, reg2, condition, value2 = instruction.split()

    if reg1 not in registers:
        registers[reg1] = 0
    if reg2 not in registers:
        registers[reg2] = 0

    if val_change == 'inc':
        val_change = 1
    else:
        val_change = -1

    value1 = int(value1) * val_change
    value2 = int(value2)

    match condition:

        case '<':
            condition_result = registers[reg2] < value2
        case '>':
            condition_result = registers[reg2] > value2
        case '<=':
            condition_result = registers[reg2] <= value2
        case '>=':
            condition_result = registers[reg2] >= value2      
        case '>=':
            condition_result = registers[reg2] >= value2
        case '==':
            condition_result = registers[reg2] == value2
        case '!=':
            condition_result = registers[reg2] != value2
        case _:
            raise('unknown condition!')
        
    if condition_result:
        registers[reg1] += value1
        # part 2
        max_reg = max(max_reg, registers[reg1])

    return registers, max_reg

# =============== TEST CASES ====================
test_instructions = ['b inc 5 if a > 1',
'a inc 1 if b < 5',
'c dec -10 if a >= 1',
'c inc -20 if c == 10']

test_registers = dict()
max_reg = 0

for instruction in test_instructions:
    test_registers, max_reg = process_instruction(instruction, test_registers, max_reg)

assert max(test_registers.values()) == 1
assert max_reg == 10

# =============== PART 1 & 2 ====================
instructions = []

with open('./2017/inputs/d8.txt') as f:
    for row in f:
        instructions.append(row)

registers = dict()
max_reg = 0

for instruction in instructions:
    registers, max_reg = process_instruction(instruction, registers, max_reg)


print('Part 1 solution:', max(registers.values()))
print('Part 2 solution:', max_reg)