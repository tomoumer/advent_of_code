# Day 1 of 2017

# =========== CLASSES AND FUNCTIONS =============
def solve_captcha(input_sequence):
    digit_sum = 0
    new_digit_sum = 0

    for i in range(len(input_sequence)):
    
        if input_sequence[i] == input_sequence[i-1]:
            digit_sum += int(input_sequence[i])

        if input_sequence[i] == input_sequence[i - len(input_sequence) // 2]:
            new_digit_sum += int(input_sequence[i])

    return digit_sum, new_digit_sum



# =============== TEST CASES ====================
test_sequences = {'1122': 3,
                  '1111': 4,
                  '1234': 0,
                  '91212129': 9}

for test_sequence, test_result in test_sequences.items():
    assert solve_captcha(test_sequence)[0] == test_result

test_sequences = {'1212': 6,
                  '1221': 0,
                  '123123': 12,
                  '12131415': 4}

for test_sequence, test_result in test_sequences.items():
    assert solve_captcha(test_sequence)[1] == test_result


# =============== PART 1 & 2 ====================

with open('./2017/inputs/d1.txt') as f:
    for row in f:
        sequence = row.strip()

captcha1, captcha2 = solve_captcha(sequence)

print('Part 1 solution:', captcha1)
print('Part 2 solution:', captcha2)