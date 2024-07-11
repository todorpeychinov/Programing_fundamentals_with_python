banned_words = input().split(', ')
input_text = input()

for word in banned_words:
    input_text = input_text.replace(word, len(word) * '*')

print(input_text)