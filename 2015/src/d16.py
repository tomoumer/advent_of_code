# Day 16 of 2015


gift_mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

aunt_suectionary = dict()

with open('./2015/inputs/d16.txt') as f:
    for j, row in enumerate(f):
        first_split = row.strip().split(',')
        for i, values in enumerate(first_split):
            if i == 0:
                sue_nr, compound_name, compound_nr = [x.strip() for x in values.split(':')]
                compound_nr = int(compound_nr)

                aunt_suectionary[sue_nr] = dict()
                aunt_suectionary[sue_nr][compound_name] = compound_nr

            else: # for values 2 and 3, still same sue
                compound_name, compound_nr = [x.strip() for x in values.split(':')]
                compound_nr = int(compound_nr)

                aunt_suectionary[sue_nr][compound_name] = compound_nr

# ================= PART 1 ======================

fake_sue = ''
correct_sue = ''

for sue, compounds in aunt_suectionary.items():
    possible_sue1 = True
    possible_sue2 = True
    for compound_name, compound_nr in compounds.items():

        if gift_mfcsam[compound_name] != compound_nr:
            possible_sue1 = False

        match compound_name:
            case ('cats') | ('trees'):
                # note that the compound_nr here is the value sue has
                if gift_mfcsam[compound_name] >= compound_nr:
                    possible_sue2 = False
            case 'goldfish':
                if gift_mfcsam[compound_name] <= compound_nr:
                    possible_sue2 = False
            case _:
                if gift_mfcsam[compound_name] != compound_nr:
                    possible_sue2 = False
        

    if possible_sue1:
        fake_sue = sue
    elif possible_sue2:
        correct_sue = sue


print('Part 1 solution:', int(fake_sue.split(' ')[1]))

# ================= PART 2 ======================

print('Part 2 solution:', int(correct_sue.split(' ')[1]))