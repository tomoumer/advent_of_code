# Day 7 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
def check_abba(ip_string_list):
    abba = False
    # need to check all the separate ip locations
    for ip_string in ip_string_list:
        for i in range(0, len(ip_string)-2):
            if (ip_string[i] != ip_string[i+1]) and (ip_string[i:i+2] == ip_string[i+3:i+1:-1]):
                abba = True
                break

        # exit out of both loops
        if abba:
            break

    return abba

def check_ababab(outside_ip_list, inside_ip_list):
    ababab = False
    # there could be more than 1
    bab_candidates = []

    # need to check all the separate ip locations
    for ip_string in outside_ip_list:
        for i in range(0, len(ip_string)-2):
            if (ip_string[i] != ip_string[i+1]) and (ip_string[i] == ip_string[i+2]):
                bab_candidates.append(ip_string[i+1] + ip_string[i] + ip_string[i+1])

    # need to check if any of the bab candidates appear in any of the 
    for bab in bab_candidates:
        for ip_string in inside_ip_list:
            if bab in ip_string:
                ababab = True
                break

        if ababab:
            break

    return ababab

def support_status(full_ip):
    outside_bracket_ip = []
    # beginning
    begin_ip = re.search('^[a-zA-Z]+', full_ip).group()
    outside_bracket_ip.append(begin_ip)

    # middle
    mid_ip = re.findall('\]([a-zA-Z]+)\[', full_ip)
    outside_bracket_ip.extend(mid_ip)

    # end
    end_ip =  re.search('[a-zA-Z]+$', full_ip).group()
    outside_bracket_ip.append(end_ip)

    # between brackets
    bracket_ip = re.findall('\[([a-zA-Z]+)\]', full_ip)

    # do the checks
    abba_outside = check_abba(outside_bracket_ip)
    abba_inside = check_abba(bracket_ip)
    support_abba = abba_outside and not abba_inside

    support_ababab = check_ababab(outside_bracket_ip, bracket_ip)

    return support_abba, support_ababab

# =============== TEST CASES ====================
test_ips = {'abba[mnop]qrst': True,
            'abcd[bddb]xyyx': False,
            'aaaa[qwer]tyui': False,
            'ioxxoj[asdfgh]zxcvbn': True}

for test_ip, is_valid in test_ips.items():
    assert support_status(test_ip)[0] == is_valid

test_ips = {'aba[bab]xyz': True,
            'xyx[xyx]xyx': False,
            'aaa[kek]eke': True,
            'zazbz[bzb]cdb': True}

for test_ip, is_valid in test_ips.items():
    assert support_status(test_ip)[1] == is_valid

# =============== PART 1 & 2 ====================
all_ips = []

with open('./2016/inputs/d7.txt') as f:
    for row in f:
        all_ips.append(row.strip())

support_tls = 0
support_ssl = 0
for ip in all_ips:
    current_tls, current_ssl = support_status(ip)
    support_tls += current_tls
    support_ssl += current_ssl

print('Part 1 solution:', support_tls)
print('Part 2 solution:', support_ssl)