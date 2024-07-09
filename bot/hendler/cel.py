from aiogram import Router, F, types
from keyboard.keyboards import  cel_create, inl_cel
from fetchs.connect import  login, cel_list, create_cel, create_comment, destroy_cel
from aiogram.fsm.context import FSMContext
from states.state import Cel, Comment


cel = Router()

#cb
@cel.callback_query(F.data == 'comment')
async def add_comment(cb:types.CallbackQuery, state:FSMContext):
    id = cb.message.text.split()
    c = cb.message.text.split('"')
    await state.update_data(id=id[-1])
    await state.set_state(Comment.body)
    print(id[-1], c[1])
    await cb.answer('ssssssss')
    await cb.message.answer(f'Что вы сделали для  достижения - "{c[1]}" напишите ваши действия')

@cel.callback_query(F.data == 'delete_cel')
async def del_cel(cb:types.CallbackQuery):
    await cb.answer('ssssssss')
    id = cb.message.text.split()
    c = cb.message.text.split('"')
    dt = {
        "username": str(cb.from_user.id),
        "password": str(cb.from_user.id)
        }
    access_token = await login(dt)
    res = await destroy_cel(id[-1],access_token)
    print(res)

    await cb.message.answer(f'Цель - "{c[1]}" успешно удалена')
    

#Цели
@cel.message(F.text=='Цели')
async def key_cel(message:types.Message):
    await message.answer('Выбирете из меню кнопок', reply_markup=cel_create)


@cel.message(F.text=='Создать цель')
async def cr_cel(message:types.Message, state:FSMContext):
    await state.set_state(Cel.cel_state)
    await message.answer('Создайте цель - напишите  вашу цель', reply_markup=types.ReplyKeyboardRemove())




@cel.message(F.text=='Посмотреть список целей')
async def start_cel(message:types.Message, state:FSMContext):
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await cel_list(access_token) 
    if res['results']:
        for cel in res['results']:                   
            await message.answer(f'''Ваша цель - "{cel['name']}": 
                                {', '.join(cel['comment'])} {cel['id']}''',
                                reply_markup=inl_cel)  
    else:
        await state.set_state(Cel.cel_state)
        await message.answer('Создайте цель - напишите  вашу цель', reply_markup=types.ReplyKeyboardRemove())

  
@cel.message(Cel.cel_state)
async def cel_creat(message:types.Message, state:FSMContext):
    name = message.text
    await state.clear()
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await create_cel({'name': name}, access_token)
    await message.answer(f'''Вы создали цель - {name} 
    Выбирете из меню кнопок''', reply_markup=cel_create)



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
    await message.answer('Выбирете из меню кнопок', reply_markup=cel_create)



