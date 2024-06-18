def add(lesson_title, schedule):
    if lesson_title not in schedule:
        schedule.append(lesson_title)


def insert(lesson_title, index, schedule):
    if lesson_title not in schedule:
        schedule.insert(index, lesson_title)


def remove(lesson_title, schedule):
    exercise = f"{lesson_title}-Exercise"

    if lesson_title in schedule:
        schedule.remove(lesson_title)

    if exercise in schedule:
        schedule.remove(exercise)


def swap(lesson_title_1, lesson_title_2, schedule):
    lesson_exercise_1 = f"{lesson_title_1}-Exercise"
    lesson_exercise_2 = f"{lesson_title_2}-Exercise"

    if lesson_title_1 in schedule and lesson_title_2 in schedule:
        index_1 = schedule.index(lesson_title_1)
        index_2 = schedule.index(lesson_title_2)
        schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]

    if lesson_exercise_1 in schedule:
        schedule.remove(lesson_exercise_1)
        schedule.insert(schedule.index(lesson_title_1) + 1, lesson_exercise_1)

    if lesson_exercise_2 in schedule:
        schedule.remove(lesson_exercise_2)
        schedule.insert(schedule.index(lesson_title_2) + 1, lesson_exercise_2)


def add_exercise(lesson_title, schedule):
    exercise = f"{lesson_title}-Exercise"

    if lesson_title in schedule:
        index = schedule.index(lesson_title)
        if exercise not in schedule:
            schedule.insert(index + 1, exercise)
    else:
        schedule.append(lesson_title)
        schedule.append(exercise)


def process_commands(commands, initial_schedule):
    for command in commands:
        command_list = command.split(':')
        current_command = command_list[0]

        if current_command == 'Add':
            lesson_title = command_list[1]
            add(lesson_title, initial_schedule)

        elif current_command == 'Insert':
            lesson_title = command_list[1]
            index = int(command_list[2])
            insert(lesson_title, index, initial_schedule)

        elif current_command == 'Remove':
            lesson_title = command_list[1]
            remove(lesson_title, initial_schedule)

        elif current_command == 'Swap':
            lesson_title_1 = command_list[1]
            lesson_title_2 = command_list[2]
            swap(lesson_title_1, lesson_title_2, initial_schedule)

        elif current_command == 'Exercise':
            lesson_title = command_list[1]
            add_exercise(lesson_title, initial_schedule)

    return initial_schedule





schedule = input().split(', ')
commands = []

while True:
    command = input()
    if command == 'course start':
        break

    else:
        commands.append(command)

final_schedule = process_commands(commands, schedule)
for index, lesson in enumerate(final_schedule, 1):
    print(f'{index}.{lesson}')


