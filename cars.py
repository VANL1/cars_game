import os
import time
from time import sleep
import random
from random import uniform
def carsMatch(x,y,z):
    y += uniform(1, 5)
    #sleep(0.1)
    print(
        x * 15 + ">>>>>>>>>>>\n" + x * int(y) +
        "┈┏┓┈██┈┈┈███┈┈┈┈\n" + x * int(y) +
        "┈┃┃╭┻┻━━━┻━┻┏┓┈\n" + x * int(y) +
        "┈┃┣╯┉┉╭━━┓╭┉┃┃┈\n" + x * int(y) +
        "┈┃┣╮┉┉╰━━┛╰┉┃┃┈\n" + x * int(y) +
        "┈┃┃╰┳┳━━━┳━┳┗┛┈\n" + x * int(y) +
        "┈┗┛┈██┈┈┈███┈┈┈┈\n" + x * int(y) +
        ">>>>>>>>>>>>>>>>>"
    )

    z += uniform(1, 5)

    print(
        x * 15 + ">>>>>>>>>>>\n" + x * int(z) +
        "┈┏┓┈██┈┈┈███┈┈┈┈\n" + x * int(z) +
        "┈┃┃╭┻┻━━━┻━┻┏┓┈\n" + x * int(z) +
        "┈┃┣╯┉┉╭━━┓╭┉┃┃┈\n" + x * int(z) +
        "┈┃┣╮┉┉╰━━┛╰┉┃┃┈\n" + x * int(z) +
        "┈┃┃╰┳┳━━━┳━┳┗┛┈\n" + x * int(z) +
        "┈┗┛┈██┈┈┈███┈┈┈┈\n" + x * int(z) +
        ">>>>>>>>>>>>>>>>>"
    )
    sleep(0.07)
    os.system('cls')
    return z,y


class car:
    def __init__(self, model, speed, price):
        self.model = model
        self.speed = speed
        self.price = price

