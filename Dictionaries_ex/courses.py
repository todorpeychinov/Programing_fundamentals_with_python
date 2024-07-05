student_records = {}

while True:
    user_input = input().split(' : ')
    if user_input[0] == 'end':
        break


    course_name = user_input[0]
    student_name = user_input[1]

    if course_name not in student_records:
        student_records[course_name] = []
    student_records[course_name].append(student_name)

for course_name, list_of_students in student_records.items():
    print(f'{course_name}: {len(list_of_students)}')
    for student in list_of_students:
        print(f'-- {student}')



