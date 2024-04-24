from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ORDER_BACK = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            )
        ]
    ]
)

ORDER_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Отмена",
                callback_data="order"
            ),
        ],
    ]
)