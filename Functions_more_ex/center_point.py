from math import sqrt


def points_diff(x1, y1, x2, y2):
    #diff_point_1 = abs(x1) + abs(y1)
    #diff_point_2 = abs(x2) + abs(y2)
    diff_point_1 = sqrt(pow(y1, 2) + pow(x1, 2))
    diff_point_2 = sqrt(pow(y2, 2) + pow(x2, 2))

    if diff_point_1 <= diff_point_2:
        return f"({int(x1)}, {int(y1)})"
    else:
        return f"({int(x2)}, {int(y2)})"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(points_diff(x1, y1, x2, y2))