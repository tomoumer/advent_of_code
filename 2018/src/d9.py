# Day 9 of 2018
from collections import deque
import re

# =========== CLASSES AND FUNCTIONS =============
def play_with_marbles(num_players, num_marbles):
    
    player_scores = num_players * [0] 

    game_state = deque([])

    for i in range(num_marbles + 1):

        if (i > 0) and (i % 23 == 0):
            game_state.rotate(7)
            removed = game_state.pop()
            player_num = i % num_players

            player_scores[player_num] += removed + i
            game_state.rotate(-1)
            

        else:
            game_state.rotate(-1)
            game_state.append(i)
        
    return max(player_scores)



# =============== TEST CASES ====================
game_configs = [
    '9 players; last marble is worth 25 points: high score is 32',
    '10 players; last marble is worth 1618 points: high score is 8317',
    '13 players; last marble is worth 7999 points: high score is 146373',
    '17 players; last marble is worth 1104 points: high score is 2764',
    '21 players; last marble is worth 6111 points: high score is 54718',
    '30 players; last marble is worth 5807 points: high score is 37305']

for game_config in game_configs:

    num_players, num_marbles, high_score = list(map(int, re.findall('\d+', game_config)))
    max_score = play_with_marbles(num_players, num_marbles)
    assert max_score == high_score



# =============== PART 1 & 2 ====================

with open('./2018/inputs/d9.txt') as f:
    for row in f:
        num_players, num_marbles = list(map(int, re.findall('\d+',row.strip())))

max_score = play_with_marbles(num_players, num_marbles)
max_score2 = play_with_marbles(num_players, num_marbles * 100)

print('Part 1 solution:', max_score)
print('Part 2 solution:', max_score2)