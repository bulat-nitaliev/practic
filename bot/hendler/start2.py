from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram import Router
from states.state import Islam
from aiogram.fsm.context import FSMContext
from keyboard.keyboards import Yes_no, menu, starts
from fetchs.connect import register, login, islam, vredprivichki
from states.state import Questions, All



start2 = Router()


#  day
@start2.message(F.text=="Вечерний опрос")
async def start_22222(message:types.Message, state:FSMContext):
    await state.set_state(All.quran) 
    question = Questions()
    await message.answer(question.quran, reply_markup=types.ReplyKeyboardRemove())


@start2.message(All.quran)
async def start1(message:types.Message, state:FSMContext):   
    count = message.text
    if count.isdigit():
        await state.update_data(quran=int(count))
        await state.set_state(All.solat_duha) 
        
        question = Questions()
        await message.answer(question.solat_duha, reply_markup=Yes_no)
    else:
        await message.answer('Введите число')


@start2.message(All.solat_duha , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(solat_duha=True)
    await state.set_state(All.mechet_fard) 
    question = Questions()
    await message.answer(question.mechet_fard, reply_markup=Yes_no)

@start2.message(All.solat_duha , F.text == "❌ Нет")
async def start2_8(message:types.Message, state:FSMContext):   
    await state.update_data(solat_duha=False)
    await state.set_state(All.mechet_fard) 
    question = Questions()
    await message.answer(question.mechet_fard, reply_markup=Yes_no)


@start2.message(All.mechet_fard , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(mechet_fard=True)
    await state.set_state(All.tauba) 
    question = Questions()
    await message.answer(question.tauba, reply_markup=Yes_no)

@start2.message(All.mechet_fard , F.text == "❌ Нет")
async def start2_7(message:types.Message, state:FSMContext):   
    await state.update_data(mechet_fard=False)
    await state.set_state(All.tauba) 
    question = Questions()
    await message.answer(question.tauba, reply_markup=Yes_no)


@start2.message(All.tauba , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=True)
    await state.set_state(All.zikr_ut) 
    question = Questions()
    await message.answer(question.zikr_ut, reply_markup=Yes_no)

@start2.message(All.tauba , F.text == "❌ Нет")
async def start2_6(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=False)
    await state.set_state(All.zikr_ut) 
    question = Questions()
    await message.answer(question.zikr_ut, reply_markup=Yes_no)


@start2.message(All.zikr_ut , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=True)
    await state.set_state(All.rodstven_otn) 
    question = Questions()
    await message.answer(question.rodstven_otn, reply_markup=Yes_no)

@start2.message(All.zikr_ut , F.text == "❌ Нет")
async def start2_5(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=False)
    await state.set_state(All.rodstven_otn) 
    question = Questions()
    await message.answer(question.rodstven_otn, reply_markup=Yes_no)


@start2.message(All.rodstven_otn , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(rodstven_otn=True)
    await state.set_state(All.sadaka) 
    question = Questions()
    await message.answer(question.sadaka, reply_markup=Yes_no)

@start2.message(All.rodstven_otn , F.text == "❌ Нет")
async def start2_4(message:types.Message, state:FSMContext):   
    await state.update_data(rodstven_otn=False)
    await state.set_state(All.sadaka) 
    question = Questions()
    await message.answer(question.sadaka, reply_markup=Yes_no)



@start2.message(All.sadaka , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(sadaka=True)
    await state.set_state(All.telefon) 
    question = Questions()
    await message.answer(question.telefon, reply_markup=Yes_no)

@start2.message(All.sadaka , F.text == "❌ Нет")
async def start2_3(message:types.Message, state:FSMContext):   
    await state.update_data(sadaka=False)
    await state.set_state(All.telefon) 
    question = Questions()
    await message.answer(question.telefon, reply_markup=Yes_no)

#######
@start2.message(All.telefon , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=True)
    await state.set_state(All.haram) 
    question = Questions()
    await message.answer(question.haram, reply_markup=Yes_no)

@start2.message(All.telefon , F.text == "❌ Нет")
async def telefon(message:types.Message, state:FSMContext):   
    await state.update_data(telefon=False)
    await state.set_state(All.haram) 
    question = Questions()
    await message.answer(question.haram, reply_markup=Yes_no)


@start2.message(All.haram , F.text == "✅ Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(haram=True)
    await state.set_state(All.eda) 
    question = Questions()
    await message.answer(question.eda, reply_markup=Yes_no)

@start2.message(All.haram , F.text == "❌ Нет")
async def haram(message:types.Message, state:FSMContext):   
    await state.update_data(haram=False)
    await state.set_state(All.eda) 
    question = Questions()
    await message.answer(question.eda, reply_markup=Yes_no)


@start2.message(All.eda , F.text == "✅ Да")
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

@start2.message(All.eda , F.text == "❌ Нет")
async def start2__0(message:types.Message, state:FSMContext):   
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

