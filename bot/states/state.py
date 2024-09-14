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
        self.zikr_ut = 'Сегодня делали утреннее поминание'
        self.zikr_vech = 'Сегодня делали вечернее поминание'
        self.rodstven_otn = 'Сегодня поддерживали родственные связи (звонили 📞, навещали 🏠)?'
        self.son = 'Вовремя вчера легли спать - после Иша намаза 😴?'
        self.telefon = 'Сегодня отказались от траты много времени в телефоне (YouTube 📺, Instagram 📸, Telegram 💬)?'
        self.haram = 'Сегодня оберегали свой взгляд , уши , язык  (от харама - запретного 🚫)?'
        self.eda = 'Сегодня были умерены в еде (не переедали 🚫)?'