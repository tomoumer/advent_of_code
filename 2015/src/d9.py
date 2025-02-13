# Day 9 of 2015
from itertools import permutations


# ================= PART 1 ======================
test_distances = [
    'London to Dublin = 464',
    'London to Belfast = 518',
    'Dublin to Belfast = 141']

map_travels = dict()

for row in test_distances:
    destinations, dist = row.split('=')
    dist = int(dist)
    dest_1, dest_2 = destinations.split('to')
    dest_1 = dest_1.strip()
    dest_2 = dest_2.strip()

    if dest_1 not in map_travels.keys():
        map_travels[dest_1] = dict()
    if dest_2 not in map_travels.keys():
        map_travels[dest_2] = dict()
    
    map_travels[dest_1][dest_2] = dist
    map_travels[dest_2][dest_1] = dist

test_routes = {
    ('Dublin', 'London', 'Belfast'): 982,
    ('London', 'Dublin', 'Belfast'): 605,
    ('London', 'Belfast', 'Dublin'): 659,
    ('Dublin', 'Belfast', 'London'): 659,
    ('Belfast', 'Dublin', 'London'): 605,
    ('Belfast', 'London', 'Dublin'): 982
}


for travel_route in permutations(map_travels.keys(), len(map_travels.keys())):
    current_dist = 0

    for i in range(len(travel_route) - 1):
        current_dist += map_travels[travel_route[i]][travel_route[i+1]]

    assert current_dist == test_routes[travel_route], f'Test routes {travel_route} produce {current_dist} instead of {test_routes[travel_route]}'


# load in the actual puzzle input
map_travels = dict()

with open('./2015/inputs/d9.txt') as f:
    for j, row in enumerate(f):
        destinations, dist = row.split('=')
        # print(destinations)
        dist = int(dist)
        dest_1, dest_2 = destinations.split('to')
        dest_1 = dest_1.strip()
        dest_2 = dest_2.strip()

        if dest_1 not in map_travels.keys():
            map_travels[dest_1] = dict()
        if dest_2 not in map_travels.keys():
            map_travels[dest_2] = dict()
        
        map_travels[dest_1][dest_2] = dist
        map_travels[dest_2][dest_1] = dist


min_dist = 10000000
max_dist = 0

for travel_route in permutations(map_travels.keys(), len(map_travels.keys())):
    current_dist = 0

    for i in range(len(travel_route) - 1):
        current_dist += map_travels[travel_route[i]][travel_route[i+1]]

    min_dist = min(min_dist, current_dist)
    max_dist = max(max_dist, current_dist)


print('Part 1 solution:', min_dist)

# ================= PART 2 ======================

print('Part 2 solution:', max_dist)