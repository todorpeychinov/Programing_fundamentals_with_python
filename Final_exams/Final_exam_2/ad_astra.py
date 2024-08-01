import re

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'
total_calories = 0
string_input = input()
items = []

matches = re.finditer(pattern, string_input)

for match in matches:
   item = match.group(2)
   expire_date = match.group(3)
   calories = int(match.group(4))

   total_calories += calories
   items.append([item, expire_date, calories])

total_days = total_calories // 2000

print(f"You have food to last you for: {total_days} days!")
for product, expiration_date, current_calories in items:
    print(f"Item: {product}, Best before: {expiration_date}, Nutrition: {current_calories}")
