import input_validator

while True:
    user_input = input("Masukkan input: ")
    if user_input == 'q':
        break

    result = (input_validator.suspicious_word(user_input))
    print(result)