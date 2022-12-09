def new_point(x, y):
    return { "x": x, "y": y }

def is_point_nearby(point_a, point_b):
    return abs(point_a["x"] - point_b["x"]) <= 1 and abs(point_a["y"] - point_b["y"]) <= 1
