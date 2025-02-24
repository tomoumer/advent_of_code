# Day 13 of 2015
import re
from itertools import permutations
import matplotlib.pyplot as plt
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def map_relationships(tmp_rel):
    relationships = dict()
    for rel in tmp_rel:
        rel = rel.strip()
        person1 = re.search('^\w+', rel).group(0)
        person2 = re.search('(\w+)\.$', rel).group(1)
        happiness_adjust = re.search('\d+', rel).group(0)
        if 'lose' in rel:
            happiness_adjust = - int(happiness_adjust)
        else:
            happiness_adjust = int(happiness_adjust)


        if person1 not in relationships.keys():
            relationships[person1] = dict()
        
        relationships[person1][person2] = happiness_adjust
    
    return relationships

def rearrange_sitting(relationships):
    best_seating = []
    max_enjoyment = 0

    for seating_arrangement in permutations(relationships.keys(), len(relationships.keys())):
        current_enjoyment = 0

        for i in range(len(seating_arrangement) - 1):
            # both ways
            current_enjoyment += relationships[seating_arrangement[i]][seating_arrangement[i+1]]
            current_enjoyment += relationships[seating_arrangement[i+1]][seating_arrangement[i]]

        # it's circular, need to connect last to first
        current_enjoyment += relationships[seating_arrangement[0]][seating_arrangement[-1]]
        current_enjoyment += relationships[seating_arrangement[-1]][seating_arrangement[0]]

        if current_enjoyment > max_enjoyment:
            max_enjoyment = current_enjoyment
            best_seating = seating_arrangement

    return best_seating, max_enjoyment

# =============== TEST CASES ====================
test_relationships = [
'Alice would gain 54 happiness units by sitting next to Bob.',
'Alice would lose 79 happiness units by sitting next to Carol.',
'Alice would lose 2 happiness units by sitting next to David.',
'Bob would gain 83 happiness units by sitting next to Alice.',
'Bob would lose 7 happiness units by sitting next to Carol.',
'Bob would lose 63 happiness units by sitting next to David.',
'Carol would lose 62 happiness units by sitting next to Alice.',
'Carol would gain 60 happiness units by sitting next to Bob.',
'Carol would gain 55 happiness units by sitting next to David.',
'David would gain 46 happiness units by sitting next to Alice.',
'David would lose 7 happiness units by sitting next to Bob.',
'David would gain 41 happiness units by sitting next to Carol.'
]

relationships = map_relationships(test_relationships)
best_seating, max_enjoyment = rearrange_sitting(relationships)
assert 330 == max_enjoyment

# ================= PART 1 ======================
all_relationships = []

with open('./2015/inputs/d13.txt') as f:
    for row in f:
        all_relationships.append(row.strip())

relationships = map_relationships(all_relationships)
best_seating, max_enjoyment = rearrange_sitting(relationships)


print('Part 1 solution:', max_enjoyment)

# ================= PART 2 ======================

# add others to mysaelf and myself to others
rest_of_family = relationships.keys()
relationships['myself'] = {x:0 for x in relationships.keys()}
for family_member in rest_of_family:
    relationships[family_member]['myself'] = 0

best_seating, max_enjoyment = rearrange_sitting(relationships)

# print('finally seated...', best_seating)
print('Part 2 solution:', max_enjoyment)

# drawing for fun ...
n = len(best_seating)
fig, ax = plt.subplots(figsize=(6, 6))

circle = plt.Circle((0, 0), 0.7, facecolor='sandybrown', fill=True, edgecolor='saddlebrown', hatch='/', linestyle='-', linewidth=3)
ax.add_patch(circle)

angles = np.linspace(0, 2 * np.pi, n, endpoint=False)

for i, angle in enumerate(angles):
    x = np.cos(angle)
    y = np.sin(angle)
    ax.text(x, y, best_seating[i], fontsize=12, ha='center', va='center', 
            bbox=dict(facecolor='sandybrown', edgecolor='saddlebrown', boxstyle='round,pad=0.3'))

ax.text(0,0, 'ARE YOU NOT\n ENTERTAINED?', fontsize=12, ha='center', va='center',
        bbox=dict(facecolor='sandybrown', edgecolor='saddlebrown', boxstyle='round,pad=0.3'))

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')
plt.savefig(f'./2015/img/best_sitting_d13.png', bbox_inches='tight', pad_inches=0)
plt.close()
