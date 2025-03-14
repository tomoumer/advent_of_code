# Day 17 of 2016
# NOOOO I'M GOING TO DREAM OF HASHES!
import hashlib
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
def get_open_doors(string, x, y):
    # print(string, x, y)

    encoded_string = string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string)
    hex_digest = md5_hash.hexdigest()

    # DOORS ARE CASE SENSITIVE (hash is diffferent)
    open_doors = ''
    if (y > 0) and (hex_digest[0] in ['b', 'c', 'd', 'e', 'f']):
        open_doors = open_doors + 'U'
    if (y < 3) and (hex_digest[1] in ['b', 'c', 'd', 'e', 'f']):
        open_doors = open_doors + 'D'
    if (x > 0) and (hex_digest[2] in ['b', 'c', 'd', 'e', 'f']):
        open_doors = open_doors + 'L'
    if (x < 3) and (hex_digest[3] in ['b', 'c', 'd', 'e', 'f']):
        open_doors = open_doors + 'R'    

    return open_doors

# this reminds me of going through the map like those turn based rhythm games!
def move_and_groove(start_pwd, x, y):
    fastest_path = 'a' * 1000
    longest_path = 0

    open_doors = get_open_doors(start_pwd, x, y)

    queue = deque()
    for open_door in open_doors:
        queue.append([start_pwd, x, y, open_door])

    while queue:

        current_pwd, x, y, open_door = queue.popleft()

        current_pwd = current_pwd + open_door
        
        match open_door:
            case 'U':
                y -= 1
            case 'D':
                y += 1
            case 'L':
                x -= 1
            case 'R':
                x += 1
            case _:
                raise ValueError('unrecognized door!')
            
        # vault
        if (x == 3) and (y == 3):
            if len(fastest_path) > len(current_pwd):
                fastest_path = current_pwd
            else:
                longest_path = max(longest_path, len(current_pwd[len(start_pwd):]))
            continue    
            
        open_doors = get_open_doors(current_pwd, x, y)

        # wops, locked myself in a corner!
        if len(open_doors) == 0:
            continue

        for open_door in open_doors:
            queue.append([current_pwd, x, y, open_door])

    # remove the initial pwd from path
    return fastest_path[len(start_pwd):], longest_path

            
# =============== TEST CASES ====================
x = 0
y = 0

assert move_and_groove('ihgpwlah', x, y) == ('DDRRRD', 370)
# print(move_and_groove('kglvqrro', x, y))
assert move_and_groove('kglvqrro', x, y) == ('DDUDRLRRUDRD', 492)
assert move_and_groove('ulqzkmiv', x, y) == ('DRURDRUDDLLDLUURRDULRLDUUDDDRR', 830)


# =============== PART 1 & 2 ====================

with open('./2016/inputs/d17.txt') as f:
    for row in f:
        start_pwd = row.strip()

shortest_path, longest_len = move_and_groove(start_pwd, x, y)

print('Part 1 solution:', shortest_path)
print('Part 2 solution:', longest_len)