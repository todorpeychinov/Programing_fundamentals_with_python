import re

pattern = r'\b_([A-Za-z0-9]+)\b'
user_input = input()

match = re.findall(pattern, user_input)
print(",".join(match))