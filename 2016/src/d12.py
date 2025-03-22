# Day 12 of 2016

# =========== CLASSES AND FUNCTIONS =============
def execute_asembunny(assembunny, registers):
    process_line = 0

    while process_line < len(assembunny):

        results = assembunny[process_line].split(' ')

        match results[0]:
            case 'inc':
                registers[results[1]] += 1
                process_line += 1
            case 'dec':
                registers[results[1]] -= 1
                process_line += 1
            case 'cpy':
                if results[1] in registers.keys():
                    registers[results[2]] = registers[results[1]]
                else:
                    registers[results[2]] = int(results[1])
                process_line += 1                    
            case 'jnz':
                if results[1] in registers.keys():
                    tmp_value = registers[results[1]]
                else:
                    tmp_value = int(results[1])

                if tmp_value == 0:
                    process_line += 1
                else:
                    process_line += int(results[2])
                    
            case _:
                raise ValueError('Unknown assembunny command!')
        
# =============== TEST CASES ====================
test_assembunny = ['cpy 41 a',
'inc a',
'inc a',
'dec a',
'jnz a 2',
'dec a']

test_registers = {'a': 0}

execute_asembunny(test_assembunny, test_registers)
assert test_registers['a'] == 42

# ================= PART 1 ======================
assembunny = []

with open('./2016/inputs/d12.txt') as f:
    for row in f:
        assembunny.append(row.strip())


registers = {'a': 0,
             'b': 0,
             'c': 0,
             'd': 0}

execute_asembunny(assembunny, registers)
print('Part 1 solution:', registers['a'])

# ================= PART 2 ======================

registers = {'a': 0,
             'b': 0,
             'c': 1,
             'd': 0}

execute_asembunny(assembunny, registers)
print('Part 2 solution:', registers['a'])