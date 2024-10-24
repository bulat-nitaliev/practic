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
    fadjr = State()

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

class All(Islam, Vred):
    pass

class Questions:
    def __init__(self) -> None:
        self.quran = 'Сколько сегодня страниц Корана 📖 прочитали? Ответь цифрами 🔢'
        self.solat_duha = 'Сегодня читали молитву Духа'
        self.solat_vitr = 'Сегодня читали молитву Витр'
        self.fadjr = 'Сегодня вовремя читали молитву Фаджр'
        self.mechet_fard = 'Сегодня ходили на фард 🕌 в мечеть'
        self.tauba = 'Сегодня делали тауба 🤲, покаяние ?'
        self.sadaka = 'Сегодня давали садака помощь'
        self.zikr_vech = 'Читал поминание Аллаха перед сном?'
        self.zikr_ut = 'Сегодня делали утренние и вечерние оскары?'
        self.rodstven_otn = 'Сегодня поддерживали родственные связи (звонили 📞, навещали 🏠)?'
        self.son = 'Вовремя вчера легли спать - после Иша намаза 😴?'
        self.telefon = 'Сегодня отказались от траты много времени в телефоне (YouTube 📺, Instagram 📸, Telegram 💬)?'
        self.haram = 'Сегодня оберегали свой взгляд , уши , язык  (от харама - запретного 🚫)?'
        self.eda = 'Сегодня были умерены в еде (не переедали 🚫)?'

# q = Questions()
# day_question = [q.solat_vitr, q.son, q.zikr_ut,q.tauba, q.telefon, q.haram,q.eda]

# night_question = [q.quran, q.solat_duha, q.mechet_fard,q.tauba, q.zikr_vech, q.rodstven_otn,q.sadaka , q.telefon, q.haram,q.eda]