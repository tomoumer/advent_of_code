# Day 21 of 2016
import re
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def process_operation(operation_str, password, scramble=True):
    # NOTE: scramble is the original, un-scramble is for part 2
    if 'swap position' in operation_str:
        pos1, pos2 = map(int, re.findall('\d', operation_str))

        password = list(password)
        password[pos1], password[pos2] = password[pos2], password[pos1]

    elif 'swap letter' in operation_str:
        letter1, letter2 = re.findall('letter ([a-z])', operation_str)
        # swapping letters with an intermediate temp letter
        password = password.replace(letter1, '%temp%').replace(letter2, letter1).replace('%temp%', letter2)

    elif 'rotate left' in operation_str:
        rotation_val = int(re.search('\d+', operation_str).group())

        password = deque(password)
        if scramble:
            password.rotate(-rotation_val)
        else:
            password.rotate(rotation_val)

    elif 'rotate right' in operation_str:
        rotation_val = int(re.search('\d+', operation_str).group())

        password = deque(password)
        if scramble:
            password.rotate(rotation_val)
        else:
            password.rotate(-rotation_val)

    elif 'rotate based' in operation_str:
        rotation_letter = re.search('letter ([a-z])', operation_str).group(1)
        rotation_idx = re.search(rotation_letter, password).start()

        if scramble:
            rotation_val = 1 + rotation_idx
            if rotation_idx >= 4:
                rotation_val += 1
        else:
            # I deconstructed this by simply doing a mapping based on the 8 char password....
            reverse_rotation = {0:-9,
                                1:-1,
                                2:-6,
                                3:-2,
                                4:-7,
                                5:-3,
                                6:-8,
                                7:-4}
            
            rotation_val = reverse_rotation[rotation_idx]


        password = deque(password)
        password.rotate(rotation_val)


    elif 'reverse' in operation_str:
        letters = re.search('(\d) through (\d)', operation_str)
        letter1_idx = int(letters.group(1))
        letter2_idx = int(letters.group(2))

        # doing this so that both ends are included - letter1_idx can be 0
        reversed_section = password[letter1_idx:letter2_idx+1][::-1]
        password = password[:letter1_idx] + reversed_section + password[letter2_idx+1:]

    elif 'move' in operation_str:
        pos1, pos2 = map(int,re.findall('\d', operation_str))

        if not scramble:
            # reverse the positions
            tmp_pos = pos1
            pos1 = pos2
            pos2 = tmp_pos

        password = list(password)
        removed_letter = password.pop(pos1)
        password.insert(pos2, removed_letter)

    # some of the methods above turn the string into list or deque for rearranging
    if type(password) != str:
        password = ''.join(password)

    return password

# =============== TEST CASES ====================
test_pwd = 'abcde'

test_instructions = {'swap position 4 with position 0': 'ebcda',
                     'swap letter d with letter b': 'edcba',
                     'reverse positions 0 through 4': 'abcde',
                     'rotate left 1 step': 'bcdea',
                     'move position 1 to position 4': 'bdeac',
                     'move position 3 to position 0': 'abdec',
                     'rotate based on position of letter b': 'ecabd',
                     'rotate based on position of letter d': 'decab'}

for operation, test_value in test_instructions.items():

    test_pwd = process_operation(operation,test_pwd)
    assert test_pwd == test_value

# ================= PART 1 ======================

operations_list = []
with open('./2016/inputs/d21.txt') as f:
    for row in f:
        operations_list.append(row.strip())


password = 'abcdefgh'
pwd2 = 'fbgdceah'

for operation in operations_list:
    password = process_operation(operation, password)

print('Part 1 solution:', password)

# ================= PART 2 ======================

for operation in operations_list[::-1]:
    pwd2 = process_operation(operation, pwd2, scramble=False)

print('Part 2 solution:', pwd2)