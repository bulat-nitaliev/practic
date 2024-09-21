from celery_app import app
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from decouple import config
from general.models import User, Islam, VredPrivichki
import  requests


@app.task
def send_mail()->None:
    token = token=config('API_TOKEN')
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    text_slice = 'Ас саламу алейкум! 👋 Поработайте над собой - пройдите опрос 📝 и обновите цели 🎯.'
    
    for user in User.objects.all():
        tg_id = user.username
        if tg_id.isdigit():
            data = {'chat_id': tg_id, 'text': text_slice}
            
            response = requests.post(method, data=data) 
            print(response.json())
    return  response.json()

@app.task
def send_graf()->None:
    token = token=config('API_TOKEN')
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendPhoto'

    headers = ['son','haram', 'telefon', 'eda']
    l = []
    for i in VredPrivichki.objects.filter(user=2):
        l.append([i.son, i.haram, i.telefon, i.eda])

    
    df = pd.DataFrame(l, columns=headers)
    type_val = ['Да', 'Нет'] * 4

    l_val = []
    for i in headers:
        true = df[i].to_list().count('True')
        false = df[i].to_list().count('False')
        l_val.append(true)
        l_val.append(false)

    header = [y for i in list(zip(headers,headers)) for y in i]

    data = {
	    'Вредные привычки': header,
	    'Значения': l_val,
	    'Type': type_val
	}


    df = pd.DataFrame(data)
    palette = {'Да': 'green', 'Нет': 'red'}

	# Построение сгруппированной столбчатой диаграммы
    # sns.barplot(x='Вредные привычки', y='Значения', hue='Type', data=df, palette=palette)
    plt.title('Оставление вредных привычек')
    plt.show()
    plt.savefig('вредные_привычки.jpg')
    with open('вредные привычки.jpg', 'rb') as photo:
        file = {'photo': photo}
        data = {'chat_id': 942913569, 'files': file}
                
        response = requests.post(method, data=data) 
        print(response.json())

