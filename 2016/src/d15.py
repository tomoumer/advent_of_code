# Day 15 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
def make_discs(disc_descriptions):
    discs = dict()
    for disc in disc_descriptions:
        disc_nr, num_pos, start_time, start_pos = map(int, re.findall('\d+', disc))

        discs[disc_nr] = [start_pos, num_pos]

    return discs

def pass_time(discs):
    initial_time = 0

    while True:

        time = initial_time
        pass_trhough = True

        for disc_nr, [start_pos, num_pos] in discs.items():

            time += 1
            new_pos = (start_pos + time) % num_pos

            if new_pos == 0:
                pass
            else:
                pass_trhough = False
                break

        if pass_trhough:
            return initial_time
        
        initial_time +=1


# =============== TEST CASES ====================
test_discs_descriptions = ['Disc #1 has 5 positions; at time=0, it is at position 4.',
'Disc #2 has 2 positions; at time=0, it is at position 1.']

test_discs = make_discs(test_discs_descriptions)
assert pass_time(test_discs) == 5

# =============== PART 1 & 2 ====================
disc_descriptions = []

with open('./2016/inputs/d15.txt') as f:
    for row in f:
        disc_descriptions.append(row.strip())

discs = make_discs(disc_descriptions)
first_time = pass_time(discs)

print('Part 1 solution:', first_time)

discs[max(discs) + 1] = [0, 11]
first_time = pass_time(discs)

print('Part 2 solution:', first_time)