import os

keywords = ["db_user", "db_password", "jwt_token"]

def scan_file(filename, keywords):
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            for keyword in keywords:
                if keyword in line:
                    print(f"[{keyword}] ditemukan di baris {line_number}: {line.strip()}")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "datafile.txt")

scan_file(FILE_PATH, keywords)


