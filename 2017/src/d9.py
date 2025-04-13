# Day 9 of 2017

# =========== CLASSES AND FUNCTIONS =============
def swim_the_stream(char_stream):
    i=0
    group_nr = 0
    total_score = 0
    garbage = False

    cleaned_garbage = 0

    while i < len(char_stream):

        char = char_stream[i]

        # this one canceles next regardless if it's in a group or garbage
        if char == '!':
            i += 2
            continue

        # logic to conclude garbage
        if garbage:
            if char == '>':
                garbage = False
            else:
                cleaned_garbage += 1
  
            i += 1
            continue
        
        # only get here if it's not ! or open garbage
        if char == '{':
            group_nr += 1
            total_score += group_nr
        elif char == '}':
            group_nr -= 1
        elif char == '<':
            garbage = True

        i += 1

    return total_score, cleaned_garbage

# =============== TEST CASES ====================
test_streams = {'{}': 1,
                '{{{}}}': 6,
                '{{},{}}': 5,
                '{{{},{},{{}}}}': 16,
                '{<a>,<a>,<a>,<a>}': 1,
                '{{<ab>},{<ab>},{<ab>},{<ab>}}': 9,
                '{{<!!>},{<!!>},{<!!>},{<!!>}}': 9,
                '{{<a!>},{<a!>},{<a!>},{<ab>}}': 3}

for stream, score in test_streams.items():

    assert swim_the_stream(stream)[0] == score

# =============== PART 1 & 2 ====================

with open('./2017/inputs/d9.txt') as f:
    for row in f:
        char_stream = row

score, cleaned_garbage = swim_the_stream(char_stream)

print('Part 1 solution:', score)
print('Part 2 solution:', cleaned_garbage)