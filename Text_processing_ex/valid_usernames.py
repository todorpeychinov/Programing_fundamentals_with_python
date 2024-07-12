def check_length(username_):
    if 3 <= len(username_) <= 16:
        return True
    return False


def check_characters(username_):
    for character in username_:
        if not(character.isalnum() or character == '-' or character == '_'):
            return False
    return True


def is_redundant(username_):
    if ' ' in username_:
        return True
    return False


def is_valid_username(username_):
    if check_length(username) and check_characters(username) and not is_redundant(username):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if is_valid_username(username):
        print(username)
