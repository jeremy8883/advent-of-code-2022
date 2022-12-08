from ramda import reduce, assoc_path
from more_itertools import peekable
from utils.print_dict import print_dict

def parse_data(data):
    return data.split("\n")

def read_input(it):
    line = next(it)
    if line == None: return None, None
    spl = line.split(" ")
    assert(spl[0] == "$")
    return spl[1], spl[2:]

def read_output(it):
    lines = []
    line = it.peek()
    while not line.startswith("$ "):
        lines.append(next(it))
        try:
            line = it.peek()
        except StopIteration:
            break
    return lines

def create_dir_ojb(name):
    return {
        "name": name,
        "children": {},
        "size": None,
        "type": "directory",
    }

def create_file_obj(name, size):
    return {
        "name": name,
        "size": size,
        "type": "file",
    }

def add_child(children, line):
    sp = line.split(" ")
    if sp[0] == "dir":
        children = { **children, sp[1]: create_dir_ojb(sp[1]) }
    else:
        children = { **children, sp[1]: create_file_obj(sp[1], int(sp[0])) }
    return children

def intersperse(list, value):
    res = [value] * (2 * len(list) - 1)
    res[::2] = list
    return res

def create_path_for_assoc(path):
    path_to_assoc = intersperse(path, "children")
    path_to_assoc.insert(0, "children")
    if len(path) != 0:
        path_to_assoc.append("children")
    return path_to_assoc

def get_dir_tree(lines):
    it = peekable(lines)
    cmd, args = read_input(it)
    tree = create_dir_ojb("")
    path = []
    while cmd != None:
        if cmd == "cd":
            if args[0] == "/":
                path = []
            elif args[0] == "..":
                path.pop()
            else:
                path.append(args[0])
        elif cmd == "ls":
            output = read_output(it)
            children = reduce(add_child, {}, output)
            tree = assoc_path(create_path_for_assoc(path), children, tree)
        try:
            cmd, args = read_input(it)
        except StopIteration:
            break
    return tree

# Mutates object because I don't care
def add_dir_sizes(dir_or_file):
    if dir_or_file["type"] == "directory":
        size = sum([add_dir_sizes(child) for child in dir_or_file["children"].values()])
        dir_or_file["size"] = size
        return size
    else:
        return dir_or_file["size"]

def find_dirs_sizes_less_than(dir, amount = 100000):
    sizes = []
    if dir["size"] <= amount:
        sizes = sizes + [dir["size"]]
    for child in dir["children"].values():
        if child["type"] == "directory":
            sizes = sizes + find_dirs_sizes_less_than(child, amount)
    return sizes

def part_1(data):
    lines = parse_data(data)
    tree = get_dir_tree(lines)
    add_dir_sizes(tree)
    return sum(find_dirs_sizes_less_than(tree))

def part_2(data):
    return "TODO"

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
