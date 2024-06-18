current_version = input().split('.')
next_version = int("".join(current_version)) + 1
print(".".join(str(next_version)))
