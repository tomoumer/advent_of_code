# Day 5 of 2025
import itertools

day = 5

# =========== CLASSES AND FUNCTIONS =============
def load_puzzle_input(filepath, kind):

    puzzle_input1 = []
    puzzle_input2 = []
    fresh_range = True

    with open(filepath) as f:
        for row in f:
            if row == '\n':
                fresh_range = False
                continue
            
            if fresh_range:
                puzzle_input1.append(list(map(int, row.strip().split('-'))))
            else:
                puzzle_input2.append(int(row.strip()))

    print(f'{kind} fresh ranges:', len(puzzle_input1))
    print(f'{kind} ingredients:', len(puzzle_input2))
    print('')

    return puzzle_input1, puzzle_input2

def consolidate_ranges(fresh_ranges):
    
    # to join intervals together
    # not optimal. was considering dropping intervals,
    # but then it gets complicated of keeping track of indices
    # so instead, just modify both intervals I'm checking and later remove duplicates
    for i, fresh_range1 in enumerate(fresh_ranges):
        for j, fresh_range2 in enumerate(fresh_ranges):

            if fresh_range1 == fresh_range2:
                continue

            min1 = fresh_range1[0]
            min2 = fresh_range2[0]
            max1 = fresh_range1[1]
            max2 = fresh_range2[1]

            if max(min1, min2) <= min(max1, max2):
                new_min = min(min1, min2)
                new_max = max(max1, max2)
                fresh_ranges[i] = [new_min, new_max]
                fresh_ranges[j] = [new_min, new_max]
    
    # now remove duplicates
    fresh_ranges.sort()
    fresh_ranges = list(k for k,_ in itertools.groupby(fresh_ranges))

    return fresh_ranges

def check_fresnhess(fresh_ranges, ingredients):

    num_fresh = 0

    for ingredient in ingredients:
        for fresh_range in fresh_ranges:
            if (ingredient >= fresh_range[0]) and (ingredient <= fresh_range[1]):
                num_fresh += 1
                break

    return num_fresh

def count_all_fresh(fresh_ranges):

    all_fresh = 0

    for fresh_range in fresh_ranges:
        # edges inclusive
        all_fresh += (fresh_range[1] - fresh_range[0] + 1)

    return all_fresh


# =============== TEST CASES ====================
fresh_ranges, ingredients = load_puzzle_input(f'./2025/inputs/d{day}test.txt', 'test')
fresh_ranges = consolidate_ranges(fresh_ranges)
num_fresh = check_fresnhess(fresh_ranges, ingredients)
assert num_fresh == 3
all_fresh = count_all_fresh(fresh_ranges)
assert all_fresh == 14

# =============== PART 1 & 2 ====================
fresh_ranges, ingredients  = load_puzzle_input(f'./2025/inputs/d{day}.txt', 'actual')
fresh_ranges = consolidate_ranges(fresh_ranges)
num_fresh = check_fresnhess(fresh_ranges, ingredients)
all_fresh = count_all_fresh(fresh_ranges)

print('Part 1 solution:', num_fresh)
print('Part 2 solution:', all_fresh)