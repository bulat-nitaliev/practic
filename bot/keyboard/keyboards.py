from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="🕌 Ислам"),
                    KeyboardButton(text="🚫 Вредные привычки"),KeyboardButton(text="🎯 Цели"),
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder='Выбирете из меню'
        )


Yes_no = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="✅ Да"),
                    KeyboardButton(text="❌ Нет"),
                ]
            ],
            resize_keyboard=True,
        )

starts = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Start"),
                ]
            ],
            resize_keyboard=True,
            input_field_placeholder='Нажмите кнопку Start'
        )

cel_create = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Создать цель"),
                    KeyboardButton(text="Посмотреть список целей"),
                ],
                [
                    KeyboardButton(text="🕌 Ислам"),
                    KeyboardButton(text="🚫 Вредные привычки"),KeyboardButton(text="🎯 Цели"),
                ]
            ],
            resize_keyboard=True,
        )

inl_cel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Цель выполнена(удаляем)', callback_data='delete_cel_'),
     InlineKeyboardButton(text='Написать комментарий', callback_data='comment_'),]
])

async def cel_list_inline(res:list)->InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    for cel in res["results"]:
        builder.add(InlineKeyboardButton(text=f'''Ваша цель - "{cel['name']}": 
                                {cel['comment']}''', callback_data=f'{cel["id"]}'))
    return builder.adjust(1).as_markup()