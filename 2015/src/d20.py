# Day 20 of 2015
import numpy as np


def find_divisor_sum(num):
    if num == 1:
        return (10, 11)
    
    # Start with 1 and number itself
    divisor_sum = 1 + num
    lazy_divisor_sum = 1 + num

    # Only need to check up to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # Add both divisors at once
            divisor_sum += i
            # If i*i != num, add the pair divisor
            if i != num // i:
                divisor_sum += num // i

                if num // i <= 50:
                    lazy_divisor_sum += i
                if i <= 50:
                    lazy_divisor_sum += num // i

            else:
                if i <= 50:
                    lazy_divisor_sum += i

    return (10 * divisor_sum, 11* lazy_divisor_sum)



def find_lowest_house(min_num_presents):
    # not super happy about this, but eh ...
    regular_house_num = 0
    lazy_elves_house_num = 0
    for house_num in range(2000000):
        num_presents, lazy_elves_num_presents = find_divisor_sum(house_num)
        if num_presents > min_num_presents:
            regular_house_num = house_num
        if lazy_elves_num_presents > min_num_presents:
            lazy_elves_house_num = house_num

        if (regular_house_num != 0) & (lazy_elves_house_num != 0):
            return regular_house_num, lazy_elves_house_num



# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d20.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', j+1)

for test_cases in zip(range(1,10), [10,30,40,70,60,120,80,150,130]):
    # print(find_divisors(test))
    assert find_divisor_sum(test_cases[0])[0] == test_cases[1], f"{test_cases[0]} produces {find_divisor_sum(test_cases[0])} not equal to {test_cases[1]}"

# ================= PART 1 ======================


house_num, lazy_elves_house_num = find_lowest_house(int(puzzle_input[0]))

print('Part 1 solution:', house_num)


# ================= PART 2 ======================

print('Part 2 solution:', lazy_elves_house_num)