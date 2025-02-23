# Day 2 of 2015

# =========== CLASSES AND FUNCTIONS =============
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

# =============== TEST CASES ====================

test_cases = {'2x3x4': [58, 34],
              '1x1x10': [43, 14]}

for dimensions, [paper, bow] in test_cases.items():
    present = Present(dimensions)
    assert present.paper_needed() == paper
    assert present.bow_needed() == bow


# ================ PART 1 & 2 =====================

present_dimensions = []

with open('./2015/inputs/d2.txt') as f:
    for j, row in enumerate(f):
        present_dimensions.append(row)

total_feetage = 0 # part 1
total_bowage = 0 # part 2

for dimensions in present_dimensions:
    present = Present(dimensions)
    total_feetage += present.paper_needed()
    total_bowage += present.bow_needed()

print('Part 1 solution:', total_feetage)
print('Part 2 solution:', total_bowage)




