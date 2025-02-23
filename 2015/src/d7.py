# Day 7 of 2015
import re

# =========== CLASSES AND FUNCTIONS =============
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def process_match(match, result, match_type=''):
    global all_equations
    global solved_equations

    if match_type in ['direct', 'left_shift', 'right_shift']:
        if is_integer(match[1]):
            result_calc = int(match[1]) 
        elif match[1] in solved_equations.keys():
            result_calc = solved_equations[match[1]]
        else:
            process_logic(all_equations[match[1]], match[1])
            result_calc = solved_equations[match[1]]

        if match_type == 'direct':
            solved_equations[result] = result_calc

        elif match_type == 'left_shift':
            solved_equations[result] = result_calc << int(match[2])

        elif match_type == 'right_shift':
            solved_equations[result]  = result_calc >> int(match[2])
    
    if match_type == 'not':
        if is_integer(match[1]):   # because the input is 16 bit, need to truncate
            result_calc = ~int(match[1]) & 0xffff
        elif match[1] in solved_equations.keys():
            result_calc = ~solved_equations[match[1]] & 0xffff
        else:
            process_logic(all_equations[match[1]], match[1])
            result_calc = ~solved_equations[match[1]] & 0xffff
        
        solved_equations[result]  = result_calc & 0xffff

    if match_type in ['and', 'or']:
        if is_integer(match[1]):
            result_calc1 = int(match[1])
        elif match[1] in solved_equations.keys():
            result_calc1 = solved_equations[match[1]]
        else:
            process_logic(all_equations[match[1]], match[1])
            result_calc1 = solved_equations[match[1]]

        if is_integer(match[2]):
            result_calc2 = int(match[2])
        elif match[2] in solved_equations.keys():
            result_calc2 = solved_equations[match[2]]
        else:
            process_logic(all_equations[match[2]], match[2])
            result_calc2 = solved_equations[match[2]]     

        if match_type == 'and':
            solved_equations[result] = (result_calc1 & result_calc2) & 0xffff 

        elif match_type == 'or':
            solved_equations[result] = result_calc1 | result_calc2

def process_logic(operation, result):
    global all_equations
    global solved_equations

    # there are different possibilities ..
    # direct number (or letters) assignment:
    match = re.search('^([a-zA-Z0-9]+)$', operation)
    if match != None:
        process_match(match, result, 'direct')
        return
    
    # LEFT SHIFT
    match = re.search('([a-zA-Z0-9]+) LSHIFT (\d+)', operation)
    if match != None:
        process_match(match, result, 'left_shift')
        return        

    # RIGHT SHIFT
    match = re.search('([a-zA-Z0-9]+) RSHIFT (\d+)', operation)
    if match != None:
        process_match(match, result, 'right_shift')
        return            
    
    # NOT
    match = re.search('NOT ([a-zA-Z0-9]+)', operation)
    if match != None:
        process_match(match, result, 'not')
        return                
        
    # AND
    match = re.search('([a-zA-Z0-9]+) AND ([a-zA-Z0-9]+)', operation)
    if match != None:
        process_match(match, result, 'and')
        return  

    # OR
    match = re.search('([a-zA-Z0-9]+) OR ([a-zA-Z0-9]+)', operation)
    if match != None:
        process_match(match, result, 'or')
        return  

# =============== TEST CASES ====================
test_solutions = {'d': 72,
                  'e': 507,
                  'f': 492,
                  'g': 114,
                  'h': 65412,
                  'i': 65079,
                  'x': 123,
                  'y': 456}

test_circuit = """
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i
"""

all_equations = dict()
solved_equations = dict()

for line in test_circuit.strip().split('\n'):
    operation, result = line.split('->')

    all_equations[result.strip()] = operation.strip()

for result in ['x','y', 'd', 'e', 'f', 'g', 'h', 'i']:
    process_logic(all_equations[result], result)

assert solved_equations == test_solutions

# ================= PART 1 ======================
solved_equations = dict()
all_equations = dict()

with open('./2015/inputs/d7.txt') as f:
    for row in f:
        operation, result = row.split('->')

        # to make sure that multiple equations don't lead to same key
        assert result not in all_equations

        all_equations[result.strip()] = operation.strip()

process_logic(all_equations['a'], 'a')

print('Part 1 solution:', solved_equations['a'])

# ================= PART 2 ======================
new_b = solved_equations['a']

# needs reset
solved_equations = dict()
all_equations['b'] = str(new_b)
solved_equations['b'] = new_b

process_logic(all_equations['a'], 'a')

print('Part 2 solution:', solved_equations['a'])