students = {}

number_of_students = int(input())

for student in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

students_with_average_grade = {student_name: sum(grades) / len(grades) for student_name, grades in students.items() if sum(grades) / len(grades) >= 4.5}

for current_student, avg_grade in students_with_average_grade.items():
    print(f"{current_student} -> {avg_grade:.2f}")
