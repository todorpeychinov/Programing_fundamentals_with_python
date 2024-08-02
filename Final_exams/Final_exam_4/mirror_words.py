import re

pattern = r'([@|#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

user_input = input()

mirror_words = []

matches = re.findall(pattern, user_input)

for match in matches:
    word_1 = match[1]
    word_2 = match[2]

    if word_1 == word_2[::-1]:
        mirror_words.append((word_1, word_2))

if not matches:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print('The mirror words are:')
    result_string = ''
    for pair in mirror_words:
        result_string += f"{pair[0]} <=> {pair[1]}, "
    result_string = result_string[:-2]
    print(result_string)
