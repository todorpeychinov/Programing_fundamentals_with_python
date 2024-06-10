number = int(input())

isPrime = True

if number < 1:
    isPrime = False


for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

print(isPrime)


