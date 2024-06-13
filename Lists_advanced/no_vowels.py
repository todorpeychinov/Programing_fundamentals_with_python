def remove_vowels(string_with_vowels):
    vowels = ['a', 'o', 'u', 'e', 'i']
    result_string = [char for char in string_with_vowels if char.lower() not in vowels]
    return "".join(result_string)

string_input = input()
print(remove_vowels(string_input))