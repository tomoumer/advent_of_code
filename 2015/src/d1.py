# Day 1 of 2015

class Santa:
    def __init__(self, floor, basement):
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
        for i, instruction in enumerate(instructions):
            self.change_floor(instruction)

            # mark the arrival in basement
            if (self.floor == -1) & (self.basement == 0):
                self.basement = i+1

    def reset(self, floor, basement):
        self.floor = floor
        self.basement = basement

# load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d1.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

# print('number of rows in input', len(puzzle_input))    

# initiate santa to start with
santa = Santa(0, 0)

# ================= PART 1 ======================
test_cases = {'(())': 0,
              '()()': 0,
              '(((': 3,
              '(()(()(': 3,
              '())': -1,
              '))(': -1,
              ')))': -3,
              ')())())': -3}

for instructions, final_floor in test_cases.items():
    santa.reset(0, 0)
    santa.process_instructions(instructions)
    assert santa.floor == final_floor, f"the {instructions} did not match {final_floor}"

santa.reset(0, 0)
santa.process_instructions(puzzle_input[0])
print('Part 1 solution:', santa.floor)


# ================= PART 2 ======================

test_cases = {')': 1,
              '()())': 5}

for instructions, basement_location in test_cases.items():
    santa.reset(0, 0)
    santa.process_instructions(instructions)
    assert santa.basement == basement_location, f"the {instructions} did not match {basement_location}"

santa.reset(0, 0)
santa.process_instructions(puzzle_input[0])
print('Part 2 solution:', santa.basement)
