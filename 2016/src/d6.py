# Day 6 of 2016
from collections import Counter

# =========== CLASSES AND FUNCTIONS =============
# basically to go from horizontal to vertical
def format_messages(original_messages):
    formatted_messages = dict()

    for msg in original_messages:

        for i, letter in enumerate(msg):
            if i not in formatted_messages.keys():
                formatted_messages[i] = []
            formatted_messages[i].append(letter)

    return formatted_messages

# extract error corrected message
def extract_ecm(formatted_messages):
    ecm_max = ''
    ecm_min = ''
    for i, (key, value) in enumerate(formatted_messages.items()):
        # extra sanity check just to make sure dictionary wasn't stored in weird order
        assert i == key
        letter_dict = Counter(''.join(value)) # count how many times each letter appears
        max_letter = max(letter_dict, key=letter_dict.get)
        min_letter = min(letter_dict, key=letter_dict.get)

        ecm_max = ecm_max + max_letter
        ecm_min = ecm_min + min_letter

    return ecm_max, ecm_min

# =============== TEST CASES ====================
test_messages = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""

test_messages = test_messages.strip().split('\n')

# need to go to vertical msg
test_formatted_messages = format_messages(test_messages)
test_ecm_max, test_ecm_min = extract_ecm(test_formatted_messages)

assert test_ecm_max == 'easter'
assert test_ecm_min == 'advent'


# =============== PART 1 & 2 ====================
messages = []

with open('./2016/inputs/d6.txt') as f:
    for row in f:
        messages.append(row.strip())

formatted_messages = format_messages(messages)
ecm_max, ecm_min = extract_ecm(formatted_messages)

print('Part 1 solution:', ecm_max)
print('Part 2 solution:', ecm_min)