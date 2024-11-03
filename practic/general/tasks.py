from celery_app import app
import matplotlib.pyplot as plt
import pandas as pd
import mplcyberpunk
from decouple import config
from general.models import User, VredPrivichki, Islam
import  requests
from datetime import date, datetime, timedelta


@app.task
def send_mail()->None:
    token = token=config('API_TOKEN')
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    text_slice = 'Ас саламу алейкум! 👋 Поработайте над собой - пройдите опрос 📝 '
    
    for user in User.objects.all():
        tg_id = user.username
        if tg_id.isdigit():
            data = {'chat_id': tg_id, 'text': text_slice}
            
            response = requests.post(method, data=data) 
            
    return  response.json()



@app.task
def send_graf()->None:
    token = config('API_TOKEN')
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendPhoto'
    headers_v = ['son','haram', 'telefon', 'eda']
    headers_i =  ['solat_vitr', 'fadjr', 'mechet_fard', 'tauba', 'sadaka', 'zikr_ut', 'zikr_vech', 'rodstven_otn']

    filter_date = datetime.now() - timedelta(days=7)

# Выполняем запрос  


    for user in User.objects.all():
        l_vred, l_islam, quran = [], [], []
        tg_id = user.username
        user_pk = user.id
        vred_all = VredPrivichki.objects.all()
        islam_all = Islam.objects.all()
        if tg_id.isdigit() and tg_id == '942913569':
            vred =[i for i in vred_all.filter(user=user_pk, created_at__gt=filter_date)]
            islam =[i for i in  islam_all.filter(user=user_pk, created_at__gt=filter_date)]
            print('vred ------------- ', vred, 'islam --------- ',islam)
            for i in vred:
                l_vred.append([i.son, i.haram, i.telefon, i.eda])
                
            quran = [i.quran for i in Islam.objects.filter(user=user_pk, created_at__gt=filter_date)]
            print(' quran ---------- ' quran)
            for i in islam:
                
                l_islam.append([i.solat_vitr,
                                i.fadjr,
                                i.mechet_fard,
                                i.tauba,
                                i.sadaka,
                                i.zikr_ut,
                                i.zikr_vech,
                                i.rodstven_otn])

            l_q = [i for i in quran if i != 0]
            df_v = pd.DataFrame(l_vred, columns=headers_v)
            # type_val_v = ['Да', 'Нет'] * 4
            df_i = pd.DataFrame(l_islam, columns=headers_i)
            
            # type_val_i = ['Да', 'Нет'] * 4

            true_v, false_v, true_i, false_i = [], [], [], []
            for i in headers_v:
                true_v.append(df_v[i].to_list().count(True))
                false_v.append(df_v[i].to_list().count(False))
                # l_val_v.append(true)
                # l_val_v.append(false)

            for i in headers_i:
                true_i.append(df_i[i].to_list().count(True))
                false_i.append(df_i[i].to_list().count(False))
                # l_val_i.append(true)
                # l_val_i.append(false)

            # header_v = [y for i in list(zip(headers_v,headers_v)) for y in i]
            # header_i1 = [y for i in list(zip(headers_i[:4],headers_i[:4])) for y in i]
            # header_i2 = [y for i in list(zip(headers_i[4:],headers_i[4:])) for y in i]

            data_v = {
                'Вредные привычки': headers_v,
                'Да': true_v,
                'Нет': false_v
            }

            data_i= {
                'Ислам': headers_i,
                'Да': true_i,
                'Нет': false_i
            }
            # data_i_2= {
            #     'Ислам': header_i2,
            #     'Значения': l_val_i[8:],
            #     'Type': type_val_i
            # }

            df_vr = pd.DataFrame(data_v)
            df_is1 = pd.DataFrame(data_i)
            # df_is2 = pd.DataFrame(data_i_2)
            # palette = {'Да': 'green', 'Нет': 'red'}

            # Построение сгруппированной столбчатой диаграммы
            # sns.barplot(x='Вредные привычки', y='Значения', hue='Type', data=df_vr, palette=palette)
            plt.title('Оставление вредных привычек')
            with plt.style.context('cyberpunk'):
                df_vr.plot(x='Вредные привычки', kind='bar', stacked=False, alpha=0.8, color=['lime', 'tomato'])
            # plt.show()
            plt.savefig('вредные_привычки_.jpg')
            plt.close()

            # sns.barplot(x='Ислам', y='Значения', hue='Type', data=df_is1, palette=palette)
            plt.title('Побуждение к благочестию')
            with plt.style.context('cyberpunk'):
                df_is1.plot(x='Ислам', kind='bar', stacked=False, alpha=0.8, color=['lime', 'tomato'])
            # plt.show()
            plt.savefig('ислам.jpg')
            plt.close()

            # sns.barplot(x='Ислам', y='Значения', hue='Type', data=df_is2, palette=palette)
            # plt.title('Побуждение к благочестию')
            # # plt.show()
            # plt.savefig('ислам2.jpg')
            # plt.close()
            # print(l_q, tg_id)
            # plt.plot(l_q, '-bo')
            # plt.grid(True)
            plt.title('Чтение корана')
            df_q = pd.DataFrame(l_q)
            # plt.plot(,'-bo')
            with plt.style.context('cyberpunk'):
                df_q.plot( kind='line',
                        lw=3, marker='.', ms=20,
                        figsize=(10,10))

                
                mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.4)
            plt.savefig('quran.jpg')
            plt.close()
            
            with open('вредные_привычки_.jpg', 'rb') as photo, open('ислам.jpg', 
                                                                    'rb') as photo_i,  open('quran.jpg', 'rb') as photo_q:
                file_v = {'photo': photo}
                file_i = {'photo': photo_i}
                # file_i2 = {'photo': photo_i2}open('ислам2.jpg', 
                                                                                        # 'rb') as photo_i2,
                file_q = {'photo': photo_q}
                data = {'chat_id': tg_id}
                        
                response = requests.post(method, data=data, files=file_v) 
                response_i = requests.post(method, data=data, files=file_i) 
                # response_i2 = requests.post(method, data=data, files=file_i2) 
                response_q = requests.post(method, data=data, files=file_q)

