# Day 2 of 2015

class Present:

    def __init__(self, dimensions):
        l, w, h = dimensions.split('x')
        self.length = int(l)
        self.width = int(w)
        self.height = int(h)

    def paper_needed(self):
        side1 = self.length * self.width 
        side2 = self.width  * self.height
        side3 = self.height * self.length

        min_side = min(side1, side2, side3)

        surface_area = 2* (side1 + side2 + side3)

        return surface_area + min_side
    
    def bow_needed(self):
        volume = self.length * self.width * self.height

        shortest_sides = [self.length, self.width, self.height]
        shortest_sides.sort()
        shortest1 = shortest_sides[0]
        shortest2 = shortest_sides[1]

        return volume + 2* shortest1 + 2* shortest2



# load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d2.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

# print(len(puzzle_input))


# ================= PART 1 ======================
test_cases = {'2x3x4': 58,
              '1x1x10': 43}

for dimensions, paper in test_cases.items():
    present = Present(dimensions)
    assert present.paper_needed() == paper, f"the {dimensions} did not match {paper}"

total_feetage = 0

for dimensions in puzzle_input:
    present = Present(dimensions)
    total_feetage += present.paper_needed()

print('Part 1 solution:', total_feetage)

# ================= PART 2 ======================
test_cases = {'2x3x4': 34,
              '1x1x10': 14}

for dimensions, bow in test_cases.items():
    present = Present(dimensions)
    assert present.bow_needed() == bow, f"the {dimensions} did not match {bow}"

total_bowage = 0

for dimensions in puzzle_input:
    present = Present(dimensions)
    total_bowage += present.bow_needed()

print('Part 2 solution:', total_bowage)




