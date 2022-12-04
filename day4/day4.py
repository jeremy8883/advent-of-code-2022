from functools import reduce

def parse_data(data):
    lines = data.split("\n")

    def split_range(line):
        pairs = line.split(",")
        pairs = list(map(lambda p: p.split("-"), pairs))
        return list(map(lambda p: [int(p[0]), int(p[1]) + 1], pairs))

    return list(map(split_range, lines))

def is_range_subsection(range_a, range_b):
    return range_a[0] >= range_b[0] and range_a[1] <= range_b[1]

def part_1(data):
    range_pairs = parse_data(data)
    filtered = filter(lambda rp: is_range_subsection(rp[0], rp[1]) or is_range_subsection(rp[1], rp[0]), range_pairs)
    return len(list(filtered))

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
