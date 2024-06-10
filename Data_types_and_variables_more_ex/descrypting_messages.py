key = int(input())
number_of_lines = int(input())
message = ""

for line in range(number_of_lines):
    current_line = input()
    message += (chr(ord(current_line) + key))

print(message)
    