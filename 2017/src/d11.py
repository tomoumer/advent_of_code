# Day 11 of 2017

# =========== CLASSES AND FUNCTIONS =============
# axial col q row r
def haxor_move(current_coord, move_dir, max_away=0):

    match move_dir:

        case 'nw':
            current_coord[0] -= 0.5
            current_coord[1] += 0.5
        case 'n':
            current_coord[1] += 1
        case 'ne':
            current_coord[0] += 0.5
            current_coord[1] += 0.5
        case 'se':
            current_coord[0] += 0.5
            current_coord[1] -= 0.5
        case 's':
            current_coord[1] -= 1
        case 'sw':
            current_coord[0] -= 0.5
            current_coord[1] -= 0.5

        case _:
            assert('unknown move!')

    max_away = max(max_away, measure_dist(current_coord))

    return current_coord, max_away

def measure_dist(current_coord):
    # total moves are diagonal (in 0.5 chunks)
    # # and vertical (in 1)
    diag_moves = abs(current_coord[0] / 0.5)
    vert_moves = abs(current_coord[1]) - abs(current_coord[0])

    total_moves = diag_moves + vert_moves

    return total_moves


# =============== TEST CASES ====================

test_moves = {'ne,ne,ne': 3,
             'ne,ne,sw,sw': 0,
             'ne,ne,s,s': 2,
             'se,sw,se,sw,sw': 3}

start_coord = [0, 0]

for move_seq, val in test_moves.items():
    current_coord = start_coord.copy()
    # print(current_coord)
    for test_move in move_seq.split(','):
        current_coord = haxor_move(current_coord, test_move)[0]

    assert measure_dist(current_coord) == val

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d11.txt') as f:
    for row in f:
        moves = row.strip()

current_coord = start_coord.copy()
max_away = 0

for move in moves.split(','):
    current_coord, max_away = haxor_move(current_coord, move, max_away)

total_moves = measure_dist(current_coord)


print('Part 1 solution:', int(total_moves))
print('Part 2 solution:', int(max_away))