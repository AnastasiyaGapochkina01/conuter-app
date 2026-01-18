import sys
import requests 

def main():
    if len(sys.argv) < 4:
        print("Использование: python notify.py <bot_token> <chat_id> <message>")
        return

    bot_token = sys.argv[1]
    chat_id = sys.argv[2]
    message = " ".join(sys.argv[3:])

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }

    response = requests.get(url, params=params)
    if response.ok:
        print("Уведомление отправлено.")
    else:
        print("Ошибка отправки:", response.status_code, response.text)

if __name__ == "__main__":
    main()
