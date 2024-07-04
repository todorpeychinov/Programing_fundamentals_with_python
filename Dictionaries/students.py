students = {}

while True:
    user_input = input()

    if ':' not in user_input:
        searched_course = user_input
        break

    name, ID, course = user_input.split(':')
    ID = int(ID)

    students[ID] = {'name' : name, 'course' : course}

for current_student in students:
    if students[current_student]['course'].startswith(searched_course[:3]):
        print(f"{students[current_student]['name']} - {current_student}")