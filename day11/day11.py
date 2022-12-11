from ramda import pipe, replace, split, map, product
from utils.print import print_json

def parse_data(data):
    def parse_group(i, g):
        return {
            "index": i,
            "items": pipe(
                replace("  Starting items: ", ""),
                split(", "),
                map(int),
            )(g[1]),
            "operation": g[2].replace("  Operation: new = ", ""),
            "test_divisible_by": int(g[3].replace("  Test: divisible by ", "")),
            "monkey_if_true": int(g[4].replace("    If true: throw to monkey ", "")),
            "monkey_if_false": int(g[5].replace("    If false: throw to monkey ", "")),
        }

    return [parse_group(i, g.split("\n")) for i, g in enumerate(data.split("\n\n"))]

def part_1(data):
    monkeys = parse_data(data)
    inspection_counts = [0] * len(monkeys)
    for round in range(20):
        for monkey in monkeys:
            for item in monkey["items"]:
                inspection_counts[monkey["index"]] = inspection_counts[monkey["index"]] + 1
                new_worry_level = eval(monkey["operation"], { "old": item }) // 3
                monkey_index = monkey["monkey_if_true"] if new_worry_level % monkey["test_divisible_by"] == 0 else monkey["monkey_if_false"]
                monkeys[monkey_index]["items"].append(new_worry_level)
            # All items will be thrown to another monkey
            monkey["items"] = []
    inspection_counts = sorted(inspection_counts)
    return product(inspection_counts[-2:])

def part_2(data):
    # monkeys = parse_data(data)
    return "TODO"

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
