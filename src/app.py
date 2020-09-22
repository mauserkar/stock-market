import os
import requests
import time

def get_stock():
    stock = os.environ["STOCK"]
    finToken = os.environ["FIN_TOKEN"]
    finUrl = 'https://finnhub.io/api/v1/quote?symbol=' + stock + '&token=' + finToken
    r = requests.get(finUrl)
    jsonResponse = r.json()
    return r.json()

def telegram_bot_sendtext():
    botMessage = "price: " + str(get_stock())
    botToken = os.environ["BOT_TOKEN"] 
    botChatId = os.environ["BOT_CHAT_ID"]
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatId + '&parse_mode=Markdown&text=' + botMessage
    response = requests.get(sendText)
    return response.json()

while True:
    print (get_stock())
    telegram_bot_sendtext()
    print("sleep 1 day")
    time.sleep(86400)