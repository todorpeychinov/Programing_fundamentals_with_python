import re

pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
travel_points = 0



user_input = input()
matches = re.findall(pattern, user_input)

destinations = [match[1] for match in matches]

for dest in destinations:
    travel_points += len(dest)


print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")



