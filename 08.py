# 08

import pathlib
import itertools

p = pathlib.Path('data/08.txt')

all_trees = {}
max_x = 0
max_y = 0

for y, line in enumerate(p.read_text().splitlines()):
    for x, height in enumerate(line):
        all_trees[(x, y)] = height

# test_data 'visible' should be 5, and 'total_visible' 21
test_data = """30373
25512
65332
33549
35390
"""

# The hard way, just incase the grid isn't square...
max_x = max(x for x, y in all_trees.keys())
max_y = max(y for x, y in all_trees.keys())
min_x = min(x for x, y in all_trees.keys())
min_y = min(y for x, y in all_trees.keys())

trees_to_check = list(itertools.product(range(min_x+1, max_x), range(min_y+1, max_y)))
total_trees = len(all_trees.keys())
perimeter_trees = total_trees - len(trees_to_check)
assert(len(trees_to_check) == total_trees - (max_x*2) - (max_y*2))


def is_visible(tree):
    # Return 1 if tree is visible to the top, bottom, left or right edges.
    x, y = tree
    up = list(((x, y) for y in range(min_y, y)))
    down = list(((x, y) for y in range(y+1, max_y+1)))
    left = list(((x, y) for x in range(min_x, x)))
    right = list(((x, y) for x in range(x+1, max_x+1)))
    for check in (up, down, left, right):
        check = list(check)
        if all(all_trees[tree] > all_trees[coord] for coord in check):
            return 1
    return 0


visible = sum([is_visible(tree) for tree in trees_to_check])
total_visible = perimeter_trees + visible
# 1870

# Part 2
def get_scenic_score(tree):
    x, y = tree
    # Up and Left need to go from big to small numbers, so needs reversing.
    up = list(((x, y) for y in reversed(range(min_y, y))))
    down = list(((x, y) for y in range(y + 1, max_y + 1)))
    left = list(((x, y) for x in reversed(range(min_x, x))))
    right = list(((x, y) for x in range(x + 1, max_x + 1)))
    sights = []
    for check in (up, down, left, right):
        # Get the sight score for all the way to the edge
        # Find the height difference between our tree and all the ones to the edgs
        sight_all = [int(all_trees[tree]) - int(all_trees[coord]) for coord in check]
        # Remove sight scores for anything after 0 or negative
        # ie. Remove all trees after we reach one our same height or taller
        sight = list()
        for val in sight_all:
            if val <= 0:
                sight.append(val)
                break
            else:
                sight.append(val)
        # Add the qty of trees in our view in each direction
        sights.append(len(sight))
    # Multiple the sight scores together
    score = 1
    for val in sights:
        score = score * val
    return score

# Get the maximum scenic score.
max([get_scenic_score(tree) for tree in trees_to_check])
#517440


