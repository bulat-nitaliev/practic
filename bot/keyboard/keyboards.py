from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Ислам"),
                    KeyboardButton(text="Вредные привычки"),KeyboardButton(text="Цели"),
                ]
            ],
            resize_keyboard=True,
        )


Yes_no = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Да"),
                    KeyboardButton(text="Нет"),
                ]
            ],
            resize_keyboard=True,
        )