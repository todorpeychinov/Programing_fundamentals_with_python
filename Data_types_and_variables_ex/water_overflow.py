number_of_inputs = int(input())
filled = 0

for i in range(number_of_inputs):
    current_fill = int(input())
    if (filled + current_fill) > 255:
        print("Insufficient capacity!")
        continue
    else:
        filled += current_fill

print(filled)