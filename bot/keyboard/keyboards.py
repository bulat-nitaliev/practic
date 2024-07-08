from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Ислам"),
                    KeyboardButton(text="Вредные привычки"),KeyboardButton(text="Цели"),
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder='Выбирете из меню'
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

cel_create = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Создать цель")
                ]
            ],
            resize_keyboard=True,
        )