from math import floor

def calculate_distance(def_x1, def_y1, def_x2, def_y2):
    return (def_x2-def_x1)**2 + (def_y2-def_y1)**2

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line_1 = calculate_distance(x1, y1, x2, y2)
    line_2 = calculate_distance(x3, y3, x4, y4)
    if line_1 > line_2:
        distance_from_center_point_1 = calculate_distance(x1, y1, 0, 0)
        distance_from_center_point_2 = calculate_distance(x2, y2, 0, 0)
        if distance_from_center_point_1 > distance_from_center_point_2:
            return f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})"
        else:
            return f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})"
    else:
        distance_from_center_point_1 = calculate_distance(x3, y3, 0, 0)
        distance_from_center_point_2 = calculate_distance(x4, y4, 0, 0)
        if distance_from_center_point_1 > distance_from_center_point_2:
            return f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})"
        else:
            return f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))


