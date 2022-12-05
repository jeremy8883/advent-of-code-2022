from pipe import select, where
from toolz import accumulate

def new_instruction(move_count, from_index, to_index):
    return {
        "move_count": int(move_count),
        "from_index": int(from_index) - 1,
        "to_index": int(to_index) - 1,
    }

def parse_data(data):
    [stack_str, instructions_str] = data.split("\n\n")

    lines = stack_str.split("\n")[0:-1][::-1]
    labels = stack_str.split("\n")[-1:][0].split(" ")\
        | where(lambda l: l != "")
    stack_count = len(list(labels))
    stacks = [[] for x in range(stack_count)]
    for line in lines:
        for i, item in enumerate(line[1:len(line):4]):
            if item != " ":
                stacks[i].append(item)

    instructions = instructions_str.split("\n")\
        | select(lambda line: line.split(" "))\
        | select(lambda line: new_instruction(line[1], line[3], line[5]))

    return [stacks, list(instructions)]

def part_1(data):
    [stacks, instructions] = parse_data(data)

    for ins in instructions:
        for x in range(ins["move_count"]):
            item = stacks[ins["from_index"]].pop()
            stacks[ins["to_index"]].append(item)

    return "".join([stack[-1:][0] for stack in stacks])

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
