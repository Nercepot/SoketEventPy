import parsTokens
import socketio
import json
from mcrcon import MCRcon
from LogicParser import ip, password, port, promo, twich_price, price, price_promo
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат логов
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    handlers=[
        logging.StreamHandler(),  # Логи в консоль
        logging.FileHandler("donation_alerts.log", mode="a")  # Логи в файл
    ]
)

# Загружаем токены из YAML файла
tokens = parsTokens.load_tokens_from_yaml('token.yml')

# Логируем загруженные токены
logging.info(f"Загруженные токены: {tokens}")

# Создаем подключение к серверу Minecraft
mc = MCRcon(ip, password, port=port)

# Создаем клиента для сокет-соединения
sio = socketio.Client()

# Множество для хранения обработанных ID донатов
processed_donations = set()


# Функция для подключения с перебором токенов
def connect_with_tokens():
    for token in tokens:
        if not token or token == "0":
            logging.warning(f"Пропускаем токен: {token}")
            continue

        try:
            # Подключаемся с каждым токеном
            logging.info(f"Попытка подключения с токеном: {token}")

            # Обработчик подключения к WebSocket
            @sio.on('connect')
            def on_connect():
                logging.info(f"Подключено к WebSocket серверу с токеном {token}")
                # Отправляем запрос на добавление пользователя с текущим токеном
                sio.emit('add-user', {"token": token, "type": "alert_widget"})
                logging.info(f"Отправлен запрос на добавление пользователя с токеном {token}")

            # Обработчик получения донатов
            @sio.on('donation')
            def on_message(data):
                logging.info(f"Получено сообщение от WebSocket: {data}")
                try:
                    # Преобразуем данные из JSON
                    y = json.loads(data)
                    username = y['username']
                    amount = float(y['amount'])
                    currency = y['currency']
                    message = y['message']
                    donation_id = y['id']  # Получаем уникальный ID доната
                    is_test_alert = y.get('_is_test_alert', False)  # Проверка на тестовый донат

                    # Пропускаем тестовый донат или если донат уже был обработан
                    if is_test_alert:
                        logging.info(f"Пропускаем тестовый донат от {username}")
                        return
                    if donation_id in processed_donations:
                        logging.info(f"Донат от {username} с ID {donation_id} уже был обработан, пропускаем.")
                        return

                    # Добавляем ID доната в множество обработанных
                    processed_donations.add(donation_id)

                    logging.info(f"Получено сообщение: {y}")

                    # Формируем команду для Minecraft
                    if message == promo:
                        if amount == price_promo:
                            command = f"whitelistbytime add {username} 1mo"
                            logging.info(f"Команда для {username}: {command}")
                            mc.command(command)
                        elif amount == price:
                            command = f"whitelistbytime add {username} 1mo"
                            logging.info(f"Команда для {username}: {command}")
                            mc.command(command)
                        elif amount == twich_price and currency == "USD":
                            command = f"whitelistbytime add {username} 1mo"
                            logging.info(f"Команда для {username}: {command}")
                            mc.command(command)

                except Exception as e:
                    logging.error(f"Ошибка обработки доната: {e}")

            # Подключаемся к WebSocket
            sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')

            # Ждем событий от WebSocket (это блокирует основной поток)
            sio.wait()

        except Exception as e:
            logging.error(f"Ошибка подключения с токеном {token}: {e}")
            continue  # Пытаемся подключиться с другим токеном


# Подключаемся к серверу Minecraft
mc.connect()
logging.info("Подключение к серверу Minecraft успешно")

# Подключаемся с токенами
connect_with_tokens()
