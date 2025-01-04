from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

# Введите свои данные API
API_ID = '20638371'
API_HASH = '3209386a83cff2bade05a9b991f4d79a'
PHONE = '+380967162675'

# Инициализация клиента
client = TelegramClient('session_name', API_ID, API_HASH)
client.start()

async def send_message(receiver, message):
    """Отправить сообщение пользователю или в чат."""
    try:
        async with client:
            # Получаем объект получателя
            receiver_entity = await client.get_entity(receiver)

            # Отправляем сообщение
            await client.send_message(receiver_entity, message)
            print(f"Сообщение отправлено: {message}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Укажите получателя и сообщение
receiver = input("Введите пользователя/чат: ")
message = input("Введите сообщение: ")
client.loop.run_until_complete(send_message(receiver, message))