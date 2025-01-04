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

async def get_chat_users(chat_name):
    """Получить список пользователей из чата/паблика."""
    try:
        async with client:
            # Получаем объект чата
            chat = await client.get_entity(chat_name)

            # Получаем список пользователей
            participants = await client.get_participants(chat)
            print(f"Участники чата '{chat_name}':")
            for user in participants:
                print(f"{user.id} - {user.first_name} {user.last_name}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Укажите название чата/паблика
chat_name = input("Введите ссылку или название чата/паблика: ")
client.loop.run_until_complete(get_chat_users(chat_name))