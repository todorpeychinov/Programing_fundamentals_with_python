import re

input_string = input()

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
destinations = []
travel_points = 0

matches = re.finditer(pattern, input_string)

for match in matches:
    destinations.append(match[2])
    travel_points += len(match[2])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")




