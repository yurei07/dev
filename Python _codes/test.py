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
