# Day 8 of 2015
import re

# =========== CLASSES AND FUNCTIONS =============
def calc_string_vals(string):
    str_len =  len(string)

    num_esc = len(re.findall(r'\\"' , string))
    num_hex = len(re.findall(r'\\x[0-9a-f]{2}', string))
    # NOTE: this one was messing me up ... initially I excluded just x
    # problem is there were some like \xaw, which is not hex
    num_bks = len(re.findall(r'\\\\(?!x[0-9a-f]{2})(?!")',string))
    # 2 is for beginning and end " "
    mem_len = str_len - 2 - num_bks - num_esc - 3* num_hex

    # part 2
    new_len = str_len + 4 + 2*num_bks + 2*num_esc + num_hex

    return (str_len, mem_len, new_len)

# =============== TEST CASES ====================
test_cases = {'""': (2, 0, 6),
              '"abc"': (5, 3, 9),
              r'"aaa\"aaa"': (10, 7, 16),
              r'"\x27"': (6, 1, 11)}

for string, lengths in test_cases.items():

    assert calc_string_vals(string) == lengths, f"the {string} did not match {lengths}"

# =============== PART 1 & 2 ====================
tot_str_len = 0
tot_mem_len = 0
new_enc_len = 0

with open('./2015/inputs/d8.txt') as f:
    for j, row in enumerate(f):

        (tmp_str, tmp_mem, tmp_new) = calc_string_vals(row.strip()) 
        # print(tmp_str, tmp_mem)
        tot_str_len += tmp_str
        tot_mem_len += tmp_mem
        new_enc_len += tmp_new

print('Part 1 solution:', tot_str_len - tot_mem_len)
print('Part 2 solution:', new_enc_len - tot_str_len)