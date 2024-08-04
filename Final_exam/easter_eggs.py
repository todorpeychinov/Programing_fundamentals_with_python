import re

pattern = r'([@#]+)([a-z]{3,})([@#]+)([^A-Za-z0-9]*)(\/+)([0-9]+)(\/+)'
input_string = input()

matches = re.findall(pattern, input_string)
for match in matches:
    color = match[1]
    amount = match[5]
    print(f'You found {amount} {color} eggs!')