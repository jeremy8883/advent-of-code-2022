from ramda import curry

from utils.point import new_point


def new_2d(width, height, fill = None):
    arr = [None] * height
    arr = [[fill] * width for _ in arr]
    return arr

@curry
def map_2d(fn, lists):
    if len(lists) == 0: return []
    new = new_2d(len(lists[0]), len(lists))
    for y, row in enumerate(lists):
        for x, cell in enumerate(row):
            new[y][x] = fn(cell, x, y, new)
    return new

@curry
def map_2d_reverse(fn, lists):
    if len(lists) == 0: return []
    new = new_2d(len(lists[0]), len(lists))
    for y, row in reversed(list(enumerate(lists))):
        for x, cell in reversed(list(enumerate(row))):
            new[y][x] = fn(cell, x, y, new)
    return new

@curry
def reduce_2d(fn, init, lists):
    if len(lists) == 0: return init
    acc = init
    for y, row in enumerate(lists):
        for x, cell in enumerate(row):
            acc = fn(acc, cell, x, y)
    return acc

def in_bounds(x, y, lists):
    x_range = range(0, len(lists[0]))
    y_range = range(0, len(lists))
    return x in x_range and y in y_range

@curry
def get_neighbours_2d(pos, lists):
    x = pos["x"]
    y = pos["y"]
    cells = []
    if in_bounds(x - 1, y, lists):
        cells.append((x - 1, y, lists[y][x - 1]))
    if in_bounds(x, y - 1, lists):
        cells.append((x, y - 1, lists[y - 1][x]))
    if in_bounds(x + 1, y, lists):
        cells.append((x + 1, y, lists[y][x + 1]))
    if in_bounds(x, y + 1, lists):
        cells.append((x, y + 1, lists[y + 1][x]))
    return cells

def find_pos(predicate, lists):
    for y, row in enumerate(lists):
        for x, cell in enumerate(row):
            if predicate(cell, x, y):
                return new_point(x, y)
    return None

def enumerate_2d(lists):
    for y, row in enumerate(lists):
        for x, cell in enumerate(row):
            yield x, y, cell
