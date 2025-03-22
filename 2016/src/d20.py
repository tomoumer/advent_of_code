# Day 20 of 2016

# =========== CLASSES AND FUNCTIONS =============
def find_available_ip(blocked_ip):

    max_int = 4294967295
    min_ip = 0
    first_min_ip = -1

    blocked_ip = sorted(blocked_ip, key=lambda x: x[0])

    num_available = 0
    for ip_range in blocked_ip:

        # it only needs to be touching
        if ip_range[0] <= min_ip:
            min_ip = max(min_ip, ip_range[1] + 1)
        else:
            if first_min_ip == -1:
                first_min_ip = min_ip
            
            num_available += (ip_range[0] - min_ip)
            min_ip = ip_range[1] + 1

    # the very last interval, if not covered
    if min_ip < max_int:
        num_available += (max_int - min_ip)

    return first_min_ip, num_available
    
# =============== TEST CASES ====================
test_ip_ranges = ['5-8',
'0-2',
'4-7']

test_blocked_ip = []

for ip in test_ip_ranges:
    ip_start, ip_end = map(int, ip.split('-'))
    test_blocked_ip.append([ip_start, ip_end])

min_ip, num_available = find_available_ip(test_blocked_ip)
assert min_ip == 3

# =============== PART 1 & 2 ====================
blocked_ip = []

with open('./2016/inputs/d20.txt') as f:
    for row in f:
        ip_start, ip_end = map(int,row.split('-'))
        blocked_ip.append([ip_start, ip_end])


min_ip, num_available = find_available_ip(blocked_ip)

print('Part 1 solution:', min_ip)
print('Part 2 solution:', num_available)