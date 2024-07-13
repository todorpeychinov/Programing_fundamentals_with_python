morse_code_dictionary = \
    {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z"
    }

words_in_morse_code = input().split(' | ')

final_words = []

for word in words_in_morse_code:
    decoded_word = ''
    for symbol in word.split():
        decoded_word += morse_code_dictionary[symbol]
    final_words.append(decoded_word)

print(" ".join(final_words))