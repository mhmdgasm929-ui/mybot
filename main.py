import telebot

TOKEN = "8737122794:AAFR51dPCPLolWdz_P3DFRN_JbvWagFkFcM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "البوت شغال 🔥")

bot.polling()
