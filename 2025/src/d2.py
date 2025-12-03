# Day 2 of 2025

# =========== CLASSES AND FUNCTIONS =============
def extract_range(id_range):

    extracted_ranges = []

    for id_pair in id_range.split(','):

        id_start, id_end = map(int, id_pair.strip().split('-'))

        # need to add +1 to be inclusive
        extracted_range = list(range(id_start, id_end+1))

        extracted_ranges.extend(extracted_range)
    
    return extracted_ranges

def check_invalid_id(extracted):

    sum_pt1 = 0
    sum_pt2 = 0

    for id_num in extracted:

        id_str = str(id_num)

        mid_point = len(id_str) // 2

        if id_str[:mid_point] == id_str[mid_point:]:
            sum_pt1 += id_num
            sum_pt2 += id_num

        # check for multiple repeats
        else:
            for i in range(1, mid_point+1):
                # if multiple of the subset can fit in the word
                # i.e. if a word of 9 letters can fit 3x3
                if len(id_str) % len(id_str[:i]) == 0:
                    multi_factor = len(id_str) // len(id_str[:i]) 

                    if id_str[:i] * multi_factor == id_str:
                        sum_pt2 += id_num
                        break

    return sum_pt1, sum_pt2

# =============== TEST CASES ====================
test_digits = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

test_ranges = extract_range(test_digits)
test_sum1, test_sum2 = check_invalid_id(test_ranges)

assert test_sum1 == 1227775554
print(test_sum2)
assert test_sum2 == 4174379265

# =============== PART 1 & 2 ====================

with open('./2025/inputs/d2.txt') as f:
    for row in f:
        puzzle_input = row.strip()

id_ranges = extract_range(puzzle_input)
fake_id_sum1, fake_id_sum2 = check_invalid_id(id_ranges)

print('Part 1 solution:', fake_id_sum1)
print('Part 2 solution:', fake_id_sum2)