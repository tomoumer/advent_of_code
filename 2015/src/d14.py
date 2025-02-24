# Day 14 of 2015
import re
import numpy as np
import matplotlib.pyplot as plt

# =========== CLASSES AND FUNCTIONS =============
class Reindeer():

    def __init__(self, name, velocity, fly_time, rest, distance, points):
        self.name = name
        self.velocity = velocity
        self.fly_time = fly_time
        self.rest = rest
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
        velocity, fly_time, rest = map(int, re.findall('\d+', reindeer))
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

# =============== TEST CASES ====================
test_reindeer = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
                 'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

test_results = {'Comet': 1120,
                'Dancer': 1056}

test_time = 1000

competing_reindeer = setup_reindeers(test_reindeer)

for reindeer in competing_reindeer:
    dist_travelled = reindeer.compete(test_time)
    assert test_results[reindeer.name] == dist_travelled, f"{reindeer.name} should've travveled {test_results[reindeer.name]}, but did {dist_travelled}"

test_results = {'Comet': 312,
                'Dancer': 689}

competing_reindeer = setup_reindeers(test_reindeer)
# note the new race is evaluated second by second
competing_reindeer = new_race(test_time, competing_reindeer)

for reindeer in competing_reindeer:
    assert test_results[reindeer.name] == reindeer.points


# =============== PART 1 & 2 ====================
deer_definitions = []

with open('./2015/inputs/d14.txt') as f:
    for row in f:
        deer_definitions.append(row.strip())

competition_time = 2503

competing_reindeer = setup_reindeers(deer_definitions)
# this next line is where the competition happens for pt 2.
competing_reindeer = new_race(competition_time, competing_reindeer)

names=[]
scores1=[]
scores2=[]

max_dist = 0 # part 1
max_points = 0 # part 2
for reindeer in competing_reindeer:
    dist_travelled = reindeer.compete(competition_time)
    max_dist = max(dist_travelled, max_dist)
    max_points = max(max_points, reindeer.points)
    # print(reindeer.name, 'travelled', dist_travelled)
    names.append(reindeer.name)
    scores1.append(dist_travelled)
    scores2.append(reindeer.points)


print('Part 1 solution:', max_dist)
print('Part 2 solution:', max_points)

# drawing for funnnn ...
# normalize for better plotting
scores1 = [x/sum(scores1) for x in scores1]
scores2 = [x/sum(scores2) for x in scores2]

fig, ax = plt.subplots(figsize=(8, 8))

# to create the bars
barWidth = 0.3
br1 = np.arange(len(names)) 
br2 = [x + barWidth for x in br1] 

plt.bar(br1, scores1, color ='r', width = barWidth, 
        edgecolor ='black', label ='pt1_score') 
plt.bar(br2, scores2, color ='g', width = barWidth, 
        edgecolor ='black', label ='pt2_score') 

plt.xlabel('Reindeer Olympics', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(names))], names)
ax.get_yaxis().set_visible(False)
plt.legend()
plt.savefig(f'./2015/img/reindeer_olympics_d14.png', bbox_inches='tight', pad_inches=0)
plt.close()
