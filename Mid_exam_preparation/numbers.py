def find_top_five_integers(integers):

    average = sum(integers) / len(integers)
    result_list = [num for num in integers if num > average]
    result_list.sort(reverse=True)

    if len(result_list) > 5:
        return " ".join(map(str, result_list[:5]))

    elif len(result_list) == 0:
        return "No"

    else:
        return " ".join(map(str, result_list))


integer_list = list(map(int, input().split()))

result = find_top_five_integers(integer_list)
print(result)
