from ramda import curry

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
