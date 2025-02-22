# Day 23 of 2015
import re

def process_instruction(row, registers):
    # print(row)
    jmp_amount = 1
    if 'hlf' in row:
        registers[row[4]] //= 2
    elif 'tpl' in row:
        registers[row[4]] *= 3
    elif 'inc' in row:
        registers[row[4]] += 1
    elif 'jmp' in row:
        jmp_amount = re.search('[+-]\d+', row).group()
    elif 'jie' in row:
        if registers[row[4]] % 2 == 0:
            jmp_amount = re.search('[+-]\d+', row).group()
    elif 'jio' in row:
        if registers[row[4]] == 1:
            jmp_amount = re.search('[+-]\d+', row).group()
    else:
        print('unknown instruction, program end')

    jmp_amount = int(jmp_amount)
    return jmp_amount


registers = {'a': 0,
             'b': 0}

puzzle_input = dict()

with open('./2015/inputs/d23.txt') as f:
    for j, row in enumerate(f):
        puzzle_input[j] = row.strip()
        # process_instruction(row.strip(), registers)

print('input rows', j+1)

# ================= PART 1 ======================

instruction = 0
while instruction < len(puzzle_input.keys()):
    instr_add = process_instruction(puzzle_input[instruction], registers)
    instruction += instr_add

print('Part 1 solution:', registers['b'])

# ================= PART 2 ======================


registers = {'a': 1,
             'b': 0}

instruction = 0
while instruction < len(puzzle_input.keys()):
    instr_add = process_instruction(puzzle_input[instruction], registers)
    instruction += instr_add

print('Part 2 solution:', registers['b'])