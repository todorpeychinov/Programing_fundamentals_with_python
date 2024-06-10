number_of_letters = int(input())

for i in range(97, number_of_letters + 97):
    for j in range(97, number_of_letters + 97):
        for k in range(97, number_of_letters + 97):
            print(chr(i) + chr(j) + chr(k))
