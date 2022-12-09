from ramda import pipe, curry
from utils.parsing import parse_2d_list
from utils.print import print_json
from utils.list_2d import map_2d, map_2d_reverse, new_2d, reduce_2d

# Version of max that will return the other value if any value is None
def max(a, b):
    if a == None: return b
    if b == None: return a
    return a if a > b else b

# Going for the O(n) solution, where we create a map of the tallest tree
# to the north, south, east, and west of each tree. We then use this map
# to determine which tree is visible
def create_tall_map(trees):
    @curry
    def add_nw(trees, current, x, y, tall_map):
        w = None if x == 0 else max(tall_map[y][x - 1]["w"], trees[y][x - 1])
        n = None if y == 0 else max(tall_map[y - 1][x]["n"], trees[y - 1][x])
        return { **current, "w": w, "n": n }

    @curry
    def add_se(trees, current, x, y, tall_map):
        e = None if x == len(trees[0]) - 1 else max(tall_map[y][x + 1]["e"], trees[y][x + 1])
        s = None if y == len(trees) - 1 else max(tall_map[y + 1][x]["s"], trees[y + 1][x])
        return { **current, "e": e, "s": s }

    return pipe(
        map_2d(add_nw(trees)),
        map_2d_reverse(add_se(trees)),
    )(new_2d(len(trees[0]), len(trees), { }))

def is_tree_visible(trees, tall_map, x, y):
    tree_height = trees[y][x]
    map_item = tall_map[y][x]
    if map_item["n"] == None or\
            map_item["e"] == None or\
            map_item["s"] == None or\
            map_item["w"] == None or \
            tree_height > map_item["n"] or\
            tree_height > map_item["e"] or\
            tree_height > map_item["s"] or\
            tree_height > map_item["w"]:
        return True
    return False

def count_visible_trees(trees, tall_map):
    return reduce_2d(
        lambda acc, height, x, y:
            acc + 1 if is_tree_visible(trees, tall_map, x, y) else acc,
        0,
        trees
    )

def part_1(data):
    trees = parse_2d_list(data)
    tall_map = create_tall_map(trees)
    return count_visible_trees(trees, tall_map)

def get_scenic_score(trees, x, y):
    total = 1
    # West
    score = 0
    for i in reversed(range(0, x)):
        score = score + 1
        if trees[y][i] >= trees[y][x]:
            break
    if score != 0:
        total = total * score

    # North
    score = 0
    for i in reversed(range(0, y)):
        score = score + 1
        if trees[i][x] >= trees[y][x]:
            break
    if score != 0:
        total = total * score

    # East
    score = 0
    for i in range(x + 1, len(trees[0])):
        score = score + 1
        if trees[y][i] >= trees[y][x]:
            break
    if score != 0:
        total = total * score

    # South
    score = 0
    for i in range(y + 1, len(trees)):
        score = score + 1
        if trees[i][x] >= trees[y][x]:
            break
    if score != 0:
        total = total * score

    return total

def part_2(data):
    trees = parse_2d_list(data)
    score = reduce_2d(lambda acc, _, x, y: max(acc, get_scenic_score(trees, x, y)), 0, trees)
    return score

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
