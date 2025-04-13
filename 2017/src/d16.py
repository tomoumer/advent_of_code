# Day 16 of 2017

# =========== CLASSES AND FUNCTIONS =============
def dance_dance_revolution(programs, dance_moves):

    # turn the string into list for easier manipulation
    programs = list(programs)

    for dance_move in dance_moves.split(','):

        match dance_move[0]:

            case 's':
                spin = int(dance_move[1:])
                programs = programs[-spin:] + programs[:-spin]
            case 'x':
                idx1, idx2 = map(int, dance_move[1:].split('/'))
                letter1 = programs[idx1]
                letter2 = programs[idx2]

                # replace, i.e. swap
                programs[idx2] = letter1
                programs[idx1] = letter2
            case 'p':
                letter1, letter2 = dance_move[1:].split('/')
                programs = ''.join(programs)
                programs = programs.replace(letter1, 't')
                programs = programs.replace(letter2, letter1)
                programs = programs.replace('t', letter2)
                programs = list(programs)
            case _:
                raise('unknown dance move!')     
            
    return ''.join(programs)


# =============== TEST CASES ====================
programs = 'abcde'
dance_moves = 's1,x3/4,pe/b'
assert dance_dance_revolution(programs, dance_moves) == 'baedc'

# =============== PART 1 & 2 ====================

start_programs = 'abcdefghijklmnop'

with open('./2017/inputs/d16.txt') as f:
    for row in f:
        dance_moves = row.strip()

programs = [start_programs]
programs.append(dance_dance_revolution(start_programs, dance_moves))

print('Part 1 solution:', programs[0])

for i in range(2,1000000):
    if i % 100000000 == 0:
        print(i)

    programs.append(dance_dance_revolution(programs[-1], dance_moves))

    # find the repetition cycle
    if programs[-1] == start_programs:
        cycle_repeats = i
        break

final_run = 1000000000 % cycle_repeats

print('Part 2 solution:', programs[final_run])

