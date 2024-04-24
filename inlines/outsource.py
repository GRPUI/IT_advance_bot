from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

OUTSOURCE_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее",
                web_app=WebAppInfo(
                    url="https://it-advance.ru/autsorsing/"
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
