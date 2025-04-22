# Day 8 of 2018

# =========== CLASSES AND FUNCTIONS =============
def traverse_tree(navigation):
    # get the current vals
    num_children = navigation[0]
    num_meta = navigation[1]
    node_values = []
    total_meta = 0

    # the rest of the data
    navigation = navigation[2:]

    if num_children == 0:
        total_meta += sum(navigation[:num_meta])
        node_value = sum(navigation[:num_meta])
        return total_meta, node_value, navigation[num_meta:]
    
    else:
        for i in range(num_children):
            # this will pick up all the 0 child metas
            sum_meta, node_value, navigation = traverse_tree(navigation)
            total_meta += sum_meta
            node_values.append(node_value)

        # child node scores
        node_value = sum(node_values[k - 1] for k in navigation[:num_meta] if k > 0 and k <= len(node_values))

    # can't forget to add the non-zero child meta
    total_meta += sum(navigation[:num_meta])

    return total_meta, node_value, navigation[num_meta:]


# =============== TEST CASES ====================
navigation = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
navigation = list(map(int, navigation.split()))

total_meta, node_value, navigation = traverse_tree(navigation)
assert total_meta == 138
assert node_value == 66

# =============== PART 1 & 2 ====================

with open('./2018/inputs/d8.txt') as f:
    for row in f:
        navigation = list(map(int, row.strip().split()))


total_meta, node_value, navigation = traverse_tree(navigation)

print('Part 1 solution:', total_meta)
print('Part 2 solution:', node_value)