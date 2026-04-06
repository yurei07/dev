---
created_at: 2026-03-19T20:09:52+01:00
modified_at: 2026-03-19T20:10:24+01:00
---

Такс сегодня первый день и я повторил питончик. Начал с ООП и изучил наследование на базовом уровне. На удивление за час сделал больше чем мог сделать за 4 часа и я ловлю рил кайф от этого.  
Такс что я изучил:

1. **Class** = это типа как чертеж в каком можно создавать обьекты и управлять ими через класс. Так же этот класс можно наследовать и что бы другие классы использовали этот класс.
2. **Object** = это как раз то что мы создаем внутри чертяжа, тоесть какой то обьект какой мы будем разробатывать. Например машину, и там задаем мы ему характеристики.(скорость, материал, шини и тп.)
3. ****init**** (пишется вместе) = Это метод, с помощью которого можно настраивать обьекты при создании (как раз те самые характиристики)
4. **self** = сылка на конкретный экземпляр. Через `self` объект лезет в свои "карманы" за переменными (`self.battery`) или методами
5. **Наследование (Inheritance)** — когда класс (ребенок) забирает все умения у другого класса (родителя). Пишется как `class Laptop(Gadget):`. Это позволяет не копипастить код

Код какой я сегодня смог сделать за урок:

```python
class Gadget:
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.battery = 100

    def turn_on(self):
        if self.battery > 0:
            self.status = "on"
            print(f"{self.name} works on Nixos!")
        elif self.battery <= 0:
            print(f"{self.name} is dead :<")

    def work(self):
        if self.status == "on":
            self.battery -= 20
            if self.battery <= 0:
                self.battery = 0
                print(f"Unluck, your device doesnt work :<")
            else:
                print(f"{self.name} works, battery: {self.battery} %")
        else:
            print(f"Turn on {self.name} first!")


class Smartphone(Gadget):
    def send_text(self, text):
        if self.status == "on":
            print(f"Send a massage: {text}")
        if self.status == "off":
            print(f"WHF??? TURN ON!!!")


class Laptop(Gadget):
    def open_terminal(self, app):
        if self.status == "on":
            print(f"Nixos {app} opened on my {self.name}")
        else:
            print("Unluck :>")


phone = Gadget("iPhone")
phone.turn_on()

my_phone = Smartphone("Pixel 9a")
my_phone.turn_on()
my_phone.send_text("Hi bro! How are you?")
my_phone.work()

my_laptop = Laptop("Tuf gaming")
my_laptop.turn_on()
my_laptop.open_terminal("Terminal")
my_laptop.work()


for _ in range(5):
    phone.work()
```