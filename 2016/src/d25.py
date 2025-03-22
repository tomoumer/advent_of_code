# Day 25 of 2016

# =========== CLASSES AND FUNCTIONS =============
# straight from d23 !
def execute_asembunny(assembunny, registers):
    process_line = 0

    num_out = 0

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

            case 'out':
                num_out += 1

                if (num_out % 2 == 1) and (tmp_res_1 != 0):
                    return 0
                
                if (num_out % 2 == 0) and (tmp_res_1 != 1):
                    return 0
                
                if num_out >= 10:
                    return 1
                
                process_line += 1
              
            case _:
                raise ValueError('Unknown assembunny command!')

# ================= PART 1 ======================
assembunny = []

with open('./2016/inputs/d25.txt') as f:
    for row in f:
        assembunny.append(row.strip())

for i in range(100000):

    registers = {'a': i}
    returns = execute_asembunny(assembunny, registers)
    if returns == 1:
        break


print('Part 1 solution:', i)
