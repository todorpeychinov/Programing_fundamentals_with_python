def factiorial(number):
    if number == 1:
        return 1
    else:
        return number * factiorial(number - 1)

def factiorial_divison(number_1, number_2):
    return factiorial(number_1) / factiorial(number_2)

number_1 = int(input())
number_2 = int(input())
print(f"{factiorial_divison(number_1, number_2):.2f}")