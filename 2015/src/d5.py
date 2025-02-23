# Day 5 of 2015

# =========== CLASSES AND FUNCTIONS =============
def is_it_nice(naughty_string):
    # these overwrite anything else
    if any(x in naughty_string for x in ('ab', 'cd', 'pq', 'xy')):
        return False
    
    num_vowels = 0
    for vowel in 'aeiou':
        num_vowels += naughty_string.count(vowel)
        
    if num_vowels < 3:
        return False

    # more efficient, I didn't know zip can be used with different # of elements
    double_letter = any(a == b for a, b in zip(naughty_string, naughty_string[1:]))

    return double_letter

def is_it_nice_v2(naughty_string):

    # more efficient, I don't need to check the left part of string ... that was done already!
    double_pair = any(naughty_string[i:i+2] in naughty_string[i+2:] for i in range(len(naughty_string)-1))

    # its really double letter with space in between
    double_letter = any(a == b for a, b in zip(naughty_string, naughty_string[2:]))

    return double_pair and double_letter

# =============== TEST CASES ====================
test_cases = {'ugknbfddgicrmopn': True,
              'aaa': True,
              'jchzalrnumimnmhp': False,
              'haegwjzuvuyypxyu': False,
              'dvszwmarrgswjxmb': False}

for naughty_string, is_nice in test_cases.items():
    assert is_it_nice(naughty_string) == is_nice

test_cases = {'qjhvhtzxzqqjkmpb': True,
              'xxyxx': True,
              'uurcxstgmygtbstg': False,
              'ieodomkazucvgmuy': False}

for naughty_string, is_nice in test_cases.items():
    assert is_it_nice_v2(naughty_string) == is_nice


# ================= PART 1 ======================
all_strings = []

with open('./2015/inputs/d5.txt') as f:
    for row in f:
        all_strings.append(row.strip())

num_nice_strings = 0

for naughty_string in all_strings:
    num_nice_strings += is_it_nice(naughty_string)

print('Part 1 solution:', num_nice_strings)

# ================= PART 2 ======================

num_nice_strings = 0

for naughty_string in all_strings:
    num_nice_strings += is_it_nice_v2(naughty_string)

print('Part 2 solution:', num_nice_strings)

