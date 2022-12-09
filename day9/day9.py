from ramda import pipe, split, map
from utils.point import is_point_nearby, new_point


def parse_data(data):
    return pipe(
        split("\n"),
        map(lambda line: line.split(" ")),
        map(lambda sp: { "direction": sp[0], "distance": int(sp[1]) }),
    )(data)

def move_head(direction, h_pos, t_pos):
    if direction == "U":
        new_h_pos = { **h_pos, "y": h_pos["y"] - 1 }
        new_t_pos = t_pos \
            if is_point_nearby(new_h_pos, t_pos)\
            else { **new_h_pos, "y": new_h_pos["y"] + 1 }
    elif direction == "D":
        new_h_pos = { **h_pos, "y": h_pos["y"] + 1 }
        new_t_pos = t_pos \
            if is_point_nearby(new_h_pos, t_pos)\
            else { **new_h_pos, "y": new_h_pos["y"] - 1 }
    elif direction == "L":
        new_h_pos = { **h_pos, "x": h_pos["x"] - 1 }
        new_t_pos = t_pos \
            if is_point_nearby(new_h_pos, t_pos)\
            else { **new_h_pos, "x": new_h_pos["x"] + 1 }
    elif direction == "R":
        new_h_pos = { **h_pos, "x": h_pos["x"] + 1 }
        new_t_pos = t_pos \
            if is_point_nearby(new_h_pos, t_pos)\
            else { **new_h_pos, "x": new_h_pos["x"] - 1 }

    return new_h_pos, new_t_pos


def part_1(data):
    instructions = parse_data(data)
    t_pos = new_point(0, 0)
    h_pos = new_point(0, 0)
    h_trail = {f"{h_pos['x']},{h_pos['y']}"}

    for ins in instructions:
        for i in range(ins["distance"]):
            h_pos, t_pos = move_head(ins["direction"], h_pos, t_pos)
            h_trail.add(f"{t_pos['x']},{t_pos['y']}")
    return len(h_trail)

def part_2(data):
    return "TODO"

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
