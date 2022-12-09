def parse_2d_list(data):
    return [[int(cell) for cell in row] for row in data.split("\n")]
