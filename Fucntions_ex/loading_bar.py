def loading_bar_fucntion(percentage):
    result_string = ''
    if percentage == 100:
        result_string = '100% Complete!\n[%%%%%%%%%%]'
    else:
        percentage_number = percentage // 10
        result_string = f'{percentage}% [{"%" * percentage_number}{"." * (10 - percentage_number)}]\nStill loading...'
    return result_string


percentage = int(input())
print(loading_bar_fucntion(percentage))