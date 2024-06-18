words_list = input().split()

even_words = [word for word in words_list if len(word) % 2 == 0]

print("\n".join(even_words))