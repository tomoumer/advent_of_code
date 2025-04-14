# Day 3 of 2018
import numpy as np
import re

# numpy
# each design would do a += 1
# check where numpy grid > 1

# =========== CLASSES AND FUNCTIONS =============
def claim_on_fabric(claims, fabric):
    
    # part 1
    for claim in claims:
        fabric[claim[2]: claim[2]+claim[4], claim[1]: claim[1]+claim[3]] += 1
    
    # part 2 - check which claim still exists in its entirety
    for claim in claims:
        if (fabric[claim[2]: claim[2]+claim[4], claim[1]: claim[1]+claim[3]] == 1).all():
            untouched_claim = claim[0]

            # flag it for drawing
            fabric[claim[2]: claim[2]+claim[4], claim[1]: claim[1]+claim[3]] = -5
            break

    return fabric[fabric > 1].shape[0], untouched_claim

# =============== TEST CASES ====================
fabric = np.zeros((8,8))

unprocessed_claims = ['#1 @ 1,3: 4x4',
'#2 @ 3,1: 4x4',
'#3 @ 5,5: 2x2']

claims = []
for unprocessed_claim in unprocessed_claims:
    claims.append(list(map(int, re.findall('\d+', unprocessed_claim))))

overlap_claims, untouched_claim = claim_on_fabric(claims, fabric)
assert overlap_claims == 4
assert untouched_claim == 3

# =============== PART 1 & 2 ====================
claims = []
fabric = np.zeros((1000,1000))

with open('./2018/inputs/d3.txt') as f:
    for row in f:
        claims.append(list(map(int, re.findall('\d+', row.strip()))))

overlap_claims, untouched_claim = claim_on_fabric(claims, fabric)

print('Part 1 solution:', overlap_claims)
print('Part 2 solution:', untouched_claim)


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 8))
sns.heatmap(fabric,  cmap='viridis_r', square=True, cbar=False)
plt.axis('off')
plt.title('Suit design 101')
# plt.show()
plt.savefig(f'./2018/img/suit_design_d3.png', bbox_inches='tight', pad_inches=0.1)