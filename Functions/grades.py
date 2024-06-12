def solve(grade):
    if grade >= 5.5:
        return 'Excellent'
    elif grade >= 4.5:
        return 'Very good'
    elif grade >= 3.5:
        return 'Good'
    elif grade >= 3.0:
        return 'Poor'
    else:
        return 'Fail'


grade = float(input())
print(solve(grade))