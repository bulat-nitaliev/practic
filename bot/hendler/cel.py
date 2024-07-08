from aiogram import Router, F, types
from keyboard.keyboards import Yes_no, menu, cel_create
from fetchs.connect import  login, cel_list, create_cel, create_comment
from aiogram.fsm.context import FSMContext
from states.state import Cel, Comment


cel = Router()

#Цели
@cel.message(F.text=='Цели')
async def start_cel(message:types.Message, state:FSMContext):
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await cel_list(access_token) 
    if res['results']:
        for cel in res['results']:
            await state.update_data(id=cel['id'])
            await state.set_state(Comment.body)
            await message.answer(f'Ваша цель - "{cel['name']}" \n Что сегодня вы сделали для её достижения - напишите коментарий', reply_markup=types.ReplyKeyboardRemove())
    else:
        await state.set_state(Cel.cel_state)
        await message.answer('Создайте цель - напишите  вашу цель', reply_markup=types.ReplyKeyboardRemove())

@cel.message(Cel.cel_state)
async def cel_create(message:types.Message):
    name = message.text
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await create_cel({'name': name}, access_token)
    await message.answer(f'Вы создали цель - {name} {res}', reply_markup=types.ReplyKeyboardRemove())

@cel.message(Comment.body)
async def comment(message:types.Message, state:FSMContext):
    body = message.text
    await state.update_data(body=body)
    data = await state.get_data()
    print(data)
    await state.clear()
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await create_comment({'body': data['body'], 'cel':data['id']}, access_token)
    print(res)


