import telebot
import subprocess

TOKEN = "8294008334:AAFqwoL9Qg4ADgPsue1tyOQnAi3EKul-92s"
ADMIN_ID = 5702867837

bot = telebot.TeleBot(TOKEN)


class SystemStats:
    def __init__(self, name) -> None:
        self.name = name
        self.status = "on"


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

@bot.message_handler(["nixos"])
def system(message):
    messageForBot = message.chat.id
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        bot.send_message(messageForBot, "Waiting info about your pc")
    
        try: 
            timeWork = subprocess.run(["uptime"], capture_output=True, text=True)
            ram = subprocess.run(["free", "-h"], capture_output=True, text=True)
            dysk = subprocess.run(["nix-shell", "-p", "dysk", "--run", "dysk"], capture_output=True, text=True)

            sys = f"**MY SYSTEM** \n\n"
            sys += f"**RAM: {ram}** \n"
            sys += f"**DYSK: {dysk}**\n"
            sys += f"**TIME WORK: {timeWork}**\n"
            
            bot.send_message(messageForBot, sys, parse_mode="Markdown")

        except Exception as e:
            bot.send_message(messageForBot, f"ERROR: {e}")
    else:
        bot.send_message(
            messageForBot,
            "You're not Admin. I can't work with you.",
        )


print("Your bot works!")

bot.infinity_polling()
