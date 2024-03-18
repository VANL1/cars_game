import os
from main import win_los
def shop_page():
    os.system('cls')
    print('.'*156)
    print('''.                                                                                                                                                          .
.                                                     |\  /|   /\   |‾‾‾  /\   ‾‾‾‾| |  /| |  |                                                            .
.                                                     | \/ |  /__\  |    /__\  ----| | / | |--|                                                            .
.                                                     |    | /    \ |   /    \ ____| |/  | |  |                                                            .
.                                                                                                                                                          .''')
    print('.'*156)

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
            print('1.Играть снова?')
            print('2.Магазин')
            #a==int(input())
        elif a == 2:
            shop_page()
            a==0
            print('1.Играть снова?')
            print('2.Магазин')

main_pagee()
#shop_page()