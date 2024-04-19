from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Случайное число')]
],
                            resize_keyboard=True)
