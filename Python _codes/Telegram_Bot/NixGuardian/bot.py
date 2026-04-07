from email import message_from_file
from pydoc import text
import telebot
import subprocess

TOKEN = "8294008334:AAFqwoL9Qg4ADgPsue1tyOQnAi3EKul-92s"
ADMIN_ID = 5702867837

bot = telebot.TeleBot(TOKEN)


class SystemStats:
    def __init__(self) -> None:
        self.name = name
        self.nixos = nixos
        self.timeWork = timeWork,

    def nixos(self):
        return subprocess.run(["neofetch"], capture_output=True, text=True)

@bot.message_handler(["start"])
def welcome(message):
    user_id = message.from_user.id
    messageForBot = message.chat.id

    if user_id == ADMIN_ID:
        bot.send_message(messageForBot, "Hi Admin, we are ready to work !")
    else:
        bot.send_message(
            messageForBot,
            "You're not Admin. I can't work with you.",
        )

@bot.message_hadler(["nixos"]):
    user_id = message.from_user.id
    messageForBot = message.chat.id


print("Your bot works!")

bot.infinity_polling()
