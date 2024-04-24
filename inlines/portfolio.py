from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

PORTFOLIO_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подробнее",
                web_app=WebAppInfo(
                    url="https://it-advance.ru/portfolio/"
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
