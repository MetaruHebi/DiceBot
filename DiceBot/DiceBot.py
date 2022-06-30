import telebot
import random
from telebot import types
import config

# Создаем бота
bot = telebot.TeleBot(config.TOKEN)
# Команда start
@bot.message_handler(commands=["start"])

def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1=types.KeyboardButton("d20")
        btn2=types.KeyboardButton("d12")
        btn3=types.KeyboardButton("d8")
        btn4=types.KeyboardButton("d6")
        btn5=types.KeyboardButton("d4")
        btn6=types.KeyboardButton("d100")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(m.chat.id, 'Бросай дайсы!',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

def handle_text(message):
    # Бросок d8
    if message.text.strip() == 'd20' :
            answer = random.randint(1,20)
    # Бросок d20
    elif message.text.strip() == 'd12':
            answer = random.randint(1,12)
    elif message.text.strip() == 'd8':
            answer = random.randint(1,8)
    elif message.text.strip() == 'd6':
            answer = random.randint(1,6)
    elif message.text.strip() == 'd4':
            answer = random.randint(1,4)
    elif message.text.strip() == 'd100':
            answer = random.randint(1,100)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)