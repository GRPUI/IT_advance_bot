from aiogram import Bot, Dispatcher, types, Router
from aiogram import filters
from aiogram.fsm.context import FSMContext

from services.order import validate_phone_number

import asyncio

import dotenv
import os

from aiogram.types import Message, InputFile

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
    photo = types.FSInputFile("2.png")
    await bot.send_photo(
        message.chat.id,
        photo,
        caption="""🌟 *Здравствуйте\! *👋 \n         
*IT\-Advance* \- ваш лучший партнер в IT\-решениях\! 🌟\n
Мы создаем первоклассные IT\-продукты для автоматизации вашей работы в клиентском сервисе, продажах, маркетинге и других процессах в вашей компании\. 💻""",
        reply_markup=MAIN_MENU_INLINE,
        parse_mode="MarkdownV2"
    )


@router.message(OrderSteps.GET_NAME)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        f"Отлично, теперь напишите *Ваш* номер в формате:\n"
        f"*\+78003008524* или *88003008524*",
        reply_markup=ORDER_MENU,
        parse_mode="MarkdownV2"
    )
    await state.set_state(OrderSteps.GET_NUMBER)


@router.message(OrderSteps.GET_NUMBER)
async def get_name(message: Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()
    if validate_phone_number(message.text):
        name = user_data["name"]
        text = message.text.replace("+", "\+")
        await message.answer(
            f"```IT\-ADVANCE```\nМы рады, что *Вы* обратились к нам\.\n\n"
            f"Ваше имя: {name}\n"
            f"Ваш номер: {text}\n\n"
            f"Мы свяжемся с *Вами* в ближайшее время\.",
            parse_mode="MarkdownV2"
        )
        await bot.send_message(
            -4102002390,
            f"```IT\-ADVANCE``` \n"
            f"Новая заявка на обратный звонок\.\n"
            f"Имя: *{name}*\n\n"
            f"Номер: *{text}*",
            parse_mode="MarkdownV2"
        )
    else:
        await message.answer(f"Введите корректный номер")


@router.callback_query()
async def callback_handler(
        callback_query: types.CallbackQuery,
        state: FSMContext
):
    message_id = str(callback_query.message.message_id)
    data = callback_query.data

    if data == "services":
        await callback_query.message.edit_caption(message_id, """*Улучшите свой онлайн\-бизнес с нашими коробочными решениями\! *\n
*Мы специализируемся на:*
🛠️ Разработке сайтов
🎨 Веб\-дизайне
🛍️ Электронной торговле
🏷️ Брендинге
🤖 Разработке telegram\-ботов
📈 Маркетинге
🎯 Контекстной рекламе
🎯 Таргетированной рекламе""",
                                                  reply_markup=SERVICES_MENU,
                                                  parse_mode="MarkdownV2")
    elif data == "outsource":
        await callback_query.message.edit_caption(message_id,
            "*Мы оказываем следующие виды аутсорсинга:*\n\n"
            "🔄 Единовременный: миграция в облако, настройка ПО, монтаж оборудования, инвентаризация, составление плана "
            "лицензирования, автоматизации и др\.\n\n"
            "🔄 На постоянной основе: обслуживание офисной техники и компьютеров, "
            "мониторинг работы и администрирование серверного и сетевого оборудования, "
            "выявление и устранение неисправностей, работа по заявкам на инциденты, ИТ поддержка\.",
            reply_markup=OUTSOURCE_MENU,
            parse_mode="MarkdownV2"
        )
    elif data == "portfolio":
        await callback_query.message.edit_caption(message_id,
            "Наша команда разрабатывает *сайты и IT\-решения*\,"
            " которые помогают нашим клиентам достичь своих бизнес\-целей\.\n\n"
            "Ознакомьтесь с нашими работами нажав на кнопку ⬇️⬇️⬇️",
            reply_markup=PORTFOLIO_MENU,
            parse_mode="MarkdownV2"
        )
    elif data == "contacts":
        await callback_query.message.edit_caption(message_id,
            "Свяжитесь с нами 👋\n\n"
            "📞 *Наш номер:* \+78003008524\n"
            "📧 *Наш email:* info@itadvance\.company",
            reply_markup=CONTACT_MENU,
            parse_mode="MarkdownV2"
        )
    elif data == "order":
        await state.clear()
        await callback_query.message.edit_caption(message_id,
            "Отлично, как *Вас* зовут?",
            reply_markup=ORDER_BACK,
            parse_mode="MarkdownV2"
        )
        await state.set_state(OrderSteps.GET_NAME)
    elif data == "main_menu":
        await state.clear()
        await callback_query.message.edit_caption(message_id,
            """ *Здравствуйте\! *👋 \n         
*IT\-Advance* \- ваш лучший партнер в IT\-решениях\! 🌟\n
Мы создаем первоклассные IT\-продукты для автоматизации вашей работы в клиентском сервисе, продажах, маркетинге и других процессах в вашей компании\. 💻""",
            reply_markup=MAIN_MENU_INLINE,
            parse_mode="MarkdownV2"
        )


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=API_TOKEN)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
