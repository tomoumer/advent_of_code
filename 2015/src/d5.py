# Day 5 of 2015


def is_it_nice(naughty_string):
    # these overwrite anything else
    if any(x in naughty_string for x in ('ab', 'cd', 'pq', 'xy')):
        return False
    
    num_vowels = 0
    for vowel in 'aeiou':
        num_vowels += naughty_string.count(vowel)

    if num_vowels < 3:
        return False

    # double_letter = False
    # for i in range(1, len(naughty_string)):

    #     if naughty_string[i] == naughty_string[i-1]:
    #         double_letter = True
    #         break

    # more efficient, I didn't know zip can be used with differetn # of elements
    double_letter = any(a == b for a, b in zip(naughty_string, naughty_string[1:]))

    return double_letter

def is_it_nice_v2(naughty_string):

    # double_pair = False
    # for i in range(len(naughty_string)-2):

    #     letters_check = naughty_string[i:i+2]
    #     remaining_string = naughty_string[0:i] + naughty_string[i+2:]
    #     if letters_check in remaining_string:
    #         double_pair = True
    #         break 

    # more efficient, I don't need to check the left part of string ... that was done already!
    double_pair = any(naughty_string[i:i+2] in naughty_string[i+2:] for i in range(len(naughty_string)-1))

    # its really double letter with space in between
    double_letter = any(a == b for a, b in zip(naughty_string, naughty_string[2:]))

    return double_pair and double_letter


# load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d5.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))


# ================= PART 1 ======================
test_cases = {'ugknbfddgicrmopn': True,
              'aaa': True,
              'jchzalrnumimnmhp': False,
              'haegwjzuvuyypxyu': False,
              'dvszwmarrgswjxmb': False}

for naughty_string, is_nice in test_cases.items():
    assert is_it_nice(naughty_string) == is_nice, f"the {naughty_string} did not match {is_nice}"

num_nice_strings = 0

for naughty_string in puzzle_input:
    num_nice_strings += is_it_nice(naughty_string)

print('Part 1 solution:', num_nice_strings)

# ================= PART 2 ======================
test_cases = {'qjhvhtzxzqqjkmpb': True,
              'xxyxx': True,
              'uurcxstgmygtbstg': False,
              'ieodomkazucvgmuy': False}

for naughty_string, is_nice in test_cases.items():
    assert is_it_nice_v2(naughty_string) == is_nice, f"the {naughty_string} did not match {is_nice}"

num_nice_strings = 0

for naughty_string in puzzle_input:
    num_nice_strings += is_it_nice_v2(naughty_string)

print('Part 2 solution:', num_nice_strings)

