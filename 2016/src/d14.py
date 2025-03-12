# Day 14 of 2016
import hashlib
import re

# =========== CLASSES AND FUNCTIONS =============
def get_md5_hex(string):

    encoded_string = string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    hex_digest = md5_hash.hexdigest()

    return hex_digest

def check_triple_quintuple(i, triplets, hex_repr, num_keys_found):
    # only consider FIRST such triplet!
    # find_triple = re.findall(r'([a-f0-9])\1\1', hex_repr)
    find_triple = re.search(r'([a-f0-9])\1\1', hex_repr)

    if find_triple:

        find_triple = find_triple.group(1)
        
        find_quintuple = re.findall(r'([a-f0-9])\1\1\1\1', hex_repr)
        if len(find_quintuple) > 0:

            for quintuple in find_quintuple:
                del_found_matches = []
                for idx, triplet in triplets.items():
                    if quintuple == triplet:
                        num_keys_found += 1
                        # NEED TO DELETE FOUND TRIPLE MATCH!!!
                        del_found_matches.append(idx)

                        if num_keys_found == 64:
                            return idx, num_keys_found
                        
                for idx in del_found_matches:
                    del triplets[idx]

        triplets[i] = find_triple

    return 0, num_keys_found

def find_one_time_pads(salt):
    triplets_base = dict()
    triplets_adv = dict()
    # quintuplets_base = dict()
    # quintuplets_adv = dict()

    num_keys_base = 0
    num_keys_adv = 0

    for i in range(100000000):
        if len(triplets_base) > 0:
            while i - min(triplets_base) > 1000:
                # only keep relevant values as idx keeps increasing
                del triplets_base[min(triplets_base)]

        if len(triplets_adv) > 0:
            while i - min(triplets_adv) > 1000:
                # only keep relevant values as idx keeps increasing
                del triplets_adv[min(triplets_adv)]
                if len(triplets_adv) == 0:
                    break

        hex_repr = get_md5_hex(salt + f'{i}')
        hex_repr_adv = hex_repr
        for j in range(2016):
            hex_repr_adv = get_md5_hex(hex_repr_adv)

        if num_keys_base != 64:
            idx_base, num_keys_base = check_triple_quintuple(i, triplets_base, hex_repr, num_keys_base)

        if num_keys_adv != 64:
            idx_adv, num_keys_adv = check_triple_quintuple(i, triplets_adv, hex_repr_adv, num_keys_adv)

        if (idx_base != 0) and (idx_adv != 0):
            return idx_base, idx_adv


# =============== TEST CASES ====================

idx_pt1, idx_pt2 = find_one_time_pads('abc')
assert idx_pt1 == 22728
assert idx_pt2 == 22551


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d14.txt') as f:
    for row in f:
        puzzle_base = row.strip()


key_pt1, key_pt2 = find_one_time_pads(puzzle_base)

print('Part 1 solution:', key_pt1)
print('Part 2 solution:', key_pt2)