# Day 10 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
class Rumba:

    def __init__(self, chips, val_low, val_high):
        self.chips = chips
        self.val_low = val_low
        self.val_high = val_high

    def add_chip(self, chip):
        self.chips.append(chip)

        outputs = []

        if len(self.chips) == 2:
            if 'bot' in self.val_low:
                outputs.append([min(self.chips), self.val_low[1]])
            if 'bot' in self.val_high:
                outputs.append([max(self.chips), self.val_high[1]])

        return outputs

def allocate_bots(instructions):
    bots = dict()

    giving_values = []
    for instruction in instructions:
        if 'gives' in instruction:
            # this will create bots
            bot1, out1, out2 = [(type, int(val)) for type, val in re.findall('(bot|output) (\d+)', instruction)]
            bots[bot1[1]] = Rumba([], out1, out2)
        # for later, that will initiate giving
        else:
            giving_values.append(instruction)

    # the giving part
    transfer_outputs = []
    for give_val in giving_values:

        # initiate the transfer of values - this could start a cascade
        val, bot_nr = list(map(int, re.findall('\d+', give_val)))

        transfer_outputs.append([val, bot_nr])

        while len(transfer_outputs) > 0:

            next_val, next_bot = transfer_outputs.pop()

            transfer_outputs.extend(bots[next_bot].add_chip(next_val))

    return bots

# =============== TEST CASES ====================
test_instructions = [
'value 5 goes to bot 2',
'bot 2 gives low to bot 1 and high to bot 0',
'value 3 goes to bot 1',
'bot 1 gives low to output 1 and high to bot 0',
'bot 0 gives low to output 2 and high to output 0',
'value 2 goes to bot 2'
]

test_bots = allocate_bots(test_instructions)

# I am too lazy to do all the different assert statements here ... a print will suffice
# for i in range(3):
#     print(test_bots[i].chips, test_bots[i].val_low, test_bots[i].val_high)


# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2016/inputs/d10.txt') as f:
    for row in f:
        puzzle_input.append(row)


bots = allocate_bots(puzzle_input)

multiplier = 1

for i in range(max(bots.keys())):
    if (min(bots[i].chips) == 17) and (max(bots[i].chips) == 61):
        comparison_bot = i

    if ('output' in bots[i].val_low) and (bots[i].val_low[1] in [0,1,2]):
        multiplier *= min(bots[i].chips)

    elif ('output' in bots[i].val_high) and (bots[i].val_high[1] in [0,1,2]):
        multiplier *= max(bots[i].chips)
    
print('Part 1 solution:', comparison_bot)
print('Part 2 solution:', multiplier)