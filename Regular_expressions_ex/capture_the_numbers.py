import re

template = r'\d+'

current_input = input()

while current_input:
    match = re.findall(template, current_input)
    if match:
        print(*match, end=" ")

    current_input = input()
