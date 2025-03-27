# Day 7 of 2017
from collections import deque


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

bottom_disc, wrong_disc, wrong_weight = parse_disk_tree(test_final_discs, test_inter_discs, test_disc_weights)
assert bottom_disc == 'tknk'

_, _, test_disc_weights = initial_disk_scan(test_discs)
assert test_disc_weights[wrong_disc] + wrong_weight == 60


# =============== PART 1 & 2 ====================
discs = []

with open('./2017/inputs/d7.txt') as f:
    for row in f:
        discs.append(row.replace(')','').replace('(','').replace(',', '').split())

final_discs, inter_discs, disc_weights = initial_disk_scan(discs)
bottom_disc, wrong_disc, wrong_weight = parse_disk_tree(final_discs, inter_discs, disc_weights)

# once I have the adjustment to weight needed, net co get the original disc weights
final_discs, inter_discs, disc_weights = initial_disk_scan(discs)
correct_weight = disc_weights[wrong_disc] + wrong_weight

print('Part 1 solution:', bottom_disc)
print('Part 2 solution:', correct_weight)


# full disclosure ... most of the code below done with claude.ai
# getting a graph together in plotly is not super complex (I've done it before)
# but ... I'm tired and I didn't think the climb would be worth the view as they say!

import networkx as nx
import plotly.graph_objs as go

G = nx.DiGraph()

# edges
for disc in inter_discs:
    for parent, children in disc.items():
        for child in children:
            G.add_edge(parent, child)

# Custom hierarchical layout function
def custom_hierarchical_layout(G, root=bottom_disc):
    # Initialize layout dictionary
    pos = {}
    
    # Recursive function to assign positions
    def _assign_pos(node, x_offset, y_level):
        # Assign position to current node
        pos[node] = (x_offset, -y_level)
        
        # Get children of the current node
        children = list(G.successors(node))
        
        # If no children, return
        if not children:
            return
        
        # Calculate spacing between children
        total_width = len(children) - 1
        start_x = x_offset - total_width / 2
        
        # Recursively assign positions to children
        for i, child in enumerate(children):
            child_x = start_x + i
            _assign_pos(child, child_x, y_level + 1)
    
    # Start assigning positions from the root
    _assign_pos(root, 0, 0)
    
    return pos

pos = custom_hierarchical_layout(G)

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
node_text = []
node_color = []

max_depth = max(len(nx.shortest_path(G, bottom_disc, node)) for node in G.nodes())

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
    
    depth = len(nx.shortest_path(G, bottom_disc, node)) - 1
    color_intensity = depth / max_depth
    node_color.append(color_intensity)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        color=node_color,
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Depth',
            xanchor='left',
            titleside='right'
        )
    )
)

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Hierarchical Tree Structure',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Hierarchical Tree Visualization",
                    showarrow=False,
                    xref="paper", yref="paper") ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

fig.show()