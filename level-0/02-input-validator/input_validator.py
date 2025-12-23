def suspicious_word(user_input):
    danger = [
        "or 1=1",
        "drop table",
        "--",
        ";",
        "'"
    ]

    for keyword in danger:
        if keyword.lower() in user_input.lower():
            return "Input berbahaya"

    return "input tidak berbahaya"
