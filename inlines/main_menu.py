from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MAIN_MENU_INLINE = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Услуги',
                callback_data='services'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Аутсорсинг',
                callback_data='outsource'
            ),
        ],
        [
            InlineKeyboardButton(
                text='Портфолио',
                callback_data='portfolio'
            )
        ],
        [
            InlineKeyboardButton(
                text='Контакты',
                callback_data='contacts'
            )
        ],
        [
            InlineKeyboardButton(
                text="Я ХОЧУ САЙТ❗️",
                callback_data="order"
            )
        ]
    ]
)
