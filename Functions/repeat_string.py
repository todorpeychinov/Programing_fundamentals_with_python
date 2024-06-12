input_string = input()
number_of_repetitions = int(input())

repeat_string = lambda string_to_repeat, num_of_repetitions: string_to_repeat * number_of_repetitions

print(repeat_string(input_string, number_of_repetitions))