students_results = {}
submbisions_count = {}

while True:
    student = input()

    if student == 'exam finished':
        break

    student = student.split('-')

    if len(student) == 3:
        username = student[0]
        language = student[1]
        points = int(student[2])

        if username not in students_results:
            students_results[username] = {language : points}

        elif language in students_results[username].keys():
            if students_results[username][language] < points:
                students_results[username][language] = points

        else:
            students_results[username][language] = points

        if language not in submbisions_count:
            submbisions_count[language] = 1
        else:
            submbisions_count[language] += 1

    if len(student) == 2:
        username = student[0]
        del students_results[username]

print('Results:')
for student, current_student_results in students_results.items():
    for current_language, grade in current_student_results.items():
        print(f'{student} | {grade}')

print('Submissions:')
for language, count in submbisions_count.items():
    print(f'{language} - {count}')







