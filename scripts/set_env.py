import random
import string
import os
import sys

ENV_FILE = ".env"

def generate_password(length=16):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    if len(sys.argv) < 2:
        print("Использование: python script.py <app_image>")
        return

    app_image = sys.argv[1]  # первый аргумент командной строки после имени скрипта[web:31][web:34][web:41]

    if os.path.exists(ENV_FILE):
        print(f"Файл {ENV_FILE} уже существует, генерация пропущена.")
        return

    port = random.choice(range(8000, 8010))
    password = generate_password()

    env_content = f"""COUNTER_PORT={port}
DB_USER=counter
DB_PASS={password}
DB_HOST=db
DB_NAME=counter-db
APP_IMAGE={app_image}
"""

    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(env_content)

    print(f"Файл {ENV_FILE} успешно создан.")

if __name__ == "__main__":
    main()