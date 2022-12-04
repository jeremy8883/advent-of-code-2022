from functools import reduce

def parse_data_1(data):
    lines = data.split("\n")
    return list(map(lambda l: (l[0:len(l) // 2], l[len(l) // 2:len(l)]), lines))

def get_intersection(items):
    # It's known that there will always be exactly 1 item returned
    return reduce(lambda acc, val: acc.intersection(set(val)), items[1:], set(items[0])).pop()

def get_priority(item):
    ascii_code = ord(item)
    # 97 a, 65 A
    return ascii_code - 64 + 26 if ascii_code < 97 else ascii_code - 96

def part_1(data):
    sacks = parse_data_1(data)
    priorities = list(map(lambda sack: get_priority(get_intersection(sack)), sacks))
    return sum(priorities)

def parse_data_2(data):
    lines = data.split("\n")
    groups = []
    for x in range(0, len(lines), 3):
        groups.append(lines[x:x+3])
    return groups

def part_2(data):
    sacks = parse_data_2(data)
    priorities = list(map(lambda sack: get_priority(get_intersection(sack)), sacks))
    return sum(priorities)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
