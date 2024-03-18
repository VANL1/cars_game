import os
import time
from time import sleep
import random
from random import uniform
def carsMatch(x,y,z):
    y += uniform(0, 2)
    #sleep(0.1)
    print('>' * 155)
    print(x * int(y) +
        "┈┏┓┈██┈┈┈███┈┈┈┈\n" + x * int(y) +
        "┈┃┃╭┻┻━━━┻━┻┏┓┈\n" + x * int(y) +
        "┈┃┣╯┉┉╭━━┓╭┉┃┃┈\n" + x * int(y) +
        "┈┃┣╮┉┉╰━━┛╰┉┃┃┈\n" + x * int(y) +
        "┈┃┃╰┳┳━━━┳━┳┗┛┈\n" + x * int(y) +
        "┈┗┛┈██┈┈┈███┈┈┈┈\n"
    )

    z += uniform(0, 2)

    print('>'*155)
    print('>' * 155)



    print(x * int(z) +
        "┈┏┓┈██┈┈┈███┈┈┈┈\n" + x * int(z) +
        "┈┃┃╭┻┻━━━┻━┻┏┓┈\n" + x * int(z) +
        "┈┃┣╯┉┉╭━━┓╭┉┃┃┈\n" + x * int(z) +
        "┈┃┣╮┉┉╰━━┛╰┉┃┃┈\n" + x * int(z) +
        "┈┃┃╰┳┳━━━┳━┳┗┛┈\n" + x * int(z) +
        "┈┗┛┈██┈┈┈███┈┈┈┈\n"
    )
    print('>' * 155)


    sleep(0.05)
    os.system('cls')
    return z,y


class car:
    def __init__(self, model, speed, price):
        self.model = model
        self.speed = speed
        self.price = price

