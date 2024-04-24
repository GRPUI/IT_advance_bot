from aiogram import Bot, Dispatcher, types, Router
from aiogram import filters
from aiogram.fsm.context import FSMContext

from services.order import validate_phone_number

import asyncio

import dotenv
import os

from aiogram.types import Message

from inlines import MAIN_MENU_INLINE, SERVICES_MENU, OUTSOURCE_MENU, PORTFOLIO_MENU, CONTACT_MENU, ORDER_MENU
from inlines.order import ORDER_BACK

from states.order import OrderSteps

dotenv.load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

router = Router()


@router.message(filters.Command("start"))
async def send_welcome(
        message: types.Message,
        bot: Bot,
) -> None:
    await bot.send_message(
        message.chat.id,
        """🌟 Здравствуйте! 👋 \n         
IT-Advance - ваш лучший партнер в IT-решениях! 🌟\n
Мы создаем первоклассные IT-продукты для автоматизации вашей работы в клиентском сервисе, продажах, маркетинге и других процессах в вашей компании. 💻""",
        reply_markup=MAIN_MENU_INLINE,
        parse_mode="Markdown"
    )


@router.message(OrderSteps.GET_NAME)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        f"Отлично, теперь напишите *Ваш* номер:",
        reply_markup=ORDER_MENU,
        parse_mode="Markdown"
    )
    await state.set_state(OrderSteps.GET_NUMBER)


@router.message(OrderSteps.GET_NUMBER)
async def get_name(message: Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()
    if validate_phone_number(message.text):
        name = user_data["name"]
        await message.answer(
            f"Ваше имя: *{name}*\n"
            f"Ваш номер: *{message.text}*\n\n"
            f"Мы свяжемся с Вами",
            parse_mode="Markdown"
        )
        await bot.send_message(
            506368232,
            f"Имя: {name}\n\n"
            f"Номер: {message.text}"
        )
    else:
        await message.answer(f"Введите корректный номер")


@router.callback_query()
async def callback_handler(
        callback_query: types.CallbackQuery,
        state: FSMContext
):
    data = callback_query.data

    if data == "services":
        await callback_query.message.edit_text("""*Улучшите свой онлайн-бизнес с нашими коробочными решениями! *\n
*Мы специализируемся на:*
🛠️ Разработке сайтов
🎨 Веб-дизайне
🛍️ Электронной торговле
🏷️ Брендинге
📈 Маркетинге
🎯 Контекстной рекламе
🎯 Таргетированной рекламе""",
                                               reply_markup=SERVICES_MENU,
                                               parse_mode="Markdown")
    elif data == "outsource":
        await callback_query.message.edit_text(
            "*Мы оказываем следующие виды аутсорсинга:*\n\n"
            "🔄 Единовременный: миграция в облако, настройка ПО, монтаж оборудования, инвентаризация, составление плана "
            "лицензирования, автоматизации и др.\n\n"
            "🔄 На постоянной основе: обслуживание офисной техники и компьютеров, "
            "мониторинг работы и администрирование серверного и сетевого оборудования, "
            "выявление и устранение неисправностей, работа по заявкам на инциденты, ИТ поддержка.",
            reply_markup=OUTSOURCE_MENU,
            parse_mode="Markdown"
        )
    elif data == "portfolio":
        await callback_query.message.edit_text(
            "Наша команда разрабатывает *сайты и IT-решения*,"
            " которые помогают нашим клиентам достичь своих бизнес-целей.\n\n"
            "Ознакомьтесь с нашими работами нажав на кнопку ⬇️⬇️⬇️",
            reply_markup=PORTFOLIO_MENU,
            parse_mode="Markdown"
        )
    elif data == "contacts":
        await callback_query.message.edit_text(
            "Свяжитесь с нами 👋\n\n"
            "📞 *Наш номер:* +78003008524\n"
            "📧 *Наш email:* info@itadvance.company",
            reply_markup=CONTACT_MENU,
            parse_mode="Markdown"
        )
    elif data == "order":
        await state.clear()
        await callback_query.message.edit_text(
            "Отлично, как *Вас* зовут?",
            reply_markup=ORDER_BACK,
            parse_mode="Markdown"
        )
        await state.set_state(OrderSteps.GET_NAME)
    elif data == "main_menu":
        await state.clear()
        await callback_query.message.edit_text(
            """*Здравствуйте!* 👋 \n         
⭐ IT-Advance - ваш лучший партнер в IT-решениях!\n
⭐ Мы создаем первоклассные IT-продукты для автоматизации вашей работы в клиентском сервисе, продажах, маркетинге и других процессах в вашей компании. 💻""",
            reply_markup=MAIN_MENU_INLINE,
            parse_mode="Markdown"
        )


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
