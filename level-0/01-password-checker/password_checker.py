def checkdigit(user_input):
    for char in user_input:
        if char.isdigit():
            return True
    return False


def checklen(user_input):
    if len(user_input) >= 8:
        return True
    else:
        return False


def check_password(user_input):
    if checkdigit(user_input) and checklen(user_input):
        return "password kuat"
    else:
        return "password lemah"



while True:
    user_input = input("Masukkan Password: ")
    if user_input == 'q':
        break

    print(check_password(user_input))