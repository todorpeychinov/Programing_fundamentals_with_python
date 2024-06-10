number_of_lines = int(input())
oppening_brackets = 0
closing_brackets = 0
last_bracket = None
flag = False

for line in range(number_of_lines):
    current_string = input()
    if last_bracket == current_string:
        flag = True
    if current_string == '(':
        oppening_brackets += 1
        last_bracket = current_string
    elif current_string == ')':
        closing_brackets += 1
        if last_bracket != '(':
            flag = True
        last_bracket = current_string

if (oppening_brackets == closing_brackets) and (flag == False):
    print('BALANCED')
else:
    print('UNBALANCED')