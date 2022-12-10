from ramda import pipe, split, map

from utils.string import insert_every


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

def draw_image(instructions):
    cycle_no = 0
    reg_x = 1
    crt = ["."] * (40 * 6)
    for line in instructions:
        for new_val in run_instruction(line["ins"], line["val"], reg_x):
            if cycle_no % 40 in range(reg_x - 1, reg_x + 2):
                crt[cycle_no] = "#"
            cycle_no = cycle_no + 1
            if new_val != None:
                reg_x = new_val
    return insert_every("".join(crt), "\n", 40)

def part_2(data):
    instructions = parse_data(data)
    return draw_image(instructions)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
