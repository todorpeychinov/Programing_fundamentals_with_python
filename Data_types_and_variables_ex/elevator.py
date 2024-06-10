from math import floor, ceil

person = int(input())
capacity = int(input())

courses = ceil(person / capacity)
print(courses)