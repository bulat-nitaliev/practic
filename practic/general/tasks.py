from celery_app import app
# from aiogram import Bot

from decouple import config
from general.models import User
import  requests


@app.task
def send_mail()->None:
    token = token=config('API_TOKEN')
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'
    text_slice = 'Ас саламу алейкум поработайте над собой - пройдите опрос и обновите цели'
    
    for user in User.objects.all():
        tg_id = user.username
        if tg_id.isdigit():
            data = {'chat_id': tg_id, 'text': text_slice}
            
            response = requests.post(method, data=data) 
            print(response.json())
    return  response.json()


# @app.task
# async def send_mail():
#     # bot = Bot(token=config('API_TOKEN'))
    
#     for user in User.objects.all():
#         tg_id = user.username
#         if tg_id.isdigit():
            
#             await bot.send_message(int(tg_id), 'Ас саламу алейкум поработайте над собой - пройдите опрос и обновите цели')
#             print(tg_id)
#             print(config('API_TOKEN'))


