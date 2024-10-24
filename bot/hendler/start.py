from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram import Router
from states.state import Islam
from aiogram.fsm.context import FSMContext
from keyboard.keyboards import Yes_no, menu, starts
from fetchs.connect import register, login, islam, vredprivichki
from states.state import Questions, All



start = Router()


#  day
@start.message(F.text=='Утренний опрос')
async def start_(message:types.Message, state:FSMContext):
    await state.set_state(All.solat_vitr) 
    question = Questions()
    await message.answer(question.solat_vitr,  reply_markup=Yes_no)


@start.message(All.solat_vitr , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(solat_vitr=True)
    await state.set_state(All.son) 
    question = Questions()
    await message.answer(question.son, reply_markup=Yes_no)

@start.message(All.solat_vitr , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(solat_vitr=False)
    await state.set_state(All.son) 
    question = Questions()
    await message.answer(question.son, reply_markup=Yes_no)

@start.message(All.son , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(son=True)
    await state.set_state(All.fadjr) 
    question = Questions()
    await message.answer(question.fadjr, reply_markup=Yes_no)

@start.message(All.son , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(son=False)
    await state.set_state(All.fadjr) 
    question = Questions()
    await message.answer(question.fadjr, reply_markup=Yes_no)


@start.message(All.fadjr , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(fadjr=True)
    await state.set_state(All.zikr_vech) 
    question = Questions()
    await message.answer(question.zikr_vech, reply_markup=Yes_no)

@start.message(All.fadjr , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(fadjr=False)
    await state.set_state(All.zikr_vech) 
    question = Questions()
    await message.answer(question.zikr_vech, reply_markup=Yes_no)


@start.message(All.zikr_vech , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_vech=True)
    data = await state.get_data()
    await state.clear() 
    
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    vred_pr = {}
    vred_pr['son'] = data.pop('son') 
    res1 = await vredprivichki(vred_pr, access_token)
    res = await islam(data, access_token)
    print(res)
    await message.answer('''Ваши данные внесены ✅\nВыберите пункт из меню 👇''', reply_markup=starts)

@start.message(All.zikr_vech , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_vech=False)
    data = await state.get_data()
    await state.clear() 
    
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    vred_pr = {}
    vred_pr['son'] = data.pop('son') 
    res1 = await vredprivichki(vred_pr, access_token)
    res = await islam(data, access_token)
    print(res)
    await message.answer('''Ваши данные внесены ✅\nВыберите пункт из меню 👇''', reply_markup=starts)

#Start
@start.message(CommandStart)
async def start_bot(message:types.Message):
    data = {
        "username": message.from_user.id,
        "password": message.from_user.id,
        "email": f"user{str(message.from_user.id)}@example.com",
        "first_name": message.from_user.username,
        "last_name": message.from_user.first_name
        }
    res = await register(data)
    print(res)
    
    await message.answer('''
        Ас саламу алеукум! 👋\n\n
        Этот бот предназначен для укрепления хороших привычек 🌱,\n
        оставления вредных привычек 🚫,\n
        Этот бот будет писать вам в 9:00 и 21:00  по Мск.⏰.\n
        Необходимо  прожать кнопки "Утренний опрос"
        \n "Вечерний опрос" 
        ответив на вопросы \n\n
        👇''' , reply_markup=starts)
