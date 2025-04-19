
import telebot
import requests
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
SMM_API_KEY = os.environ.get("SMM_API_KEY")
CHAT_ID = '5335667019'

bot = telebot.TeleBot(BOT_TOKEN)

def get_balance():
    url = 'https://smmzz.com/api/v2'
    data = {
        'key': SMM_API_KEY,
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
