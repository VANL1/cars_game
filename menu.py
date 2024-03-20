import os
from main import win_los
import config
def shop_page():
    config.shop_ui()
    x = int(input())
    while x!=0:
        if x == 1:
            if config.money>250:
                config.money-=250
                config.shop_ui()
                print('Поздровляем, вы купили '"'Карыто'"'')
                x = int(input())
            else:
                print('Недостаточно средств')
                x = int(input())
        elif x==2:
            if config.money>1000:
                config.money-=1000
                config.shop_ui()
                print('Поздровляем, вы купили '"'Toyota Corolla(1992)'"'')
                x = int(input())
            else:
                print('Недостаточно средств')
                x = int(input())
        elif x==0:
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

    print('1.Start game')
    print('2.Shop')

    while True:
        a = int(input())
        if a == 1:
            a -= 1
            win_los()
            print('1.Play')
            print('2.Shop')
            #a==int(input())
        elif a == 2:
            a -= 2
            shop_page()

main_pagee()