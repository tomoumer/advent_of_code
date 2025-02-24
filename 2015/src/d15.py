# Day 15 of 2015
import numpy as np
import re
from itertools import combinations
from copy import deepcopy
import time

# =========== CLASSES AND FUNCTIONS =============
class Ingredient():

    def __init__(self, name, values, tsp):
        self.name = name
        self.values = np.array(values[:-1])
        self.calories = values[-1]
        self.tsp = tsp

def assemble_ingredients(ingredients_list):
    # not really needed, but if this were to be generalizable ..
    even_tsp = int(100 / len(ingredients_list))
    assert 100 % len(ingredients_list) == 0, f"100 is not evenly divisible by the number of ingredients {len(ingredients_list)}"

    ingredient_mix = []
    for ingredient in ingredients_list:
        name = re.search('^\w+', ingredient).group(0)
        values = list(map(int, re.findall('-?\d', ingredient)))
        ingredient_mix.append(Ingredient(name, values, even_tsp))

    return ingredient_mix

def calculate_score_and_calories(ingredient_mix):
    total_score = np.zeros(4)
    cals = 0
    for ingredient in ingredient_mix:
        total_score += ingredient.tsp * ingredient.values
        cals += ingredient.calories * ingredient.tsp

    total_score = np.prod(total_score)
    
    return max(0, total_score), cals


# essentially, optimizing values by changing 2 ingredients at a time
def find_best_score(ingredient_mix):
    current_score, _ = calculate_score_and_calories(ingredient_mix)
    best_score = current_score

    # needed to add this to reiterate multiple times over
    # just because 1 and 2 got optimized, doesnt mean that will still be the same
    # once 3 and 4 are optimized too
    for i in range(100):
        # try two at a time
        for ingredient1, ingredient2 in combinations(ingredient_mix, 2):
            
            # simplified, this way it will first increase one and decrease the other
            # and vice-vers
            for direction in [+1, -1]: 
                while True:
                    ingredient1.tsp += direction
                    ingredient2.tsp -= direction
                    new_score, _ = calculate_score_and_calories(ingredient_mix)

                    # update and keep going
                    if new_score > current_score:
                        current_score = new_score
                    else: # reset the changes
                        ingredient1.tsp -= direction
                        ingredient2.tsp += direction        
                        break

        #
        if best_score == current_score:
            break
        else:
            best_score = current_score

    return current_score

# I need to try all the options - part 2
def optimize_calories(ingredient_mix):
    global possible_optimizations
    global checked_scores

    for ingredient1, ingredient2 in combinations(ingredient_mix, 2):
        tmp_ingr1 = ingredient1.tsp
        tmp_ingr2 = ingredient2.tsp

        # note I'm going from the max score already and want to reduce calories
        if ingredient1.calories < ingredient2.calories:
            ingredient1.tsp += 1
            ingredient2.tsp -= 1
        else:
            ingredient1.tsp -= 1
            ingredient2.tsp += 1

        current_score, current_calories = calculate_score_and_calories(ingredient_mix)

        # to not repeat calculations with recursion ...
        if [current_score, current_calories] in checked_scores:
            # reset
            ingredient1.tsp = tmp_ingr1
            ingredient2.tsp = tmp_ingr2
            continue
        else:
            checked_scores.append([current_score,current_calories])

        if current_score == 0:
            pass
        elif current_calories == 500:
            possible_optimizations.append(deepcopy(ingredient_mix))
        elif current_calories < 500:
            pass        
        else:
            optimize_calories(deepcopy(ingredient_mix))

        # reset
        ingredient1.tsp = tmp_ingr1
        ingredient2.tsp = tmp_ingr2

# for fun, not needed
def print_recipe(ingredient_mix):
    print('')
    print('==== recipe - DONT TRY THIS AT HOME ====')
    for ingredient in ingredient_mix:
        print(ingredient.name, ':', ingredient.tsp, 'tsp')
    print('total calories', calculate_score_and_calories(ingredient_mix)[1])
    print('')

# =============== TEST CASES ====================
test_input = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']

ingredient_mix = assemble_ingredients(test_input)
best_score = find_best_score(ingredient_mix)
assert best_score == 62842880

possible_optimizations = []
checked_scores = []
optimize_calories(deepcopy(ingredient_mix))
for possibility in possible_optimizations:
    assert calculate_score_and_calories(possibility)[0] == 57600000


# ================= PART 1 ======================
ingredients_list = []

with open('./2015/inputs/d15.txt') as f:
    for row in f:
        ingredients_list.append(row)

ingredient_mix = assemble_ingredients(ingredients_list)
best_score = find_best_score(ingredient_mix)

# print_recipe(ingredient_mix)
print('Part 1 solution:', int(best_score))

# ================= PART 2 ======================

possible_optimizations = []
checked_scores = []
optimize_calories(deepcopy(ingredient_mix))

calory_conscious = 0
bestest_calory_conscious_cookie = ''
for possibility in possible_optimizations:
    if calory_conscious < calculate_score_and_calories(possibility)[0]:
        calory_conscious = calculate_score_and_calories(possibility)[0]
        bestest_calory_conscious_cookie = possibility
    
# print_recipe(bestest_calory_conscious_cookie)

print('Part 2 solution:', int(calory_conscious))
