# Day 14 of 2018

# =========== CLASSES AND FUNCTIONS =============
def next_recipe(elf1, elf2, scores):

    total_score = scores[elf1] + scores[elf2]

    if total_score >= 10:
        score1 = 1
        score2 = total_score % 10
        scores.extend([score1, score2])

    else:
        scores.append(total_score)

    # the move is 1 plus current recipe (scores[elf1])
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores)

    return elf1, elf2, scores

def cycle_recipes(elf1, elf2, scores, num_cycles):

    for i in range(num_cycles + 10):

        elf1, elf2, scores = next_recipe(elf1, elf2, scores)

    return scores



# =============== TEST CASES ====================
scores = [3, 7]
elf1 = 0
elf2 = 1

scores = cycle_recipes(elf1, elf2, scores, 2018)
assert ''.join(map(str, (scores[9:19]))) == '5158916779' 
assert ''.join(map(str, (scores[5:15]))) == '0124515891'
assert ''.join(map(str, (scores[18:28]))) == '9251071085'
assert ''.join(map(str, (scores[2018:2028]))) == '5941429882'

scores = ''.join(map(str, scores))
assert scores.find('51589') == 9
assert scores.find('01245') == 5
assert scores.find('92510') == 18
assert scores.find('59414') == 2018


# =============== PART 1 & 2 ====================
with open('./2018/inputs/d14.txt') as f:
    for row in f:
        num_cycles = int(row.strip())


scores = [3, 7]
elf1 = 0
elf2 = 1

scores = cycle_recipes(elf1, elf2, scores, num_cycles * 50)

print('Part 1 solution:', ''.join(map(str, (scores[num_cycles:num_cycles+10]))))

scores = ''.join(map(str, scores))

print('Part 2 solution:', scores.find(str(num_cycles)))