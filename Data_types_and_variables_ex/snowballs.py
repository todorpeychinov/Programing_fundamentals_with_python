number_of_snowballs = int(input())
best_snowball = 0
best_snowball_time = 0
best_snowball_weight = 0
best_snowball_quality = 0
for i in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    current_snowball_rate = (snowball_weight / snowball_time) ** snowball_quality
    if best_snowball < current_snowball_rate:
        best_snowball = current_snowball_rate
        best_snowball_time = snowball_time
        best_snowball_weight = snowball_weight
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {int(best_snowball)} ({best_snowball_quality})")


