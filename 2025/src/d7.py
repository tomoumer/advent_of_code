# Day 7 of 2025
import re
day = '7'

# =========== CLASSES AND FUNCTIONS =============
def load_puzzle_input(filepath, kind):

    puzzle_input = []

    with open(filepath) as f:
        for row in f:
            puzzle_input.append(row.strip())

    print(f'{kind} input rows:', len(puzzle_input))
    print('')

    return puzzle_input

# def beamify(manifold):

#     beam = [m.start() for m in re.finditer('S', manifold[0])]
#     new_beam = []
#     num_splits = 0

#     for i, row in enumerate(manifold):
#         if i == 0:
#             continue

#         splitters = [m.start() for m in re.finditer('\^', row)]

#         for beam_part in beam:
            
#             if beam_part not in splitters:
#                 new_beam.append(beam_part)
#             else:
#                 num_splits += 1
#                 # num_timelines *= 2

#                 for s in [1, -1]:
#                     beam_split = beam_part + s
#                     # if beam_split not in new_beam:
#                     new_beam.append(beam_split)

#         # to remove overlapping
#         beam = list(set(new_beam)).copy()
#         new_beam = []
    
#     return num_splits

def worldify(manifold):

    # for pt. 2 need to track how many worlds each beam path carries
    beam = [m.start() for m in re.finditer('S', manifold[0])]
    worldbeam = {beam[0]: 1} # there's only one S

    num_splits = 0

    for i, row in enumerate(manifold):
        if i == 0:
            continue

        splitters = [m.start() for m in re.finditer('\^', row)]

        new_worldbeam = {}
        for beam_part, num_timelines in worldbeam.items():
            
            if beam_part not in splitters:
                if beam_part not in new_worldbeam:
                    new_worldbeam[beam_part] = num_timelines
                else:
                    new_worldbeam[beam_part] += num_timelines
            else:
                num_splits += 1

                for s in [1, -1]:
                    beam_split = beam_part + s
                    if beam_split not in new_worldbeam:
                        new_worldbeam[beam_split] = num_timelines
                    else:
                        new_worldbeam[beam_split] += num_timelines

        worldbeam = new_worldbeam.copy()
    
    # simply sum all the timelines that got created
    total_timelines = sum([timeline for _, timeline in worldbeam.items()])

    return num_splits, total_timelines
                


# =============== TEST CASES ====================
puzzle_input = load_puzzle_input(f'./2025/inputs/d{day}test.txt', 'test')
num_splits, num_timelines = worldify(puzzle_input)
assert num_splits == 21
assert num_timelines == 40

# =============== PART 1 & 2 ====================
puzzle_input = load_puzzle_input(f'./2025/inputs/d{day}.txt', 'actual')
num_splits, num_timelines = worldify(puzzle_input)

print('Part 1 solution:', num_splits)
print('Part 2 solution:', num_timelines)