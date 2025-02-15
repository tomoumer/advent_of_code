# Day 13 of 2015
import re
from itertools import permutations


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


# ================= PART 1 ======================

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

# this won't work just because they can be parsed in different order
# assert ['David', 'Alice', 'Bob', 'Carrol'] == best_seating
assert 330 == max_enjoyment

# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d13.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

relationships = map_relationships(puzzle_input)
best_seating, max_enjoyment = rearrange_sitting(relationships)


print('Part 1 solution:', max_enjoyment)

# ================= PART 2 ======================

rest_of_family = relationships.keys()

# add others to mysaelf and myself to others
relationships['myself'] = {x:0 for x in relationships.keys()}
for family_member in rest_of_family:
    relationships[family_member]['myself'] = 0

best_seating, max_enjoyment = rearrange_sitting(relationships)

print('finally seated...', best_seating)
print('Part 2 solution:', max_enjoyment)