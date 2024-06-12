def is_long_enough(password):
    return len(password) >= 6 and len(password) <= 10

def has_only_digits_and_letters(password):
    for digit in password:
        if not digit.isdigit() and not digit.isalpha():
            return False
    return True

def has_two_digits(password):
    counter = 0
    for digit in password:
        if digit.isdigit():
            counter += 1
    if counter >= 2:
        return True

def check_password(password):
    if is_long_enough(password) and has_only_digits_and_letters(password) and has_two_digits(password):
        print('Password is valid')
    if not is_long_enough(password):
        print("Password must be between 6 and 10 characters")
    if not has_only_digits_and_letters(password):
        print("Password must consist only of letters and digits")
    if not has_two_digits(password):
        print("Password must have at least 2 digits")

password = input()
check_password(password)
