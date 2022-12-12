def parse_2d_int(data) -> list[list[int]]:
    return [[int(cell) for cell in row] for row in data.split("\n")]

def parse_2d(data) -> list[list[str]]:
    return [[cell for cell in row] for row in data.split("\n")]
