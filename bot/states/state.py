from aiogram.fsm.state import StatesGroup, State

class Islam(StatesGroup):
    quran = State()
    solat_duha = State()
    solat_vitr = State()
    mechet_fard = State()
    tauba = State()
    sadaka = State()
    zikr_ut = State()
    zikr_vech = State()
    rodstven_otn = State()

class Vred(StatesGroup):
    son = State()
    telefon = State()
    haram = State()
    eda = State()

class Cel(StatesGroup):
    cel_state = State()

class Comment(StatesGroup):
    id = State()
    body = State()