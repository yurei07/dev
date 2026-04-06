import telebot
import subprocess
import json
import os

TOKEN = "8790090320:AAFMGme9t2az0VJDW8hf03vR2-q2o0Sf99s"
bot = telebot.TeleBot(TOKEN)

users_gadgets = {}


def load_data():
    if os.path.exists("data-bot.json"):
        with open("data-bot.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)

            for user_id, info in raw_data.items():
                phone = Smartphone(info["name"])
                phone.battery = info["battery"]
                phone.status = info["status"]

                users_gadgets[int(user_id)] = phone
        print("Data loaded seccess!")
    else:
        print("Your dont have a data")


def save_data():
    data_to_save = {}

    for user_id, phone in users_gadgets.items():
        data_to_save[str(user_id)] = {
            "name": phone.name,
            "battery": phone.battery,
            "status": phone.status,
        }

    with open("data-bot.json", "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4)

    print("Your Data saved.")


class Smartphone:
    def __init__(self, name) -> None:
        self.name = name
        self.battery = 100
        self.status = "on"

    def get_info(self):
        return f"Device: {self.name}\nBattery: {self.battery}%"


load_data()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = "Welcome my friend!"
    user_id = message.from_user.id

    if user_id not in users_gadgets:
        users_gadgets[user_id] = Smartphone("Nothing Phone")
        bot.send_message(message.chat.id, "New phone, nice!")
    else:
        bot.send_message(message.chat.id, "I have info about your phone")

    bot.send_message(message.chat.id, text)
    save_data()


@bot.message_handler(commands=["status"])
def check_status(message):
    user_id = message.from_user.id
    if user_id in users_gadgets:
        phone = users_gadgets[user_id]
        info = phone.get_info()
        bot.send_message(message.chat.id, info)
    else:
        bot.send_message(message.chat.id, "I dont have your id of phone.")
    save_data()


@bot.message_handler(commands=["work"])
def use_phone(message):
    user_id = message.from_user.id

    if user_id in users_gadgets:
        phone = users_gadgets[user_id]
        if phone.battery > 0:
            phone.battery -= 20
            bot.send_message(
                message.chat.id, "You played and your battery had lost 20 %"
            )
        else:
            bot.send_message(message.chat.id, "You phone is dead!")
    else:
        bot.send_message(
            message.chat.id, "I dont know your phone. Please, write /start"
        )
    save_data()


@bot.message_handler(commands=["charge"])
def charge_phone(message):
    user_id = message.from_user.id

    if user_id in users_gadgets:
        phone = users_gadgets[user_id]

        if phone.battery < 100:
            phone.battery = phone.battery + 20
            bot.send_message(message.chat.id, "Your phone charge on 20%")
        else:
            bot.send_message(message.chat.id, "You phone has 100%")
    else:
        bot.send_message(
            message.chat.id, "I dont know your phone. Please, write /start"
        )
    save_data()


@bot.message_handler(["sysinfo"])
def check_system(message):
    bot.send_message(message.chat.id, "Waiting for info about Nixos....")

    try:
        result_uptime = subprocess.run(["uptime"], capture_output=True, text=True)
        result_ram = subprocess.run(["free", "-h"], capture_output=True, text=True)

        sys_text = f"**Status of Nixos:** \n\n"
        sys_text += f"**Uptime:** {result_uptime.stdout}\n"
        sys_text += f"**Free ram:** {result_ram.stdout}"

        bot.send_message(message.chat.id, sys_text, parse_mode="Markdown")

    except Exception as e:
        bot.send_message(message.chat.id, f"ERROR: {e}")


@bot.message_handler(["screen"])
def screen_pc(message):
    bot.send_message(message.chat.id, "Doing a screenshot on Nixos")

    try:
        result_screen = subprocess.run(
            [
                "hyprshot",
                "-m",
                "output",
                "-m",
                "DP-1",
                "-o",
                "/home/prizrak/Pictures/Screenshots",
                "-f",
                "bot_screen.png",
                "--clipboard-only",
            ],
            check=True,
        )

        path = "/home/prizrak/Pictures/Screenshots/bot_screen.png"
        with open(path, "rb") as photo_file:
            bot.send_photo(message.chat.id, photo_file, caption="SCREEN")
    except Exception as e:
        bot.send_message(message.chat.id, f"ERROR: {e}")


print("Your bot works!")

bot.infinity_polling()
