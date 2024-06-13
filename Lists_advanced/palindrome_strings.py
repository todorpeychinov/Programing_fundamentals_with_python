def create_list_of_palindromes(list_of_words):
    palindromes = [word for word in list_of_words if word == word[::-1]]
    return palindromes

def word_counter(word, list_of_words):
    counter = 0
    for current_word in list_of_words:
        if current_word == word:
            counter += 1
    return counter

list_of_words = input().split()
searched_palindrome = input()

palindromes_list = create_list_of_palindromes(list_of_words)
searched_palindrome_counter = word_counter(searched_palindrome, palindromes_list)

print(palindromes_list)
print(f'Found palindrome {searched_palindrome_counter} times')