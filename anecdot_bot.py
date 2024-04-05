from config import TOKEN
from telebot import TeleBot, types
from anecdot_parser import get_random_anecdot, get_random_pic

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, 'Привет, я умею \
        рассылать анекдоты!, отправь мне /anecdot и я расскажу тебе анекдот или отправь /pic и я пришлю тебе картинку.')

@bot.message_handler(commands=['anecdot'])
def anecdot_handler(message: types.Message):
    anekdot = get_random_anecdot()
    bot.send_message(message.chat.id, anekdot)
    
    
@bot.message_handler(commands=['pic'])
def pic_handler(message: types.Message):
    pic = get_random_pic()
    bot.send_photo(message.chat.id, pic)
    
bot.infinity_polling()