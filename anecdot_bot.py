from config import TOKEN
from telebot import TeleBot, types
from anecdot_parser import get_random_anecdot, get_random_pic
from auth import User

bot = TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, 'Привет, я умею \
        рассылать анекдоты!, отправь мне /anecdot и я расскажу тебе анекдот или отправь /pic и я пришлю тебе картинку.')
    
    user = User(message.from_user.username, message.from_user.id)
    if user.new:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('Да'), types.KeyboardButton('Нет'))
        bot.send_message(message.chat.id, 'Хочешь получать анекдоты?', reply_markup=keyboard)
        bot.register_next_step_handler(message, subscribe_handler)

def subscribe_handler(message: types.Message):
    if message.text == 'Да':
        user = User(message.from_user.username, message.from_user.id)
        user.subscribe()
        bot.send_message(message.chat.id, 'Подписка оформлена')
    elif message.text == 'Нет':
        user = User(message.from_user.username, message.from_user.id)
        user.unsubscribe()
        bot.send_message(message.chat.id, 'Подписка отменена')   
    
@bot.message_handler(commands=['anecdot'])
def anecdot_handler(message: types.Message):
    anekdot = get_random_anecdot()
    bot.send_message(message.chat.id, anekdot)
    
    
@bot.message_handler(commands=['pic'])
def pic_handler(message: types.Message):
    pic = get_random_pic()
    bot.send_photo(message.chat.id, pic)
    
bot.infinity_polling()