from ramda import pipe

def parse_data(data):
    return data.split("\n")

def part_1(data):
    lines = parse_data(data)
    return "TODO"

def part_2(data):
    lines = parse_data(data)
    return "TODO"

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
