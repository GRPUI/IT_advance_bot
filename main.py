import asyncpg
from asyncpg import Connection

from aiogram import Bot, Dispatcher, types, Router
from aiogram import filters

import asyncio

import dotenv
import os


dotenv.load_dotenv()


API_TOKEN = os.getenv("API_TOKEN")

router = Router()


@router.message(filters.Command("start"))
async def send_welcome(message: types.Message, bot: Bot, connection: Connection) -> None:
    await bot.send_message(message.chat.id, "Привет")


async def main() -> None:
    database = os.getenv(key="DB_NAME")
    user = os.getenv(key="POSTGRES_USER")
    password = os.getenv(key="DB_PASSWORD")
    host = os.getenv(key="DB_HOST")
    port = os.getenv(key="DB_PORT")

    connection = await asyncpg.connect(
        f"postgresql://{user}:{password}@localhost:{port}/{database}"
    )

    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)

    dp.workflow_data.update(
        {
            "connection": connection
        }
    )

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
