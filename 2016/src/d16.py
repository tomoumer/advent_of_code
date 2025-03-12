# Day 16 of 2016

# =========== CLASSES AND FUNCTIONS =============
def fill_disk(data, disk_size):

    while len(data) < disk_size:
        data_rev = data[::-1]
        data_rev = ''.join(['0' if chr == '1' else '1' for chr in data_rev])

        data = data + '0' + data_rev

    # truncate unneccessary right here
    return data[:disk_size]

def checksum(filled_data):

    while len(filled_data) % 2 == 0:
        tmp_data = ''
        for i in range(0, len(filled_data), 2):
            if filled_data[i] == filled_data[i+1]:
                tmp_data = tmp_data + '1'
            else:
                tmp_data = tmp_data + '0'

        filled_data = tmp_data

    return filled_data
    

# =============== TEST CASES ====================
# NOTE: these won't work anymore, only had them to test first step
# assert fill_disk('1') == '100'
# assert fill_disk('0') == '001'
# assert fill_disk('11111') == '11111000000'
# assert fill_disk('111100001010') == '1111000010100101011110000'

test_initial = '10000'
test_filled = fill_disk('10000', 20)
assert test_filled == '10000011110010000111'
assert checksum(test_filled) == '01100'


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d16.txt') as f:
    for row in f:
        initial_data = row

filled_data_1 = fill_disk(initial_data, 272)
final_checksum_1 = checksum(filled_data_1)

filled_data_2 = fill_disk(initial_data, 35651584)
final_checksum_2 = checksum(filled_data_2)

print('Part 1 solution:', final_checksum_1)
print('Part 2 solution:', final_checksum_2)