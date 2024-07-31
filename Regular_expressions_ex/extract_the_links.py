import re

pattern = r"(www\.[A-Za-z0-9-]+(\.[a-z]+)+)"

user_input = input()

while user_input:
    match = re.search(pattern, user_input)
    if match:
        print(match.group(1))

    user_input = input()