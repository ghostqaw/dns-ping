from flask import Flask
import threading
import time
from ping3 import ping, verbose_ping

app = Flask(__name__)

# Функция для проверки доступности DNS серверов
def check_dns_servers():
    while True:
        verbose_ping("1.1.1.1")
        verbose_ping("8.8.8.8")
        time.sleep(5)

# Эндпоинт для проверки здоровья приложения
@app.route("/health")
def health():
    return "OK", 200

# Запуск потока для проверки DNS серверов
thread = threading.Thread(target=check_dns_servers)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
