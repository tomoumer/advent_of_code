# Day 22 of 2015
from copy import deepcopy


# YER A WIZARD HARRY
# smh Wizards are for scrubs, Necromancers FTW.
# also note if I get back to this, I should get rid of player and boss class
# instead, have a cached gamestate to track the ones that have happened already...
# =========== CLASSES AND FUNCTIONS =============
class Character():

    def __init__(self, type, hp, damage, armor=0, mp=0):
        self.type = type
        self.hp = int(hp)
        self.damage = int(damage)
        self.armor = int(armor)
        self.mp = int(mp)

class Spell():

    def __init__(self, name, manacost, damage, heal, armor, mana_regen, duration):
        self.name = name
        self.manacost = manacost
        self.damage = damage
        self.heal = heal
        self.armor = armor
        self.mana_regen = mana_regen
        self.duration = duration

def process_turn(player, boss, effects=dict(), total_mana_used=0, turn='player', hardmode=False):
    global spell_list
    global least_mana_used

    if hardmode & (turn == 'player'):
        player.hp -= 1
        if player.hp <= 0:
            return

    if total_mana_used > least_mana_used:
        return

    # first resolve existing effects, regardless of whose turn it is
    expired_effects = []
    if len(effects) > 0:
        for sp_name, effect in effects.items():
            effect.duration -= 1
            player.hp += effect.heal
            boss.hp -= effect.damage
            if effect.armor > 0:    # this one really meessed me up 
                player.armor = effect.armor
            player.mp += effect.mana_regen

            if effect.duration == 0:
                if sp_name == 'Shield':
                    player.armor = 0
                expired_effects.append(sp_name)
    
    if len(expired_effects) > 0:
        for expired in expired_effects:
            del effects[expired]
    
    if boss.hp <= 0:
        # print('player wins!', total_mana_used)
        least_mana_used = min(least_mana_used, total_mana_used)
        return

    if turn == 'boss':
        boss_dmg = max(1, boss.damage - player.armor)
        player.hp -= boss_dmg
        if player.hp <= 0:
            # print('boss wins')
            return
        else:
            process_turn(player, boss, effects, total_mana_used, 'player', hardmode)

    else:
        for spell in spell_list:
            if spell.manacost > player.mp: # not enough mana
                continue

            if spell.name in effects.keys(): #spell ongoing, can't duplicate
                continue
            
            update_player = deepcopy(player)
            update_boss = deepcopy(boss)
            update_effects = deepcopy(effects)
            update_player.mp -= spell.manacost
            
            if spell.duration == 0:
                update_boss.hp -= spell.damage
                update_player.hp += spell.heal
                if update_boss.hp <= 0:
                    least_mana_used = min(least_mana_used, total_mana_used + spell.manacost)
                    return
                process_turn(update_player, update_boss, update_effects, total_mana_used + spell.manacost, 'boss', hardmode)

            elif spell.name not in effects.keys():   

                update_effects[spell.name] = deepcopy(spell)
                process_turn(update_player, update_boss, update_effects, total_mana_used + spell.manacost, 'boss', hardmode)

            else:
                raise('spell not accounted for!')

# =============== TEST CASES ====================
spell_list = [
    Spell('Magic Missile', 53, 4, 0, 0, 0, 0),
    Spell('Drain', 73, 2, 2, 0, 0, 0),
    Spell('Shield', 113, 0, 0, 7, 0, 6),
    Spell('Poison', 173, 3, 0, 0, 0, 6),
    Spell('Recharge', 229, 0, 0, 0, 101, 5)]

test_boss = Character('boss', 13, 8, 0, 0)
test_player = Character('player', 10, 0, 0, 250)

least_mana_used = 100000
process_turn(deepcopy(test_player), deepcopy(test_boss))
assert least_mana_used == 173 + 53

test_boss2 = Character('boss', 14, 8, 0, 0)
test_player2 = Character('player', 10, 0, 0, 250)

least_mana_used = 100000
process_turn(deepcopy(test_player2), deepcopy(test_boss2))
assert least_mana_used == 229 + 113 + 73 + 173 + 53

# =============== PART 1 & 2 ====================
puzzle_input = []

with open('./2015/inputs/d22.txt') as f:
    for j, row in enumerate(f):
        _, tmp_val = row.split(':')
        puzzle_input.append(int(tmp_val.strip()))

# note the values are in correct order
boss = Character('boss', *puzzle_input)
player = Character('player', 50, 0, 0, 500)

least_mana_used = 100000
process_turn(deepcopy(player), deepcopy(boss))

print('Part 1 solution:', least_mana_used)

least_mana_used = 100000
process_turn(deepcopy(player), deepcopy(boss), hardmode=True)

print('Part 2 solution:', least_mana_used)