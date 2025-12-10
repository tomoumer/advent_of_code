# Day 8 of 2025
import math
day = '8'

# =========== CLASSES AND FUNCTIONS =============
def load_puzzle_input(filepath, kind):

    puzzle_input = []

    with open(filepath) as f:
        for row in f:
            puzzle_input.append(list(map(int, row.strip().split(','))))

    print(f'{kind} input rows:', len(puzzle_input))
    print('')

    return puzzle_input

def make_circuits(junction_boxes):

    checked_boxes = []
    box_distances = {}

    for i in range(len(junction_boxes)):
        # save the idx of checked box
        checked_boxes.append(i)
        box1 = junction_boxes[i]

        box_distances[i] = []
        
        # print('')

        for j in range(len(junction_boxes)):
            if j in checked_boxes:
                continue

            box2 = junction_boxes[j]
            
            dist = (box1[0] - box2[0])**2 + (box1[1] - box2[1])**2 + (box1[2] - box2[2])**2 
            dist = math.sqrt(dist)
            # print(dist)
            box_distances[i].append(dist)
        
    return box_distances

def find_shortest(box_distances, num_connections):

    box_groups = []

    for i in range(1000000):
        current_shortest_dist = 999999999
        if i == 0:
            # this one so that we don't keep taking the same shortest dist
            shortest_dist = 0

        for box_nr1, distances in box_distances.items():
            for box_nr2, distance in enumerate(distances):
                if (distance > shortest_dist) and (distance < current_shortest_dist):
                    box_pair = [box_nr1, box_nr1 + box_nr2 + 1]
                    current_shortest_dist = distance

        shortest_dist = current_shortest_dist
        box_groups.append(box_pair)
        # print(box_groups)

        box_groups = join_groups(box_groups)
        # print(box_groups)

        if i == num_connections-1:
            circuit_sizes = 1
            box_groups.sort(key=len, reverse=True)
            for j, box_group in enumerate(box_groups):
                if j > 2:
                    break
                circuit_sizes *= len(box_group)

        if len(box_groups[0]) == len(box_distances.keys()):
            break

    return circuit_sizes, box_pair

def join_groups(box_groups):

    sets = [set(lst) for lst in box_groups]
    
    merged = []
    for current in sets:

        overlapping = [s for s in merged if s & current]
        
        if overlapping:
            for s in overlapping:
                merged.remove(s)
                current = current | s
        
        merged.append(current)
    
    # Convert back to lists
    box_groups = [list(s) for s in merged]

    return box_groups

        

# =============== TEST CASES ====================
puzzle_input = load_puzzle_input(f'./2025/inputs/d{day}test.txt', 'test')
box_distances = make_circuits(puzzle_input)
circuit_sizes, final_pair = find_shortest(box_distances, 10)
assert circuit_sizes == 40
wall_dist = puzzle_input[final_pair[0]][0] * puzzle_input[final_pair[1]][0]
assert wall_dist == 25272

# =============== PART 1 & 2 ====================
puzzle_input = load_puzzle_input(f'./2025/inputs/d{day}.txt', 'actual')
box_distances = make_circuits(puzzle_input)
circuit_sizes, final_pair = find_shortest(box_distances, 1000)
wall_dist = puzzle_input[final_pair[0]][0] * puzzle_input[final_pair[1]][0]


print('Part 1 solution:', circuit_sizes)
print('Part 2 solution:', wall_dist)