# Day 5 of 2016
import hashlib

# =========== CLASSES AND FUNCTIONS =============
def get_md5_hex(string):

    encoded_string = string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    hex_digest = md5_hash.hexdigest()

    return hex_digest

def find_password(string, num_zeros=5):
    i = 1
    pwd = ''
    pwd2 = [0, 0, 0, 0, 0, 0, 0, 0]
    while (len(pwd) < 8) or (0 in pwd2):
        hex_digest = get_md5_hex(string + str(i))
        if (num_zeros == 5) & (hex_digest[:5] == '00000'):

            if (len(pwd) < 8):
                pwd = pwd + hex_digest[5]

            # 6th character is position, also verify that it's not been filled in yet
            try:
                pos_digit = int(hex_digest[5])
                if (pos_digit <= 7) and (pwd2[pos_digit] == 0):
                    pwd2[pos_digit] = hex_digest[6]
            except:
                pass # the pos_digit is not an int
   
        i += 1

    # to make it a string instad of a list
    pwd2 = ''.join(pwd2)
    return pwd, pwd2

# =============== TEST CASES ====================
test_pwd1, test_pwd2 = find_password('abc')
assert test_pwd1 == '18f47a30'
assert test_pwd2 == '05ace8e3'

# =============== PART 1 & 2 ====================

with open('./2016/inputs/d5.txt') as f:
    for row in f:
        door_id = row.strip()

first_password, second_password = find_password(door_id)

print('Part 1 solution:', first_password)
print('Part 2 solution:', second_password)