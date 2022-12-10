from ramda import pipe, split, map

def parse_data(data):
    return pipe(
        split("\n"),
        map(lambda line: line.split(" ")),
        map(lambda line: { "ins": line[0], "val": None if len(line) <= 1 else int(line[1]) }),
    )(data)

def run_instruction(ins, val, reg_x):
    if ins == "noop":
        yield None
    elif ins == "addx":
        yield None
        # This is a bit silly, but I wanted to practice using generators in python
        yield reg_x + val

cycles = set([20, 60, 100, 140, 180, 220])

def get_signal_strength(instructions):
    cycle_no = 0
    reg_x = 1
    signals = []
    for line in instructions:
        for new_val in run_instruction(line["ins"], line["val"], reg_x):
            cycle_no = cycle_no + 1
            if cycle_no in cycles:
                signals.append(cycle_no * reg_x)
            if new_val != None:
                reg_x = new_val
    return sum(signals)


def part_1(data):
    instructions = parse_data(data)
    return get_signal_strength(instructions)

def part_2(data):
    return "TODO"

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
