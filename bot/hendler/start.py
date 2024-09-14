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
@start.message(F.text=='Start')
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
    await state.set_state(All.zikr_ut) 
    question = Questions()
    await message.answer(question.zikr_ut, reply_markup=Yes_no)

@start.message(All.fadjr , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(fadjr=False)
    await state.set_state(All.zikr_ut) 
    question = Questions()
    await message.answer(question.zikr_ut, reply_markup=Yes_no)


@start.message(All.zikr_ut , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=True)
    await state.set_state(All.tauba) 
    question = Questions()
    await message.answer(question.tauba, reply_markup=Yes_no)

@start.message(All.zikr_ut , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=False)
    await state.set_state(All.tauba) 
    question = Questions()
    await message.answer(question.tauba, reply_markup=Yes_no)

@start.message(All.tauba , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=True)
    await state.set_state(All.telefon) 
    question = Questions()
    await message.answer(question.telefon, reply_markup=Yes_no)

@start.message(All.tauba , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=False)
    await state.set_state(All.telefon) 
    question = Questions()
    await message.answer(question.telefon, reply_markup=Yes_no)


@start.message(All.telefon , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=True)
    await state.set_state(All.haram) 
    question = Questions()
    await message.answer(question.haram, reply_markup=Yes_no)

@start.message(All.telefon , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=False)
    await state.set_state(All.haram) 
    question = Questions()
    await message.answer(question.haram, reply_markup=Yes_no)


@start.message(All.haram , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(haram=True)
    await state.set_state(All.eda) 
    question = Questions()
    await message.answer(question.eda, reply_markup=Yes_no)

@start.message(All.haram , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(haram=False)
    await state.set_state(All.eda) 
    question = Questions()
    await message.answer(question.eda, reply_markup=Yes_no)


@start.message(All.eda , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(eda=True)
    data = await state.get_data()
    await state.clear() 
    islam_data, vred_pr = {}, {}
    islam_data.update(data)
    vred_pr['eda'] = islam_data.pop('eda') 
    vred_pr['telefon'] = islam_data.pop('telefon')    
    vred_pr['haram'] = islam_data.pop('haram')       
    print(islam_data)
    print(vred_pr)
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await islam(islam_data, access_token)
    res1 = await vredprivichki(vred_pr, access_token)
    print(res)
    await message.answer('''Ваши данные внесены ✅\nВыберите пункт из меню 👇''', reply_markup=starts)

@start.message(All.eda , F.text == "❌ Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(eda=False)
    data = await state.get_data()
    await state.clear() 
    islam_data, vred_pr = {}, {}
    islam_data.update(data)
    vred_pr['eda'] = islam_data.pop('eda') 
    vred_pr['telefon'] = islam_data.pop('telefon')    
    vred_pr['haram'] = islam_data.pop('haram')       
    print(islam_data)
    print(vred_pr)
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await islam(islam_data, access_token)
    res1 = await vredprivichki(vred_pr, access_token)
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
        Необходимо  прожать кнопку "Start" \n
        ответив на вопросы \n\n
        👇''' , reply_markup=starts)
