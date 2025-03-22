# Day 9 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
def find_matches(match_string):
    matches = re.finditer('\((\d+)x(\d+)\)', match_string)
    marker_list = []
    all_marker_effect = []
    overlap_pos = -1

    for match in matches:
        # for pt 2. just mark when each marker begins and ends (index) and its multiplier
        all_marker_effect.append([match.end(),  match.end() + int(match.group(1)), int(match.group(2))])
        
        if match.start() > overlap_pos:
            marker_list.append([int(match.group(1)), int(match.group(2)), match.start(), match.end()])
            overlap_pos = match.end() - 1 + int(match.group(1))
            # print(match.group(1), match.group(2), match.start(), match.end(), overlap_pos)

    # print(all_marker_effect)
    return marker_list, all_marker_effect


def decompress(match_string, marker_list, all_marker_effect):
    decompressed = len(match_string)


    for marker in marker_list:

        num_char = marker[0]
        num_repeat = marker[1]
        marker_start = marker[2]
        marker_end = marker[3]

        # each marker length is given by end - start
        decompressed -= (marker_end- marker_start)
        # here we subtract 1 because we'll just be adding and not removing existing ones
        # otherwise, we could remove the len of marker[0] first 
        decompressed += num_char * (num_repeat -1)


    # part 2
    all_marker_effect
    matches = re.finditer('[A-Z]', match_string)
    decompressed_v2 = 0

    for match in matches:
        letter_index = match.start()
        multiplier = 1

        # the logic here is that if the letter is found within the "reach" of a decompression 
        # that's going to repeat the letter. And if another decompressor comes along, those decompressors multiply
        for marker in all_marker_effect:
            if (letter_index >= marker[0]) and (letter_index < marker[1]):
                multiplier *= marker[2]

        decompressed_v2 += multiplier


    return decompressed, decompressed_v2

# =============== TEST CASES ====================

test_strings = {'ADVENT': 6,
                'A(1x5)BC': 7,
                '(3x3)XYZ': 9,
                'A(2x2)BCD(2x2)EFG': 11,
                '(6x1)(1x3)A': 6,
                'X(8x2)(3x3)ABCY': 18}

for test_string, test_len in test_strings.items():
    test_marker, test_marker_effect = find_matches(test_string)
    assert decompress(test_string, test_marker, test_marker_effect)[0] == test_len

test_strings2 = {'(3x3)XYZ': 9, 
                'X(8x2)(3x3)ABCY': 20,
                '(27x12)(20x12)(13x14)(7x10)(1x12)A': 241920,
                '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN ': 445
} 

for test_string, test_len in test_strings2.items():
    test_marker, test_marker_effect = find_matches(test_string)
    assert decompress(test_string, test_marker, test_marker_effect)[1] == test_len


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d9.txt') as f:
    for row in f:
        mystery_string = row.strip()


marker, all_marker_effect = find_matches(mystery_string)
final_len, final_len_2 = decompress(mystery_string, marker, all_marker_effect)

print('Part 1 solution:', final_len)
print('Part 2 solution:', final_len_2)
