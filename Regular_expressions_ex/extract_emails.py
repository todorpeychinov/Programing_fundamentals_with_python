import re

pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'

user_input = input()
match = re.findall(pattern, user_input)

for email in match:
    print(email[0])