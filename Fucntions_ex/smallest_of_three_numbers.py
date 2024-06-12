def smallest_of_three_integers(num1, num2, num3):
    list_of_numbers = [num1, num2, num3]
    return min(list_of_numbers)

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_of_three_integers(number_1, number_2, number_3))