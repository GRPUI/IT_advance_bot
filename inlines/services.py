from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

SERVICES_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее",
                web_app=WebAppInfo(
                    url="https://it-advance.ru/services/"
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            ),
        ],
    ]
)
