import telebot

TOKEN = "8215348467:AAFfwdIH0c94ljfrLzpSOprPdJp7gMA1Z58"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is alive 🚀")

bot.infinity_polling()
