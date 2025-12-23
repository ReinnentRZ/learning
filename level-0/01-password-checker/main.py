import password_checker

while True:
    user_input = input("Masukkan Password (q untuk keluar): ")
    if user_input == 'q':
        break

    result = password_checker.check_password(user_input)
    print(result)
