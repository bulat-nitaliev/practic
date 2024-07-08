from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram import Router
from states.state import Islam
from aiogram.fsm.context import FSMContext
from keyboard.keyboards import Yes_no, menu
from fetchs.connect import register, login, islam

router = Router()


@router.message(Islam.quran)
async def start(message:types.Message, state:FSMContext):
    count = message.text
    if count.isdigit():
        await state.update_data(quran=int(count))
        await state.set_state(Islam.solat_duha) 
        
        await message.answer(f'Сегодня читали молитву Духа ', reply_markup=Yes_no)
    else:
        await message.answer('Введите число')
    

@router.message(Islam.solat_duha , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(solat_duha=True)
    await state.set_state(Islam.solat_vitr) 
    await message.answer('Сегодня читали молитву Витр', reply_markup=Yes_no)

@router.message(Islam.solat_duha , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(solat_duha=False)
    await state.set_state(Islam.solat_vitr) 
    await message.answer('Сегодня читали молитву Витр', reply_markup=Yes_no)


#vitr
@router.message(Islam.solat_vitr , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(solat_vitr=True)
    await state.set_state(Islam.mechet_fard) 
    await message.answer('Сегодня ходили на фард в мечеть', reply_markup=Yes_no)

@router.message(Islam.solat_vitr , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(solat_vitr=False)
    await state.set_state(Islam.mechet_fard) 
    await message.answer('Сегодня ходили на фард в мечеть', reply_markup=Yes_no)

#mechet_fard
@router.message(Islam.mechet_fard , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(mechet_fard=True)
    await state.set_state(Islam.tauba) 
    await message.answer('Сегодня делали тауба покаяние', reply_markup=Yes_no)

@router.message(Islam.mechet_fard , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(mechet_fard=False)
    await state.set_state(Islam.tauba) 
    await message.answer('Сегодня делали тауба покаяние', reply_markup=Yes_no)

#tauba
@router.message(Islam.tauba , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=True)
    await state.set_state(Islam.sadaka) 
    await message.answer('Сегодня давали садака помощь', reply_markup=Yes_no)

@router.message(Islam.tauba , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(tauba=False)
    await state.set_state(Islam.sadaka) 
    await message.answer('Сегодня давали садака помощь', reply_markup=Yes_no)

#sadaka
@router.message(Islam.sadaka , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(sadaka=True)
    await state.set_state(Islam.zikr_ut) 
    await message.answer('Сегодня делали утреннее поминание', reply_markup=Yes_no)

@router.message(Islam.sadaka , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(sadaka=False)
    await state.set_state(Islam.zikr_ut) 
    await message.answer('Сегодня делали утреннее поминание', reply_markup=Yes_no)

#zikr_ut
@router.message(Islam.zikr_ut , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=True)
    await state.set_state(Islam.zikr_vech) 
    await message.answer('Сегодня делали вечернее поминание', reply_markup=Yes_no)

@router.message(Islam.zikr_ut , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_ut=False)
    await state.set_state(Islam.zikr_vech) 
    await message.answer('Сегодня делали вечернее поминание', reply_markup=Yes_no)

#zikr_vech
@router.message(Islam.zikr_vech , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_vech=True)
    await state.set_state(Islam.rodstven_otn) 
    await message.answer('Сегодня поддерживали родственные связи(звонили, навещали)', reply_markup=Yes_no)

@router.message(Islam.zikr_vech , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(zikr_vech=False)
    await state.set_state(Islam.rodstven_otn) 
    await message.answer('Сегодня поддерживали родственные связи(звонили, навещали)', reply_markup=Yes_no)

#rodstven_otn
@router.message(Islam.rodstven_otn , F.text == "Да")
async def start1(message:types.Message, state:FSMContext):   
    await state.update_data(rodstven_otn=True)
    data = await state.get_data()
    await state.clear() 
    data_islam = {
        "quran": data['quran'],
        "solat_duha": data['solat_duha'],
        "solat_vitr": data['solat_vitr'],
        "mechet_fard": data['mechet_fard'],
        "tauba": data['tauba'],
        "sadaka": data['sadaka'],
        "zikr_ut": data['zikr_ut'],
        "zikr_vech": data['zikr_vech'],
        "rodstven_otn": data['rodstven_otn']
        }
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await islam(data, access_token)
    print(res)
    await message.answer(f'{data}', reply_markup=types.ReplyKeyboardRemove())

@router.message(Islam.rodstven_otn , F.text == "Нет")
async def start2(message:types.Message, state:FSMContext):   
    await state.update_data(rodstven_otn=False)
    data = await state.get_data()
    await state.clear() 
    data_islam = {
        "quran": data['quran'],
        "solat_duha": data['solat_duha'],
        "solat_vitr": data['solat_vitr'],
        "mechet_fard": data['mechet_fard'],
        "tauba": data['tauba'],
        "sadaka": data['sadaka'],
        "zikr_ut": data['zikr_ut'],
        "zikr_vech": data['zikr_vech'],
        "rodstven_otn": data['rodstven_otn']
        }
    dt = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id)
        }
    access_token = await login(dt)
    res = await islam(data, access_token)
    print(res)
    await message.answer(f'{data}', reply_markup=types.ReplyKeyboardRemove())


#Islam
@router.message(F.text=='Ислам')
async def start(message:types.Message, state:FSMContext):
    await state.set_state(Islam.quran) 
    await message.answer('As salamu aleykum сколько страниц курана прочитали', reply_markup=types.ReplyKeyboardRemove())
    

#Start
@router.message(CommandStart)
async def start(message:types.Message):
    data = {
        "username": str(message.from_user.id),
        "password": str(message.from_user.id),
        "email": f"user{str(message.from_user.id)}@example.com",
        "first_name": message.from_user.username,
        "last_name": message.from_user.first_name
        }
    res = await register(data)
    # dt = {
    #     "username": str(message.from_user.id),
    #     "password": str(message.from_user.id)
    #     }

    # print(res)
    # rs = await login(dt)
    # print(rs)
    await message.answer('As salamu aleykum' , reply_markup=menu)