---
created_at: 2026-03-19T20:11:10+01:00
modified_at: 2026-03-19T20:17:37+01:00
---
Сегодня начал писать своего ботика в тг и изучаю библиотеку таку как `telebot`. Очень интерессно но сегодня позанимался не долго так я уставший и голова болит.

Для того чтобы я не гадил в системе можно использовать виртуальное окружение где я могу скачивать библиотеки для проекта и оно никак не будет задевать мою систему. Для того что бы создать виртуальное окружение нужно вести вот эти команды:

- `python3 -m venv .venv` — создание песочницы.
- `source .venv/bin/activate` — вход в песочницу (появляется префикс `(.venv)`).
- `pip install pyTelegramBotAPI` — установка библиотеки для ботов.

Для того что бы был бот в тг нужно его там создать. Создается от чезер `BotFather`, он находится в тг. После этого он дает **токен** какой мы вставляем в код. Выглядит так:

```python
import telebot  # Подключаем библиотеку, которую мы скачали

# Вставь сюда свой токен в кавычках (тот, что дал BotFather)
TOKEN = "ТВОЙ_ТОКЕН_СЮДА" 

# Создаем объект бота (вспоминаем ООП: telebot - это библиотека, TeleBot - класс)
bot = telebot.TeleBot(TOKEN)

# Это "Декоратор". Он работает как антенна, которая ловит команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Если кто-то написал /start, бот выполнит эту функцию
    # message.chat.id — это уникальный номер чата с пользователем, чтобы бот знал, куда отвечать
    text = "Здарова, бро! Я твой первый бот, и я кручусь на NixOS!"
    bot.send_message(message.chat.id, text)

print("Бот успешно запущен! Жду сообщений...")

# Эта команда заставляет бота работать бесконечно и постоянно опрашивать сервера Telegram
bot.infinity_polling()
```

Так же я прицеплю свой код какой я сделал за сегодня:

```python 
import telebot

TOKEN = "8790090320:AAFMGme9t2az0VJDW8hf03vR2-q2o0Sf99s"
bot = telebot.TeleBot(TOKEN)


class Smartphone:
    def __init__(self, name) -> None:
        self.name = name
        self.battery = 100
        self.status = "on"

    def get_info(self):
        return f"Device: {self.name}\nBattery: {self.battery}%"


my_phone = Smartphone("Pixel 9a")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = "Welcome my friend!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["status"])
def check_status(message):
    info = my_phone.get_info()
    bot.send_message(message.chat.id, info)


@bot.message_handler(commands=["work"])
def use_phone(message):
    if my_phone.battery > 0:
        my_phone.battery = my_phone.battery - 20
        bot.send_message(message.chat.id, "You played and your battery had lost 20 %")
    else:
        bot.send_message(message.chat.id, "You phone is dead!")


@bot.message_handler(commands=["charge"])
def charge_phone(message):
    if my_phone.battery < 100:
        my_phone.battery = my_phone.battery + 20
        bot.send_message(message.chat.id, "Your phone charge on 20%")
    else:
        bot.send_message(message.chat.id, "You phone has 100%")


print("Your bot works!")

bot.infinity_polling()

```