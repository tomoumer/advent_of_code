# Day 10 of 2015
from itertools import groupby

class LookAndSay:

    def __init__(self, sequence):
        self.sequence = sequence

    def length(self):
        return len(self.sequence)
    
    def update_seq(self):
        # new_sequence = ''
        # repeat = 1

        # for i in range(1, len(self.sequence)):
        #     if self.sequence[i] == self.sequence[i-1]:
        #         repeat += 1
        #     else:
        #         new_sequence = new_sequence + str(repeat) + self.sequence[i-1]
        #         repeat = 1

        # # append last one
        # new_sequence = new_sequence + str(repeat) + self.sequence[-1]
        # #update
        # self.sequence = new_sequence

        # the groupby is more optimized. switched to it to compute the 50x repeat
        self.sequence = ''.join([str(len(list(g))) + str(k) for k, g in groupby(self.sequence )])



# ================= PART 1 ======================
test_results = ['11', '21', '1211', '111221', '312211']
looksay = LookAndSay('1')

for res in test_results:
    looksay.update_seq()
    assert looksay.sequence == res, f"{res} failed test"


with open('./2015/inputs/d10.txt') as f:
    for j, row in enumerate(f):
        initial_look = row.strip()

looksay = LookAndSay(initial_look)

# lmbda = 1

for i in range(50):
    looksay.update_seq()

    if i == 39:
        part_1 = len(looksay.sequence)
        
part_2 = len(looksay.sequence)

print('Part 1 solution:', part_1)

# ================= PART 2 ======================

# based on conway const ...
# https://www.youtube.com/watch?v=ea7lJkEhytA

# 10 more steps than 1, using conway's constant 1.303577269034 its just a little off ..
# part_2 = part_1 * (1.303577269034)**10

print('Part 2 solution:', part_2)

