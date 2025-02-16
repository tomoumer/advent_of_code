# Day 14 of 2015
import re

class Reindeer():

    def __init__(self, name, velocity, fly_time, rest, distance, points):
        self.name = name
        self.velocity = int(velocity)
        self.fly_time = int(fly_time)
        self.rest = int(rest)
        # only for part 2
        self.distance = int(distance)
        self.points = int(points)

    def compete(self, comp_time):
        # rest and fly
        full_cycles = comp_time // (self.fly_time + self.rest)
        distance = full_cycles * self.velocity * self.fly_time 

        remaining_sec = comp_time % (self.fly_time + self.rest)
        distance += min(remaining_sec, self.fly_time) * self.velocity

        return distance
    
    def new_scoring_compete(self, current_time):
        remaining_sec = current_time % (self.fly_time + self.rest)

        # important at 0 still resting!!
        if 0 < remaining_sec <= self.fly_time:
            self.distance += self.velocity * 1
        else: # resting
            pass

    

def setup_reindeers(reindeer_list):
    competing_reindeer = []
    for reindeer in reindeer_list:
        name = re.search('^\w+', reindeer).group(0)
        velocity, fly_time, rest = re.findall('\d+', reindeer)
        competing_reindeer.append(Reindeer(name, velocity, fly_time, rest, 0, 0))

    return competing_reindeer

def new_race(total_time, competing_reindeer):
    max_dist = 0
    for race_time in range(1, total_time+1):
        for reindeer in competing_reindeer:
            reindeer.new_scoring_compete(race_time)
            max_dist = max(max_dist, reindeer.distance)

        for reindeer in competing_reindeer:
            if reindeer.distance == max_dist:
                reindeer.points += 1

    return competing_reindeer


# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d14.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

# ================= PART 1 ======================

test_reindeer = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

test_results = {'Comet': 1120,
                'Dancer': 1056}

competing_reindeer = setup_reindeers(test_reindeer)

for reindeer in competing_reindeer:
    dist_travelled = reindeer.compete(1000)
    assert test_results[reindeer.name] == dist_travelled, f"{reindeer.name} should've travveled {test_results[reindeer.name]}, but did {dist_travelled}"

competing_reindeer = setup_reindeers(puzzle_input)

max_dist = 0
for reindeer in competing_reindeer:
    dist_travelled = reindeer.compete(2503)
    max_dist = max(dist_travelled, max_dist)
    print(reindeer.name, 'travelled', dist_travelled)

print('Part 1 solution:', max_dist)
print('')

# ================= PART 2 ======================

test_results = {'Comet': 312,
                'Dancer': 689}

competing_reindeer = setup_reindeers(test_reindeer)

competing_reindeer = new_race(1000, competing_reindeer)

for reindeer in competing_reindeer:
    assert test_results[reindeer.name] == reindeer.points, f"{reindeer.name} should've gotten {test_results[reindeer.name]} points, but got {reindeer.points}"


competing_reindeer = setup_reindeers(puzzle_input)

competing_reindeer = new_race(2503, competing_reindeer)

max_points = 0
for reindeer in competing_reindeer:
    max_points = max(max_points, reindeer.points)
    print(reindeer.name, 'points gotten', reindeer.points)

print('Part 2 solution:', max_points)
