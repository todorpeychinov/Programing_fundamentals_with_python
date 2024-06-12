def tribonacci_sequence(number):
    result_list = [1]
    for i in range(1, number):
        if len(result_list) < 3:
            result_list.append(i)
        else:
            result_list.append(result_list[i - 1] + result_list[i - 2] + result_list[i - 3])
    return " ".join([str(num) for num in result_list])

tribonacci_sequence_list = []
tribonacci_number = int(input())

print(tribonacci_sequence(tribonacci_number))

