# Day 10 of 2015
from itertools import groupby

# =========== CLASSES AND FUNCTIONS =============
class LookAndSay:

    def __init__(self, sequence):
        self.sequence = sequence

    def length(self):
        return len(self.sequence)
    
    def update_seq(self):
        # I used to be a for loop, but then I took an arrow to the knee ...
        # the groupby is more optimized. switched to it to compute the 50x repeat
        self.sequence = ''.join([str(len(list(g))) + str(k) for k, g in groupby(self.sequence )])

# =============== TEST CASES ====================
test_results = ['11', '21', '1211', '111221', '312211']
looksay = LookAndSay('1')

for res in test_results:
    looksay.update_seq()
    assert looksay.sequence == res


# =============== PART 1 & 2 ====================

with open('./2015/inputs/d10.txt') as f:
    for row in f:
        initial_look = row.strip()

looksay = LookAndSay(initial_look)

for i in range(50):
    looksay.update_seq()

    if i == 39:
        part_1 = len(looksay.sequence)
        
part_2 = len(looksay.sequence)

print('Part 1 solution:', part_1)
print('Part 2 solution:', part_2)

# based on Conway constant ...
# https://www.youtube.com/watch?v=ea7lJkEhytA

# 10 more steps than 1, using conway's constant 1.303577269034 its just a little off ..
# part_2_calc = part_1 * (1.303577269034)**10
# print(100*(part_2 - part_2_calc) / part_2_calc)

