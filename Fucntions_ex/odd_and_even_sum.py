def odd_and_even_digits_sum(number_as_string):
    even_sum = 0
    odd_sum = 0
    for digit in number_as_string:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

num_as_string = input()
print(odd_and_even_digits_sum(num_as_string))

