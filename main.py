from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Главное меню
def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("О школе", callback_data='about_school')],
        [InlineKeyboardButton("Позвать оператора", callback_data='call_operator')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Меню "О школе"
def about_school_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Предоставляемые услуги", callback_data='services')],
        [InlineKeyboardButton("Информация о каникулах", callback_data='holidays')],
        [InlineKeyboardButton("Об \"отработках\" пропусков", callback_data='makeup_classes')],
        [InlineKeyboardButton("Об оплате", callback_data='payment')],
        [InlineKeyboardButton("Важные ссылки", callback_data='important_links')],
        [InlineKeyboardButton("О \"Третьем месте\"", callback_data='about_third_place')],
        [InlineKeyboardButton("Вернуться назад", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Меню "О каникулах"
def holidays_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Летние каникулы", callback_data='summer_holidays')],
        [InlineKeyboardButton("Весенние каникулы", callback_data='spring_holidays')],
        [InlineKeyboardButton("Осенние каникулы", callback_data='autumn_holidays')],
        [InlineKeyboardButton("Зимние каникулы", callback_data='winter_holidays')],
        [InlineKeyboardButton("Вернуться назад", callback_data='about_school')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Меню "Предоставляемые услуги"
def services_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Индивидуальные занятия", callback_data='individual_lessons')],
        [InlineKeyboardButton("Групповые занятия", callback_data='group_lessons')],
        [InlineKeyboardButton("Хакатоны", callback_data='hackathons')],
        [InlineKeyboardButton("Стажировки", callback_data='internships')],
        [InlineKeyboardButton("Клуб", callback_data='club')],
        [InlineKeyboardButton("Вернуться назад", callback_data='about_school')]
    ]
    return InlineKeyboardMarkup(keyboard)

# Функция для приветственного сообщения
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Добро пожаловать в школу 'Третье место'! "
        "Я бот техподдержки, и я здесь, чтобы помочь вам. Вы можете использовать кнопки ниже, чтобы получить нужную информацию.",
        reply_markup=main_menu_keyboard(),
    )


# Функция для предоставления информации о компании
async def about_school(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Выберите интересующую вас информацию:",
        reply_markup=about_school_menu_keyboard()
    )

# Функции для обработки конкретных запросов в меню "О школе"
async def services(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Выберите интересующую вас услугу:",
        reply_markup=services_menu_keyboard()
    )


async def holidays(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Выберите тип каникул:",
        reply_markup=holidays_menu_keyboard()
    )


async def makeup_classes(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Об 'отработках' пропусков: Пропущенные занятия можно отработать в следующие даты...",
        reply_markup=about_school_menu_keyboard()
    )


async def payment(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Об оплате: Оплата производится через ...",
        reply_markup=about_school_menu_keyboard()
    )


async def important_links(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Важные ссылки: [Наш сайт](https://example.com)",
        reply_markup=about_school_menu_keyboard()
    )


async def about_third_place(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "О 'Третьем месте': Школа 'Третье место' - это место, где каждый ученик получает индивидуальное внимание и поддержку.",
        reply_markup=about_school_menu_keyboard()
    )


# Функция для обработки кнопки "Позвать оператора"
async def call_operator(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Если вы не нашли ответы на интересующие вас вопросы, пожалуйста, обратитесь к нашему оператору: [Позвать оператора](https://t.me/Sc_sort_bot)",
        reply_markup=main_menu_keyboard()
    )


# Функция для обработки нажатий кнопок
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data

    if data == 'about_school':
        await about_school(update, context)
    elif data == 'call_operator':
        await call_operator(update, context)
    elif data == 'services':
        await services(update, context)
    elif data == 'holidays':
        await holidays(update, context)
    elif data == 'makeup_classes':
        await makeup_classes(update, context)
    elif data == 'payment':
        await payment(update, context)
    elif data == 'important_links':
        await important_links(update, context)
    elif data == 'about_third_place':
        await about_third_place(update, context)
    elif data == 'main_menu':
        await query.edit_message_text(
            "Вы вернулись в главное меню.",
            reply_markup=main_menu_keyboard()
        )


# Основная функция для запуска бота
def main() -> None:
    # Вставьте свой токен здесь
    application = Application.builder().token("7380678860:AAHg0c12KXSkj3_kZRDNSH2kUkzdQQKd2vs").build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))

    # Обработчик нажатий кнопок
    application.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    application.run_polling()


if __name__ == '__main__':
    main()
