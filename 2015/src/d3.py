# Day 3 of 2015

class Santa:
    
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.visited = {(x,y): 1}

    def move(self, direction):
        if direction == '^':
            self.y += 1
        elif direction == 'v':
            self.y -= 1
        elif direction == '>':
            self.x += 1
        elif direction == '<':
            self.x -= 1
        else:
            raise('unrecognized move!' )
        
        # once moved, the dict of visited houses needs to be updated
        current_coord = (self.x, self.y)
        if current_coord in self.visited:
            self.visited[current_coord] += 1
        else:
            self.visited[current_coord] = 1

        
    def radio_instructions(self, instructions):
        for direction in instructions:
            self.move(direction)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.visited = {(x,y): 1}


santa = Santa(0,0)
robo_santa = Santa(0,0)

# load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d3.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

# ================= PART 1 ======================
test_cases = {'>': 2,
              '^>v<': 4,
              '^v^v^v^v^v': 2}

for instructions, num_houses in test_cases.items():
    santa.reset(0,0)
    santa.radio_instructions(instructions)
    assert len(santa.visited) == num_houses, f"the {instructions} did not match {num_houses}"

santa.reset(0,0)
santa.radio_instructions(puzzle_input[0])
print('Part 1 solution:', len(santa.visited))


# ================= PART 2 ======================
test_cases = {'^v': 3,
              '^>v<': 3,
              '^v^v^v^v^v': 11}

for instructions, num_houses in test_cases.items():
    santa.reset(0,0)
    robo_santa.reset(0,0)

    santa.radio_instructions(instructions[::2])
    robo_santa.radio_instructions(instructions[1::2])

    total_houses = santa.visited | robo_santa.visited
    assert len(total_houses) == num_houses, f"the {instructions} did not match {num_houses}"

    
    
santa.reset(0,0)
robo_santa.reset(0,0)

santa.radio_instructions(puzzle_input[0][::2])
robo_santa.radio_instructions(puzzle_input[0][1::2])

total_houses = santa.visited | robo_santa.visited
print('Part 2 solution:', len(total_houses))






