def check_happiness(improved_happiness_lst):
    average_happiness = sum(improved_happiness_lst) / len(improved_happiness_lst)
    counter_happy = 0
    total_count = len(improved_happiness_lst)
    for current_happiness in improved_happiness_lst:
        if current_happiness >= average_happiness:
            counter_happy += 1
    happiness = 'happy' if counter_happy >= total_count / 2 else 'not happy'
    return f'Score: {counter_happy}/{total_count}. Employees are {happiness}!'


employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
improved_happiness = [current_happiness * happiness_improvement_factor for current_happiness in employees_happiness]

print(check_happiness(improved_happiness))

