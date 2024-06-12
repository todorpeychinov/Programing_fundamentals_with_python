def check_perfect_number(number):
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())

print(check_perfect_number(number))