from python.utils import get_index_pairs, Node

MSG_NOT_TRIANGLE_FEW_LEVELS = "Bad Input: Not a triangle - too few lines."
MSG_NOT_TRIANGLE_FEW_NODES = "Bad Input: Not a triangle - each line must have 1 extra item than the previous. " \
                             "See lines {}, {}"

with open('../input.txt', 'r') as file:
    lines = file.readlines()

levels = list()
for line in lines:
    levels.append([Node(int(i), None, None) for i in line.split(' ')])  # node value, max, idx to max path.

if len(levels) < 2:
    raise ValueError(MSG_NOT_TRIANGLE_FEW_LEVELS)

level_pairs = get_index_pairs(levels)

for root_lvl_idx, leaf_lvl_idx in reversed(level_pairs):
    roots, leafs = levels[root_lvl_idx], levels[leaf_lvl_idx]
    if len(leafs) - len(roots) > 1:
        raise ValueError(MSG_NOT_TRIANGLE_FEW_NODES.format(roots, leafs))
    for root_idx, value in enumerate(roots):
        for leaf_idx in [root_idx, root_idx + 1]:
            node = roots[root_idx]
            node.max_path_watermark(leafs[leaf_idx], leaf_idx)


print("Max path value: {}".format(levels[0][0].get_subtotal()))

current_crumble = 0
path = [current_crumble]
for i in range(len(levels) - 1):
    crumble = levels[i][current_crumble].get_crumble()
    path.append(crumble)

print("Path: {}".format(path))
