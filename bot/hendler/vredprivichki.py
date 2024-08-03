from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from states.state import Vred
from keyboard.keyboards import Yes_no, menu
from fetchs.connect import  login, vredprivichki


vred = Router()

#Вредные привычки
@vred.message(F.text=='Вредные привычки')
async def start(message:types.Message, state:FSMContext):
    await state.set_state(Vred.son) 
    await message.answer('Вовремя вчера легли спать(до 23:00)', reply_markup=Yes_no)

#Vred.son
@vred.message(Vred.son , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(son=True)
    await state.set_state(Vred.telefon) 
    await message.answer('Сегодня много проводили времени в телефоне(youtube, instagram, tg)', reply_markup=Yes_no)

@vred.message(Vred.son , F.text == "Нет")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(son=False)
    await state.set_state(Vred.telefon) 
    await message.answer('Сегодня много проводили времени в телефоне(youtube, instagram, tg)', reply_markup=Yes_no)

#Vred.telefon
@vred.message(Vred.telefon , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=True)
    await state.set_state(Vred.haram) 
    await message.answer('Сегодня смотрели на харам("запретное"- ели, слушали, ходили)', reply_markup=Yes_no)

@vred.message(Vred.telefon , F.text == "Нет")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=False)
    await state.set_state(Vred.haram) 
    await message.answer('Сегодня смотрели на харам("запретное"- ели, слушали, ходили)', reply_markup=Yes_no)

#Vred.haram
@vred.message(Vred.haram , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(haram=True)
    await state.set_state(Vred.eda) 
    await message.answer('Сегодня приходилось объедаться(съесть лишнего)', reply_markup=Yes_no)

@vred.message(Vred.haram , F.text == "Нет")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(haram=False)
    await state.set_state(Vred.eda) 
    await message.answer('Сегодня приходилось объедаться(съесть лишнего)', reply_markup=Yes_no)

#Vred.eda
@vred.message(Vred.eda , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(eda=True)
    data = await state.get_data() 
    await state.clear() 
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await vredprivichki(data, access_token)
    await message.answer('''Ваши данные внесены
                         Выбирете из меню кнопок''', reply_markup=menu)

@vred.message(Vred.eda , F.text == "Нет")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(eda=False)
    data = await state.get_data() 
    await state.clear() 
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    
    res = await vredprivichki(data, access_token)
    
    await message.answer('''Ваши данные внесены
                         Выбирете из меню кнопок''', reply_markup=menu)