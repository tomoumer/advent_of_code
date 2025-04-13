# Day 13 of 2017

# =========== CLASSES AND FUNCTIONS =============
def pass_through_security(firewalls_dict):
    # for first part ... each firewall be in the top position
    # again after (n-1) * 2 picoseconds, where n = range
    severity = 0
    
    # part 1
    for i in range(max(firewalls_dict)+1):

        # at a firewall location
        if i in firewalls_dict.keys():
            f_range = firewalls_dict[i]

            if i % ((f_range-1) * 2) == 0:
                severity += i * f_range

    # part 2
    for delay in range(1,10000000):
        caught = False

        for i in range(max(firewalls_dict)+1):

            # at a firewall location
            if i in firewalls_dict.keys():
                f_range = firewalls_dict[i]

                # basically any other position but 0 is fine
                if (i + delay) % ((f_range-1) * 2) == 0:
                    caught = True
                    break
        
        if not caught:

            return severity, delay

# =============== TEST CASES ====================
test_firewalls = ['0: 3',
'1: 2',
'4: 4',
'6: 4']

test_firewalls_dict = {}

for firewall in test_firewalls:
    f_depth, f_range = map(int, firewall.split(':'))
    test_firewalls_dict[f_depth] = f_range

assert pass_through_security(test_firewalls_dict) == (24, 10)

# =============== PART 1 & 2 ====================

firewalls_dict = {}

with open('./2017/inputs/d13.txt') as f:
    for row in f:
        f_depth, f_range = map(int, row.split(':'))
        firewalls_dict[f_depth] = f_range

severity, delay = pass_through_security(firewalls_dict)

print('Part 1 solution:', severity)
print('Part 2 solution:', delay)