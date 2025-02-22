# Day 21 of 2015
import re
from itertools import combinations, product

# RPG yesss, let's gooooo! Elden Ring best RPG. BEHOLD, DOG.

class Character():

    def __init__(self, type, hp, damage, armor):
        self.type = type
        self.hp = int(hp)
        self.damage = int(damage)
        self.armor = int(armor)

    def equip(self, equipment):
        # print('equipping', equipment[0])
        self.damage += equipment[2]
        self.armor += equipment[3]

    def uneqip(self, equipment):
        self.damage -= equipment[2]
        self.armor -= equipment[3]        

class Item():

    def __init__(self, type, name, cost, damage, armor):
        self.type = type
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

class ItemShop():

    def __init__(self):
        self.weapons = []
        self.armor = []
        self.rings = []

    # sort by cost
    def add_item(self, item):

        if item.type == 'Weapon':
            self.weapons.append(item)
        elif item.type == 'Armor':
            self.armor.append(item)
        else:
            self.rings.append(item)


    def show_inventory(self):
        print('What does a hero truly need? (https://www.youtube.com/watch?v=-cSFPIwMEq4)')
        for item in self.weapons + self.armor + self.rings:
            print(item.name)

    def cheapskate_equipment(self):

        equipment = []
        all_combos = product(self.weapons, self.armor, (self.rings + list(combinations(self.rings, 2)))) 

        for item_sale in all_combos:
            total_equipment = ''
            total_cost = 0
            total_damage = 0
            total_armor = 0

            weapon_choice, armor_choice, rings_choice = item_sale
            total_equipment += (' ' + weapon_choice.name + ' ' + armor_choice.name)
            total_cost += (weapon_choice.cost + armor_choice.cost)
            total_damage += (weapon_choice.damage + armor_choice.damage)
            total_armor += (weapon_choice.armor + armor_choice.armor)

            if isinstance(rings_choice, Item):
                total_equipment += (' ' + rings_choice.name)
                total_cost += rings_choice.cost
                total_damage += rings_choice.damage
                total_armor += rings_choice.armor
            else:
                total_equipment += (' ' + rings_choice[0].name +  ' ' + rings_choice[1].name)
                total_cost += (rings_choice[0].cost + rings_choice[1].cost)
                total_damage += (rings_choice[0].damage + rings_choice[1].damage)
                total_armor += (rings_choice[0].armor + rings_choice[1].armor)

            equipment.append([total_equipment, total_cost, total_damage, total_armor])

        # sort by total cost from lowest to highest
        equipment = sorted(equipment, key=lambda x: x[1])#, reverse=True)

        return equipment


def fight(player, boss):
    player_dmg = max(1, player.damage - boss.armor)
    boss_dmg = max(1, boss.damage - player.armor)

    player_die_turn, reminder = divmod(player.hp, boss_dmg)
    if reminder != 0:
        player_die_turn += 1

    boss_die_turn, reminder = divmod(boss.hp, player_dmg)
    if reminder != 0:
        boss_die_turn += 1


    if player_die_turn < boss_die_turn:
        return boss.type
    else:
        return player.type

# # load in the actual puzzle input
puzzle_input = []

with open('./2015/inputs/d21.txt') as f:
    for j, row in enumerate(f):
        _, tmp_val = row.split(':')
        puzzle_input.append(int(tmp_val.strip()))

# note the values are in correct order
boss = Character('boss', *puzzle_input)

# ================= PART 1 ======================

test_player = Character('player', 8, 5, 5)
test_boss = Character('boss', 12, 7, 2)

assert fight(test_player, test_boss) == 'player'

available_items = ItemShop()

# NOTE: I initially misread .. there HAS to be one weapon
all_items =  """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
NoArmor       0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
NoRing        0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

for item_class in all_items.split('\n\n'):
    for i, item in enumerate(item_class.split('\n')):
        if i == 0:
            item_type = re.match('\w+[^s:]', item).group().strip()
        else:
            item_name = re.match('(\w+\s\+?\d?)', item).group(0).strip()
            item_values = re.findall('[^+]\d+', item)

            available_items.add_item(Item(item_type, item_name, *item_values))

available_items.show_inventory()


player = Character('player', 100, 0, 0)

equipment = available_items.cheapskate_equipment()

for equip_choice in equipment:
    player.equip(equip_choice)
    winner = fight(player, boss)
    # to essentially reset the player
    player.uneqip(equip_choice)
    if winner == 'player':
        break

    
print('Cheapest equipment that wins', equip_choice[0])
print('Part 1 solution:', equip_choice[1])

# ================= PART 2 ======================

# just reverse the order and start from the most expensive
equipment = sorted(equipment, key=lambda x: x[1], reverse=True)


for equip_choice in equipment:
    player.equip(equip_choice)
    winner = fight(player, boss)
    # to essentially reset the player
    player.uneqip(equip_choice)

    if winner == 'boss':
        break


# 282 too high
print('Most expensive equipment that loses', equip_choice[0])
print('Part 2 solution:', equip_choice[1])


