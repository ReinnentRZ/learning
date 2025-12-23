def checkdigit(user_input):
    for char in user_input:
        if char.isdigit():
            return True
    return False


def checklen(user_input):
    return len(user_input) >= 8


def check_password(user_input):
    if checkdigit(user_input) and checklen(user_input):
        return "password kuat"
    else:
        return "password lemah"
