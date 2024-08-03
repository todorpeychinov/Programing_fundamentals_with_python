import re

emoji_pattern = r'((::)|(\*\*))([A-Z][a-z]{2,})\1'
numbers_pattern = r'[0-9]'
threshold = 1
emojis = []
cool_emojis = []

text = input()

emoji_matches = re.finditer(emoji_pattern, text)
numbers_matches = re.findall(numbers_pattern, text)
if emoji_matches:
    for emoji in emoji_matches:
        emojis.append(emoji.group())

if numbers_matches:
    for number in numbers_matches:
        threshold *= int(number)

for current_emoji in emojis:
    current_threshold = 0
    for character in current_emoji:
        current_threshold += ord(character)
    if current_threshold >= threshold:
        cool_emojis.append(current_emoji)

print(f"Cool threshold: {threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojis:
    print(cool_emoji)
