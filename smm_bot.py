
import telebot
import requests
import os

BOT_TOKEN = os.environ.get("8053589642:AAFM2g0rd-lWwX0wmCf-N-mNWr9wFKuvvFk")
SMM_API_KEY = os.environ.get("b028e8faf58eef167a0447cbe1a35de2c4becaba")
CHAT_ID = '5335667019'

bot = telebot.TeleBot(8053589642:AAFM2g0rd-lWwX0wmCf-N-mNWr9wFKuvvFk)

def get_balance():
    url = 'https://smmzz.com/api/v2'
    data = {
        'key': b028e8faf58eef167a0447cbe1a35de2c4becaba ,
        'action': 'balance'
    }
    response = requests.post(url, data=data).json()
    return response.get('balance'), response.get('currency')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the SMM Bot!\nUse /balance to check balance.")

@bot.message_handler(commands=['balance'])
def check_balance(message):
    balance, currency = get_balance()
    bot.reply_to(message, f"Your balance is: {balance} {currency}")

bot.polling()
