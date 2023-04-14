import telebot
import time
import pyshorteners
import os

bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'ᴇʟʟᴏ ʙᴀʙʏ , ᴀᴀᴘᴋᴏ ʙʜɪ ʟɪɴᴋ ᴍᴇ ᴄᴏɴᴠᴇʀᴛ ᴋᴀʀɴᴀ ʜ ᴋʏᴀ ʙᴀʙʏ ᴍᴜᴊʜᴇ sᴇɴᴅ ᴋᴀʀᴅᴏ ʙᴀʙʏ .\n\n🌚 ᴘᴏᴡᴇʀᴇᴅ ʙʏ @TeamSukun 🌝')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'ᴊᴀʟᴅɪ sᴇ ᴋᴏɪ ғɪʟᴇ ʙʜᴇᴊᴏ ʙᴀʙʏ ᴊɪsᴋᴏ ᴍᴀɪɴ ʟɪɴᴋ ᴍᴇ ᴄᴏɴᴠᴇʀᴛ ᴋᴀʀ sᴀᴋᴜ')    

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
