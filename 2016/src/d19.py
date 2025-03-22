# Day 19 of 2016
from collections import deque
from datetime import datetime

# =========== CLASSES AND FUNCTIONS =============
def elves_white_elephant(num_elves):

    elves = [i for i in range(1, num_elves+1)]

    while num_elves > 1:

        elves = elves[::2]

        # if current cycle is odd, then the 1st one in the
        # next round is going to get eliminated
        if num_elves % 2 == 1:
            elves.pop(0)

        num_elves = len(elves)
        
    return elves[0]

# for pt 2.
def elves_circular_elephant(num_elves):

    elves = deque([i for i in range(1, num_elves+1)])
    while num_elves > 1:

        # we always take the left one, so round down.
        to_steal = num_elves // 2

        elves.rotate(-to_steal)
        elves.popleft()
        elves.rotate(to_steal - 1)

        num_elves -= 1

    return elves[0]

# =============== TEST CASES ====================
assert elves_white_elephant(5) == 3
assert elves_circular_elephant(5) == 2


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d19.txt') as f:
    for row in f:
        num_elves = int(row)

elf_winner = elves_white_elephant(num_elves)
start_elimination = datetime.now()
elf_real_winner = elves_circular_elephant(num_elves)
end_elimination = datetime.now()

print('Part 1 solution:', elf_winner)
# 16 min solution ...
print('Part 2 solution:', elf_real_winner)
print('Part2 execution time', end_elimination- start_elimination)

