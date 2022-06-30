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
        btn2=types.KeyboardButton("d20")
        btn1=types.KeyboardButton("d8")
        markup.add(btn1, btn2)
        bot.send_message(m.chat.id, 'Бросай дайсы!',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])

def handle_text(message):
    # Бросок d8
    if message.text.strip() == 'd8' :
            answer = random.randint(1,8)
    # Бросок d20
    elif message.text.strip() == 'd20':
            answer = random.randint(1,20)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)