def new_point(x, y):
    return { "x": x, "y": y }

def is_point_nearby(point_a, point_b):
    return abs(point_a["x"] - point_b["x"]) <= 1 and abs(point_a["y"] - point_b["y"]) <= 1

def point_eq(point_a, point_b):
    return point_a == None and point_b == None or\
           point_a != None and point_b != None and point_a["x"] == point_b["x"] and point_a["y"] == point_b["y"]