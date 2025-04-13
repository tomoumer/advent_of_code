# Day 7 of 2017
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


# =========== CLASSES AND FUNCTIONS =============
def initial_disk_scan(discs):
    final_discs = set()
    inter_discs = deque()
    # part 2
    disc_weights = dict()

    for disc in discs:
        if len(disc) == 2:
            final_discs.add(disc[0])
        else:
            # note 1 is the value and 2 is the arrow, the rest are held discs
            inter_discs.append({disc[0]: {disc[i] for i in range(3,len(disc))}})

        # weights always in same position
        disc_weights[disc[0]] = int(disc[1])

    return final_discs, inter_discs, disc_weights

def parse_disk_tree(final_discs, inter_discs, disc_weights):

    wrong_disc=''

    # the logic is to go from the end to base
    while inter_discs:
        disc = inter_discs.popleft()
        disc_root = list(disc.keys())[0]

        if disc[disc_root].issubset(final_discs):
            # check weights
            if wrong_disc == '':
                tower_weight = 0
                tmp_weights = dict()
                for tmp_disc in disc[disc_root]:
                    # check that all the weights are the same by building a dict of weights as keys
                    if disc_weights[tmp_disc] not in tmp_weights.keys():
                        tmp_weights[disc_weights[tmp_disc]] = [tmp_disc]
                    else:
                        tmp_weights[disc_weights[tmp_disc]].append(tmp_disc)

                    tower_weight += disc_weights[tmp_disc]
                
                # if dictionary has 2 different keys (weights), we found what we're looking for
                # if it only has 1 key, then all branches have same weight
                if len(tmp_weights) > 1:
                    for w, dsc in tmp_weights.items():
                        if len(dsc) == 1:
                            wrong_disc = dsc[0]
                            wrong_weight = w
                        else:
                            correct_weight = w
                    
                    # weight adjustment needed
                    wrong_weight = correct_weight - wrong_weight

                # the root disk takes on the weight of the tower
                disc_weights[disc_root] += tower_weight
            
            # remove the three elemenets that bind to the next one
            final_discs.difference(disc[disc_root])
            # now the disc that held them up is the "final"
            final_discs.add(disc_root)

        else:
            # the current examined disc provides support for discs
            # not yet found
            inter_discs.append(disc)

    # the last disk to be processed is going to be the bottom one
    return disc_root, wrong_disc, wrong_weight


# =============== TEST CASES ====================
test_vals =['pbga (66)',
'xhth (57)',
'ebii (61)',
'havc (66)',
'ktlj (57)',
'fwft (72) -> ktlj, cntj, xhth',
'qoyq (66)',
'padx (45) -> pbga, havc, qoyq',
'tknk (41) -> ugml, padx, fwft',
'jptl (61)',
'ugml (68) -> gyxo, ebii, jptl',
'gyxo (61)',
'cntj (57)']

test_discs = []
for row in test_vals:
    test_discs.append(row.replace(')','').replace('(','').replace(',', '').split())

test_final_discs, test_inter_discs, test_disc_weights = initial_disk_scan(test_discs)

test_bottom_disc, wrong_disc, wrong_weight = parse_disk_tree(test_final_discs, test_inter_discs, test_disc_weights)
assert test_bottom_disc == 'tknk'

test_final_discs, test_inter_discs, test_disc_weights = initial_disk_scan(test_discs)
assert test_disc_weights[wrong_disc] + wrong_weight == 60


# =============== PART 1 & 2 ====================
discs = []

with open('./2017/inputs/d7.txt') as f:
    for row in f:
        discs.append(row.replace(')','').replace('(','').replace(',', '').split())

final_discs, inter_discs, disc_weights = initial_disk_scan(discs)
bottom_disc, wrong_disc, wrong_weight = parse_disk_tree(final_discs, inter_discs, disc_weights)

# once I have the adjustment to weight needed, net to get the original disc weights
final_discs, inter_discs, disc_weights = initial_disk_scan(discs)
correct_weight = disc_weights[wrong_disc] + wrong_weight

print('Part 1 solution:', bottom_disc)
print('Part 2 solution:', correct_weight)


G = nx.DiGraph()

leveling = deque([[bottom_disc, 0]])
G.add_node(bottom_disc, level=0)

while leveling:
    # print(leveling)
    parent_disc, level = leveling.popleft()
    level += 1
    
    for disc_map in inter_discs:
        if parent_disc in disc_map.keys():
            for child_disc in disc_map[parent_disc]:
                G.add_node(child_disc, level=level)
                G.add_edge(parent_disc, child_disc)
                leveling.append([child_disc, level])

            break

pos = nx.multipartite_layout(G, subset_key="level", align="horizontal")

plt.figure(figsize=(14, 8))
nx.draw(G, pos=pos)
# plt.show()
plt.savefig(f'./2017/img/tree_circus_d7.png', bbox_inches='tight', pad_inches=0.1)