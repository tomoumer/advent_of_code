# Day 1 of 2015

# =========== CLASSES AND FUNCTIONS =============
class Santa:
    def __init__(self, floor=0, basement=0):
        self.floor = floor
        self.basement = basement

    def change_floor(self, direction):
        if direction == '(':
            self.floor += 1
        elif direction == ')':
            self.floor -= 1
        else:
            print('santa is confused with the directions ...')

    def process_instructions(self, instructions):
        self.reset()

        for i, instruction in enumerate(instructions):
            self.change_floor(instruction)

            # mark the arrival in basement for the first time
            if (self.floor == -1) & (self.basement == 0):
                self.basement = i+1

    def reset(self, floor=0, basement=0):
        self.floor = floor
        self.basement = basement

# =============== TEST CASES ====================

# test 1
test_santa = Santa(0,0)

test_cases = {'(())': 0,
              '()()': 0,
              '(((': 3,
              '(()(()(': 3,
              '())': -1,
              '))(': -1,
              ')))': -3,
              ')())())': -3}

for test_directions, final_floor in test_cases.items():
    test_santa.process_instructions(test_directions)
    assert test_santa.floor == final_floor

# test 2
test_cases = {')': 1,
              '()())': 5}

for test_directions, basement_location in test_cases.items():
    test_santa.process_instructions(test_directions)
    assert test_santa.basement == basement_location

# ================= PART 1 ======================

santa = Santa(0, 0)
directions = []

with open('./2015/inputs/d1.txt') as f:
    for row in f:
        directions = row.strip()

santa.process_instructions(directions)
print('Part 1 solution:', santa.floor)

# ================= PART 2 ======================

santa.process_instructions(directions)
print('Part 2 solution:', santa.basement)
