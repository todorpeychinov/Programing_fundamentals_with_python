def multiplication_sign(num1,num2,num3):
    if num1 < 0 and num2 > 0 and num3 > 0 or \
        num1 > 0 and num2 < 0 and num3 > 0 or \
        num1 > 0 and num2 > 0 and num3 < 0 or \
            num1 < 0 and num2 < 0 and num3 < 0:
        return "negative"
    elif num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    else:
        return "positive"

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(multiplication_sign(num1,num2,num3))