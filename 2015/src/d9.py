# Day 9 of 2015
from itertools import permutations

# =========== CLASSES AND FUNCTIONS =============
def map_travel_destinations(distances):
    map_travels = dict()
    for row in distances:
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
    
    return map_travels

def evaluate_travel_routes(map_travels):
    all_travel_routes = dict()
    for travel_route in permutations(map_travels.keys(), len(map_travels.keys())):
        current_dist = 0

        for i in range(len(travel_route) - 1):
            current_dist += map_travels[travel_route[i]][travel_route[i+1]]

        all_travel_routes[travel_route] = current_dist

    return all_travel_routes

# =============== TEST CASES ====================

test_routes = {
    ('Dublin', 'London', 'Belfast'): 982,
    ('London', 'Dublin', 'Belfast'): 605,
    ('London', 'Belfast', 'Dublin'): 659,
    ('Dublin', 'Belfast', 'London'): 659,
    ('Belfast', 'Dublin', 'London'): 605,
    ('Belfast', 'London', 'Dublin'): 982
}

test_distances = [
    'London to Dublin = 464',
    'London to Belfast = 518',
    'Dublin to Belfast = 141']

test_map_travels = map_travel_destinations(test_distances)
assert test_routes == evaluate_travel_routes(test_map_travels)


# =============== PART 1 & 2 ====================
distances = []
with open('./2015/inputs/d9.txt') as f:
    for row in f:
        distances.append(row.strip())

map_travels = map_travel_destinations(distances)
all_travel_routes = evaluate_travel_routes(map_travels)

min_dist = min(all_travel_routes.values())
max_dist = max(all_travel_routes.values())

print('Part 1 solution:', min_dist)
print('Part 2 solution:', max_dist)