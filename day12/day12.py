from ramda import pipe  # type: ignore
import queue
from utils.list_2d import map_2d, new_2d, get_neighbours_2d, find_pos, enumerate_2d
from utils.parsing import parse_2d
from utils.point import new_point, point_eq

def parse_data(data) -> (list[list[int]], dict[str, int], dict[str, int]):
    chars = parse_2d(data)
    heights = map_2d(lambda char, x, y, _: 0 if char == "S" else 25 if char == "E" else ord(char) - 97, chars)
    start_pos = find_pos(lambda char, x, y: char == "S", chars)
    end_pos = find_pos(lambda char, x, y: char == "E", chars)

    return heights, start_pos, end_pos

def get_path_length(heights, start_pos, end_pos):
    visit_map = new_2d(len(heights[0]), len(heights), False)
    visit_map[start_pos["y"]][start_pos["x"]] = True
    q = queue.Queue()  # FIFO
    q.put((start_pos, []))
    while not q.empty():
        pos, path = q.get()
        height = heights[pos["y"]][pos["x"]]
        if point_eq(pos, end_pos):
            return len(path)
        for x, y, neighbour in get_neighbours_2d(pos, heights):
            if neighbour in range(0, height + 2) and not visit_map[y][x]:
                q.put((new_point(x, y), path + [new_point(x, y)]))
                visit_map[y][x] = True

    return None

def part_1(data) -> int:
    heights, start_pos, end_pos = parse_data(data)
    return get_path_length(heights, start_pos, end_pos)

def part_2(data):
    heights, _, end_pos = parse_data(data)
    results = []
    for x, y, height in enumerate_2d(heights):
        if height == 0:
            path_length = get_path_length(heights, new_point(x, y), end_pos)
            if path_length != None:
                results.append(path_length)
    return min(results)

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
