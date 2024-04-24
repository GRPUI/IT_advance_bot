from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CONTACT_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Наш Telegram",
                url="https://t.me/+79537774187"
            )
        ],
        [
            InlineKeyboardButton(
                text="Наш WhatsApp",
                url="https://wa.me/+79537774187"
            )
        ],
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            ),
        ],
    ]
)
