import telebot
from telebot import types

bot = telebot.TeleBot('5276309587:AAERpdoJYo1OyAFCwe7wBCqfM90ftQ-jfgs')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm bot who can help you with your costs. "
                          ""
                          " Now you need click on this button -> /button. "
                          ""
                          " I believe that my bot help you. ")


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Information', callback_data='one')
    item2 = types.InlineKeyboardButton("Кар'єра", callback_data='two')
    item3 = types.InlineKeyboardButton("Сім'я", callback_data='three')
    item4 = types.InlineKeyboardButton("Оточення ", callback_data='four')
    item5 = types.InlineKeyboardButton("Творчість і хоббі", callback_data='five')
    item6 = types.InlineKeyboardButton("Відпочинок та подорожі", callback_data='six')
    item7 = types.InlineKeyboardButton("Розвиток (освіта)", callback_data='seven')
    item8 = types.InlineKeyboardButton("Здоров'я, спорт", callback_data='eight')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, 'Hi! Choose the button', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "one":
            bot.send_message(call.message.chat.id, 'My bot can help you with you costs. You need read instruction.'
                                                   'Good luck:) ')
        elif call.data == 'two':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save1)
        elif call.data == 'three':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save2)
        elif call.data == 'four':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save3)
        elif call.data == 'five':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save4)
        elif call.data == 'six':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save5)
        elif call.data == 'seven':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save6)
        elif call.data == 'eight':
            msg = bot.send_message(call.message.chat.id, 'Print How many maney you spend.')
            bot.register_next_step_handler(msg, save7)

def save1(message):
    file = open('carier.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save2(message):
    file = open('family.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save3(message):
    file = open('otochenya.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save4(message):
    file = open('art and hobby.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save5(message):
    file = open('vekend and travel.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save6(message):
    file = open('rozvutok(osvita).txt', 'w')
    file.write(message.text)
    file.close()
    print("save")

def save7(message):
    file = open('helth and sport.txt', 'w')
    file.write(message.text)
    file.close()
    print("save")



bot.polling()
