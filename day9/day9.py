from ramda import pipe, split, map, min, max, assoc
from utils.point import is_point_nearby, new_point

def frame(min_val, max_val, value):
    return min(max(min_val, value), max_val)

def direction_to_vector(direction):
    if direction == "U":
        return new_point(0, -1)
    elif direction == "D":
        return new_point(0, 1)
    elif direction == "L":
        return new_point(-1, 0)
    elif direction == "R":
        return new_point(1, 0)

def parse_data(data):
    return pipe(
        split("\n"),
        map(lambda line: line.split(" ")),
        map(lambda sp: { "direction": direction_to_vector(sp[0]), "distance": int(sp[1]) }),
    )(data)

def move_head(direction, h_pos):
    return new_point(h_pos["x"] + direction["x"], h_pos["y"] + direction["y"])

def move_knot(new_h_pos, k_pos):
    if is_point_nearby(new_h_pos, k_pos):
        return k_pos
    move_by = new_point(
        frame(-1, 1, new_h_pos["x"] - k_pos["x"]),
        frame(-1, 1, new_h_pos["y"] - k_pos["y"]),
    )
    return new_point(
        k_pos["x"] + move_by["x"],
        k_pos["y"] + move_by["y"],
    )

def part_1(data):
    instructions = parse_data(data)
    h_pos = new_point(0, 0)
    k_pos = new_point(0, 0)
    end_trail = {f"{h_pos['x']},{h_pos['y']}"}

    for ins in instructions:
        for i in range(ins["distance"]):
            h_pos = move_head(ins["direction"], h_pos)
            k_pos = move_knot(h_pos, k_pos)
            end_trail.add(f"{k_pos['x']},{k_pos['y']}")
    return len(end_trail)

def move_tail(poses):
    new_poses = poses + [] # avoid mutation outside the function
    for i, pos in enumerate(new_poses):
        if i != 0:
            new_poses[i] = move_knot(new_poses[i - 1], pos)

    return new_poses

def part_2(data):
    instructions = parse_data(data)
    poses = [new_point(0, 0)] * 10
    end_trail = {"0,0"}
    for ins in instructions:
        for i in range(ins["distance"]):
            poses = [move_head(ins["direction"], poses[0])] + poses[1:]
            poses = move_tail(poses)
            end_trail.add(f"{poses[-1]['x']},{poses[-1]['y']}")
    return len(end_trail)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
