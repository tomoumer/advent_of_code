# Day 15 of 2017
import re
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
class Generator:

    def __init__(self, start_value, multi_factor):
        self.value = start_value
        self.factor = multi_factor

    def reset_generator(self, start_value):
        self.value = start_value

    def generate_next(self):
        self.value = (self.value * self.factor) % 2147483647
        return self.value


def judge_vals(gen_a, gen_b):

    judged_equal = 0
    judged_equal_2 = 0

    # part 1 counter
    first_count = 0
    # part 2 counters
    gen_a_count = 0
    gen_b_count = 0

    # they won't be in sync, this is to temporarily keep their values
    gen_a_generated = deque()
    gen_b_generated = deque()

    while (first_count <= 40000000) | (gen_a_count < 5000000) | (gen_b_count < 5000000):

        first_count += 1

        # if first_count % 10000000 == 0:
        #     print('repetition', first_count)

        val_a = gen_a.generate_next()
        val_b = gen_b.generate_next()

        if first_count <= 40000000:
            # convert to binary
            val_a_bin = bin(val_a)[2:].zfill(32)
            val_b_bin = bin(val_b)[2:].zfill(32)

            if val_a_bin[16:] == val_b_bin[16:]:
                judged_equal += 1

        if (gen_a_count <= 5000000) & (val_a % 4 == 0):
            gen_a_generated.append(val_a)
            gen_a_count += 1

        if (gen_b_count <= 5000000) & (val_b % 8 == 0):
            gen_b_generated.append(val_b)
            gen_b_count += 1

        if (len(gen_a_generated) > 0) & (len(gen_b_generated) > 0):
            tmp_a = gen_a_generated.popleft()
            tmp_b = gen_b_generated.popleft()

            val_a_bin = bin(tmp_a)[2:].zfill(32)
            val_b_bin = bin(tmp_b)[2:].zfill(32)

            if val_a_bin[16:] == val_b_bin[16:]:
                judged_equal_2 += 1            

    return [judged_equal, judged_equal_2]


# =============== TEST CASES ====================
A = Generator(65, 16807)
B = Generator(8921, 48271)

assert judge_vals(A, B) == [588, 309]


# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2017/inputs/d15.txt') as f:
    for row in f:
        puzzle_input.append(row)

A.reset_generator(int(re.search('\d+', puzzle_input[0]).group()))
B.reset_generator(int(re.search('\d+', puzzle_input[1]).group()))

[judged_equal, judged_equal_2] = judge_vals(A, B)


print('Part 1 solution:', judged_equal)
print('Part 2 solution:', judged_equal_2)