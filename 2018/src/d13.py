# Day 13 of 2018

# =========== CLASSES AND FUNCTIONS =============
def find_carts(map_of_carts):

    carts = []

    for i, line in enumerate(map_of_carts):
        for j, char in enumerate(line):

            match char:
                case '<':
                    carts.append(['l', '+l', i, j])

                case '>':
                    carts.append(['r', '+l', i, j])

                case 'v':
                    carts.append(['d', '+l', i, j])

                case '^':
                    carts.append(['u', '+l', i, j])

                case _:
                    pass

        # once I have the carts, need to redraw the map to have the regular parts
        map_of_carts[i] = map_of_carts[i].replace('>', '-').replace('<', '-').replace('v', '|').replace('^', '|')

    return carts, map_of_carts


def move_carts_until_collision(carts, tracks, keep_coliding=False):

    first_collision = []

    while True:

        # carts need to move in order
        carts.sort(key=lambda x: (x[2],x[3]))
        collisions_found = []

        for cart_nr, cart in enumerate(carts):

            if cart_nr in collisions_found:
                continue

            # move based on current dir
            match cart[0]:
                case 'u':
                    cart[2] -= 1

                case 'd':
                    cart[2] += 1

                case 'l':
                    cart[3] -= 1

                case 'r':
                    cart[3] += 1

                case _:
                    pass

            # change dir        
            track_type = tracks[cart[2]][cart[3]]

            if track_type == '/':
                if cart[0] == 'd':
                    cart[0] = 'l'
                elif cart[0] == 'u':
                    cart[0] = 'r'
                elif cart[0] == 'l':
                    cart[0] = 'd'
                else: # 'r'
                    cart[0] = 'u'

            elif track_type == '\\':
                if cart[0] == 'd':
                    cart[0] = 'r'
                elif cart[0] == 'u':
                    cart[0] = 'l'
                elif cart[0] == 'l':
                    cart[0] = 'u'
                else: # 'r'
                    cart[0] = 'd'

            # move depends on previous
            elif track_type == '+':
                if cart[1] == '+l':
                    cart[1] = '+s'

                    if cart[0] == 'd':
                        cart[0] = 'r'
                    elif cart[0] == 'u':
                        cart[0] = 'l'
                    elif cart[0] == 'l':
                        cart[0] = 'd'
                    else: # 'r'
                        cart[0] = 'u'
                
                elif cart[1] == '+s':
                    # direction doesn't change here
                    cart[1] = '+r'
                
                else: # '+r'
                    cart[1] = '+l'

                    if cart[0] == 'd':
                        cart[0] = 'l'
                    elif cart[0] == 'u':
                        cart[0] = 'r'
                    elif cart[0] == 'l':
                        cart[0] = 'u'
                    else: # 'r'
                        cart[0] = 'd'

            # after EACH CART moves, check for collision
            carts_pos = [cart[2:] for cart in carts]

            for i, cart_pos in enumerate(carts_pos):
                if (i not in collisions_found) and (i != cart_nr) and (cart_pos == carts[cart_nr][2:]):
                    # print(collisions_found)

                    collisions_found.append(cart_nr)
                    collisions_found.append(i)


        if len(collisions_found) > 0:
            # part 1
            if not keep_coliding:
                return carts[collisions_found[0]]
            
            # part 2
            else:
                if len(first_collision) == 0:
                    first_collision = carts[collisions_found[0]]

                # need to delete in correct order to not mess up the indexing
                collisions_found.sort()
                for idx in collisions_found[::-1]:
                    carts.pop(idx)

                # reset for next round
                collisions_found = []

                # print('carts', carts)
                if len(carts) == 1:
                    return first_collision, carts[0]




# =============== TEST CASES ====================
map_of_carts = [
'/->-\         ', 
'|   |  /----\ ',
'| /-+--+-\  | ',
'| | |  | v  | ',
'\-+-/  \-+--/ ',
'  \------/    '
]

carts, tracks = find_carts(map_of_carts)
crash_pos = move_carts_until_collision(carts, tracks)
assert [crash_pos[3], crash_pos[2]] == [7,3] 

map_of_carts = [
'/>-<\   ',
'|   |   ',
'| /<+-\ ',
'| | | v ',
'\>+</ | ',
'  |   ^ ',
'  \<->/ '
]

carts, tracks = find_carts(map_of_carts)
_, final_pos = move_carts_until_collision(carts, tracks, keep_coliding=True)
assert [final_pos[3], final_pos[2]] == [6,4] 
    

# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2018/inputs/d13.txt') as f:
    for row in f:
        puzzle_input.append(row.replace('\n',''))


carts, tracks = find_carts(puzzle_input)
crash_pos, final_pos = move_carts_until_collision(carts, tracks, keep_coliding=True)

print(f'Part 1 solution: {crash_pos[3]},{crash_pos[2]}')
print(f'Part 2 solution: {final_pos[3]},{final_pos[2]}')