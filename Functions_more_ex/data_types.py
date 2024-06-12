def data_type_func(data_type, data):
    if data_type == "int":
        result = int(data) * 2
    elif data_type == "real":
        result = f'{float(data) * 1.5:.2f}'
    elif data_type == "string":
        result =  '$' + data + '$'
    return result

data_type = input()
data = input()

print(data_type_func(data_type, data))