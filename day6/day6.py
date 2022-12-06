def parse_data(data):
    return data

def find_index_by_sliding_window(fn, size, arr):
    iter_count = len(arr) - size + 1
    if iter_count <= 0:
        return None

    for i in range(iter_count):
        window = arr[i:i+size]
        if fn(window):
            return i
    return None

def are_all_unique(arr):
    vals = set(arr)
    return len(vals) == len(arr)

def part_1(data):
    return find_index_by_sliding_window(are_all_unique, 4, data) + 4

def part_2(data):
    return find_index_by_sliding_window(are_all_unique, 14, data) + 14

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()
    print(part_1(data))
    print(part_2(data))
