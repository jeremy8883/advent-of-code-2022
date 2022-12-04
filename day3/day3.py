
def parse_data(data):
    lines = data.split("\n")
    return list(map(lambda l: (l[0:len(l) // 2], l[len(l) // 2:len(l)]), lines))

def get_intersection(items_a, items_b):
    # It's known that there will always be exactly 1 item returned
    return set(items_a).intersection(set(items_b)).pop()

def get_priority(item):
    ascii_code = ord(item)
    # 97 aa 65 AA
    return ascii_code - 64 + 26 if ascii_code < 97 else ascii_code - 96


def part_1(data):
    sacks = parse_data(data)
    priorities = list(map(lambda sack: get_priority(get_intersection(sack[0], sack[1])), sacks))
    return sum(priorities)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
