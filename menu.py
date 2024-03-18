import os
from main import win_los
import config
def shop_page():
    config.shop_ui()
    #Товары магазина
    print('0.Выйти из магазина')
    print(" "*10,'1.Карыто, скорость: 1/10      250$')
    print(" "*10,"2.Toyota Corolla(1992), скорость: 2/10      1000$")
    x = int(input())
    if x == 1:
        config.money-=250
        print('Поздровляем, вы купили '"'Карыто'"'')
        config.shop_ui()
    elif x ==0:
        pass


def main_pagee():
    os.system('cls')
    print('.' * 156)
    print('''.                                                                                                                                                          .
.                                                                   |‾‾‾ |‾‾‾| |  | | / |  /|                                                              .
.                                                                   |    |   | |--| |/  | / |                                                              .
.                                                                   |    |___| |  | | \ |/  |                                                              .
.                                                                                                                                                          .''')
    print('.' * 156)

    print('1.Начать игру')
    print('2.Магазин')

    while True:
        a = int(input())
        if a == 1:
            win_los()
            a==0
            print('1.Играть')
            print('2.Магазин')
            #a==int(input())
        elif a == 2:
            shop_page()
            a==0
            main_pagee()

main_pagee()