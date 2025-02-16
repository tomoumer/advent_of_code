# Day 15 of 2015
import numpy as np
import re
from itertools import combinations
from copy import deepcopy
import time

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
        values = [int(x) for x in re.findall('-?\d', ingredient)]
        ingredient_mix.append(Ingredient(name, values, even_tsp))

    return ingredient_mix

def calculate_score(ingredient_mix):
    total_score = np.zeros(4)
    for ingredient in ingredient_mix:
        total_score += ingredient.tsp * ingredient.values

    total_score = np.prod(total_score)
    return max(0, total_score)


# essentially, optimizing values by changing 2 ingredients at a time
def find_best_score(ingredient_mix):
    current_score = calculate_score(ingredient_mix)
    best_score = current_score

    # needed to add this to reiterate multiple times over
    # just because 1 and 2 got optimized, doesnt mean that will still hold
    # once 3 and 4 are optimized too
    for i in range(100):
        # try two at a time
        for ingredient1, ingredient2 in combinations(ingredient_mix, 2):
            
            # increasing ingredient 1
            while True:
                ingredient1.tsp += 1
                ingredient2.tsp -= 1
                new_score = calculate_score(ingredient_mix)

                # update and keep going
                if new_score > current_score:
                    current_score = new_score
                else: # reset the changes
                    ingredient1.tsp -= 1
                    ingredient2.tsp += 1                
                    break
            
            # increasing ingredient 2
            while True:
                ingredient1.tsp -= 1
                ingredient2.tsp += 1
                new_score = calculate_score(ingredient_mix)

                # update and keep going
                if new_score > current_score:
                    current_score = new_score
                else: # reset the changes
                    ingredient1.tsp += 1
                    ingredient2.tsp -= 1                
                    break

        #
        if best_score == current_score:
            break
        else:
            best_score = current_score

    return current_score


# for efficiency this could be done in calculate_score instead
def get_calories(ingredient_mix):
    cals = 0
    for ingredient in ingredient_mix:
        cals += ingredient.calories * ingredient.tsp
    return cals


# I need to try all the options
def optimize_calories(ingredient_mix):
    global possible_optimizations
    global checked_scores
    for ingredient1, ingredient2 in combinations(ingredient_mix, 2):
        tmp_ingr1 = ingredient1.tsp
        tmp_ingr2 = ingredient2.tsp
        if ingredient1.calories < ingredient2.calories:
            ingredient1.tsp += 1
            ingredient2.tsp -= 1
        else:
            ingredient1.tsp -= 1
            ingredient2.tsp += 1

        current_score = calculate_score(ingredient_mix)
        current_calories = get_calories(ingredient_mix) 

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
    print('==== recipe - DONT TRY THIS AT HOME ====')
    for ingredient in ingredient_mix:
        print(ingredient.name, ':', ingredient.tsp, 'tsp')
    print('total calories', get_calories(ingredient_mix))
    print('')


# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d15.txt') as f:
    for j, row in enumerate(f):
        puzzle_input.append(row)

print('input rows', len(puzzle_input))

test_input = [
    'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
    'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']


# ================= PART 1 ======================

ingredient_mix = assemble_ingredients(test_input)
best_score = find_best_score(ingredient_mix)
print_recipe(ingredient_mix)
assert best_score == 62842880


# # part 2 test
possible_optimizations = []
checked_scores = []
optimize_calories(deepcopy(ingredient_mix))
for possibility in possible_optimizations:
    assert calculate_score(possibility) == 57600000


ingredient_mix = assemble_ingredients(puzzle_input)
best_score = find_best_score(ingredient_mix)
print_recipe(ingredient_mix)

print('Part 1 solution:', int(best_score))

# ================= PART 2 ======================

possible_optimizations = []
checked_scores = []
optimize_calories(deepcopy(ingredient_mix))
calory_conscious = 0
bestest_calory_conscious_cookie = ''
for possibility in possible_optimizations:
    # print(get_calories(possibility), calculate_score(possibility))
    if calory_conscious < calculate_score(possibility):
        calory_conscious = calculate_score(possibility)
        bestest_calory_conscious_cookie = possibility
    
print_recipe(bestest_calory_conscious_cookie)


print('Part 2 solution:', int(calory_conscious))
