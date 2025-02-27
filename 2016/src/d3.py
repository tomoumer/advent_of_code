# Day 3 of 2016
import re

# =========== CLASSES AND FUNCTIONS =============
def check_if_valid(s1, s2, s3):
    # take the largest side and check if other two are larger
    is_valid = False
    if s1 == max(s1, s2, s3):
        if s2 + s3 > s1:
            is_valid = True
    elif s2 == max(s1, s2, s3):
        if s1 + s3 > s2:
            is_valid = True
    else:
        if s1+s2 > s3:
            is_valid = True

    return is_valid

# =============== TEST CASES ====================


# ================= PART 1 ======================
triangles = []

with open('./2016/inputs/d3.txt') as f:
    for row in f:
        triangles.append(list(map(int, re.findall('\d+',row))))

valid_triangles = 0
for triangle in triangles:
    valid_triangles += check_if_valid(*triangle)

print('Part 1 solution:', valid_triangles)

# ================= PART 2 ======================

valid_verti_triangles = 0

for i in range(0, len(triangles), 3):
    # to get the right numbers together
    for j in range(3):
        s1 = triangles[i][j]
        s2 = triangles[i+1][j]
        s3 = triangles[i+2][j]

        valid_verti_triangles += check_if_valid(s1,s2,s3)

print('Part 2 solution:', valid_verti_triangles)