# Day 6 of 2025
import numpy as np
import re

day = '6'

# =========== CLASSES AND FUNCTIONS =============
def load_puzzle_input(filepath, kind):

    puzzle_input = []
    puzzle_input2 = []

    with open(filepath) as f:
        for row in f:
            puzzle_input.append(row.strip().split())
            puzzle_input2.append([(m.start(0), m.end(0)) for m in re.finditer('\d+', row)])
            # print(row.strip())
            # print([(m.start(0), m.end(0)) for m in re.finditer('\d+', row)])

    print(f'{kind} input rows:', len(puzzle_input))
    print('')

    return puzzle_input, puzzle_input2

# def do_math(homework):
    
#     final_result = 0

#     for i in range(len(homework[-1])):
#         if homework[-1][i] == '+':
#             current_calc = 0
#         else:
#             current_calc = 1

#         for row in homework[:-1]:
#             if homework[-1][i] == '+':
#                 current_calc += int(row[i])
#             else:
#                 current_calc *= int(row[i])

#         final_result += current_calc
    
#     return final_result

def do_math(homework, positions):

    result_wrong = 0
    result_correct = 0

    for i in range(len(homework[-1])):
        if homework[-1][i] == '+':
            current_calc1 = 0
            current_calc2 = 0
        else:
            current_calc1 = 1
            current_calc2 = 1

        correct_numbers = {}
        for j in range(len(homework)-1):
            row_num = homework[j][i]

            # part 1
            if homework[-1][i] == '+':
                current_calc1 += int(row_num)
            else:
                current_calc1 *= int(row_num)

            # part 2, assemble correct digits
            start_digit = positions[j][i][0]
            end_digit = positions[j][i][1]

            for n, d in enumerate(range(start_digit, end_digit)):
                if d in correct_numbers:
                    correct_numbers[d] += row_num[n]
                else:
                    correct_numbers[d] = row_num[n]

        # part 2 calculate
        for correct_num in correct_numbers.values():
            if homework[-1][i] == '+':
                current_calc2 += int(correct_num)
            else:
                current_calc2 *= int(correct_num)

        result_wrong += current_calc1
        result_correct += current_calc2
    
    return result_wrong, result_correct



# print('123'[-4])

# =============== TEST CASES ====================
numbers, positions = load_puzzle_input(f'./2025/inputs/d{day}test.txt', 'test')
homework_result, homework_corrected = do_math(numbers, positions)
assert homework_result == 4277556
assert homework_corrected == 3263827


# =============== PART 1 & 2 ====================
numbers, positions = load_puzzle_input(f'./2025/inputs/d{day}.txt', 'actual')
homework_result, homework_corrected = do_math(numbers, positions)

print('Part 1 solution:', homework_result)
print('Part 2 solution:', homework_corrected)