# Day 23 of 2016

# =========== CLASSES AND FUNCTIONS =============
# straight from d12 !
def execute_asembunny(assembunny, registers):
    process_line = 0

    while process_line < len(assembunny):

        results = assembunny[process_line].split(' ')

        # depending if it's a letter or number
        if results[1] in registers.keys():
            tmp_res_1 = registers[results[1]]
        else:
            tmp_res_1 = int(results[1])

        match results[0]:
            case 'inc':
                registers[results[1]] += 1
                process_line += 1
            case 'dec':
                registers[results[1]] -= 1
                process_line += 1
            case 'cpy':
                registers[results[2]] = tmp_res_1
                process_line += 1                    
            case 'jnz':
                if results[2] in registers.keys():
                    tmp_res_2 = registers[results[2]]
                else:
                    tmp_res_2 = int(results[2])

                if tmp_res_1 == 0:
                    process_line += 1
                else:
                    process_line += tmp_res_2

            case 'tgl':
                line_to_modify = tmp_res_1 + process_line

                if line_to_modify >= len(assembunny):
                    pass
                
                # target self
                elif line_to_modify == process_line:
                    assembunny[line_to_modify].replace('tgl', 'inc')

                else:
                    mod_results = assembunny[line_to_modify].split(' ')

                    # one argument instructions
                    if len(mod_results) == 2:
                        if mod_results[0] == 'inc':
                            mod_results[0] = 'dec'
                        else:
                            mod_results[0] = 'inc'
                    

                    else: # 2 argument instructions
                        if mod_results[0] == 'jnz':
                            mod_results[0] = 'cpy'
                        else:
                            mod_results[0] = 'jnz'

                    # in either case, save it back:
                    assembunny[line_to_modify] = ' '.join(mod_results)

                process_line += 1

                    
            case _:
                raise ValueError('Unknown assembunny command!')

# =============== TEST CASES ====================
test_assembunny = ['cpy 2 a',
'tgl a',
'tgl a',
'tgl a',
'cpy 1 a',
'dec a',
'dec a']

test_registers = dict()

execute_asembunny(test_assembunny, test_registers)
assert test_registers['a'] == 3

# ================= PART 1 ======================
assembunny = []

with open('./2016/inputs/d23.txt') as f:
    for row in f:
        assembunny.append(row.strip())

registers = {'a': 7}
execute_asembunny(assembunny, registers)

# ================= PART 2 ======================

assembunny = []

with open('./2016/inputs/d23.txt') as f:
    for row in f:
        assembunny.append(row.strip())

registers = {'a': 12}
execute_asembunny(assembunny, registers)

print('Part 2 solution:', registers['a'])
