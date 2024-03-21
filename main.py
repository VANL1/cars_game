import random

from cars import carsMatch
import config
import os
from time import sleep


def win_los():
    x=" "
    y=0
    z=0

    os.system('cls')
    print('.' * 156)
    print('''.                                                                                                                                                          .
.                                                                   |‾‾‾ |‾‾‾| |  | | / |  /|                                                              .
.                                                                   |    |   | |--| |/  | / |                                                              .
.                                                                   |    |___| |  | | \ |/  |                                                              .
.                                                                                                                                                          .''')
    print('.' * 156)



    print('Выберете машину на которую хотите поставить:')
    print("1.На первую                                             2.На вторую")
    select_car = int(input())
    if select_car!=1 and select_car!=2:
        print("Выберете машину на которую хотите поставить:")
        select_car = int(input())
    elif select_car==0:
        import menu
        menu.main_pagee()
    else:
        pass


    print(" " * 67, "Your balance:", config.money)
    print('Сделайте ставку:')
    bet = int(input())

    while bet>config.money:
        if bet > config.money:
            print("Недостаточно стредств")
            bet = int(input())
        elif bet < config.money:
            config.money -= bet
            print(f"Вы поставили {bet}$")
            sleep(3)





    while int(y)<=137 and int(z)<=137:
        carsMatch(x,y,z)
        z,y=carsMatch(x,y,z)

    x_bet = random.uniform(10, 24)
    x_bet = int(x_bet) / 10
    win_bet = x_bet * bet
    win_bet=int(win_bet)
    consolation = random.uniform(0, 100)
    consolation=int(consolation)

    if z>y:
        print(
            """
                                                       ВЫИГРАЛА ВТОРАЯ МАШИНА!!!!
                                                           ╲╲╲╲┗━━┳┳━━┛╱╱╱╱
                                                           ╲╲╭━━╮╭┻┻╮╭━━╮╱╱
                                                           ╲╲┃┊┊┣┫╭╮┣┫┊┊┃╱╱
                                                           ╲╲╰━╭┻╯┃┃╰┻╮━╯╱╱
                                                           ╲╭━╮╭━╲╭╮╱━╮╭━╮╱
                                                           ╲┃┊┣┻━━╰╯━━┻┫┊┃╱
                                                           ┈╰━┗━━━━━━━━┛━╯╱
                                                       ВЫИГРАЛА ВТОРАЯ МАШИНА!!!!
        """)
        if select_car == 2:
            print(f'Ваша ставка сыграла')
            print(f'Вы поставили {bet}$ на вторую машину, с коэфициентом {x_bet}')
            print(f'И вы выиграли: {win_bet}$')
        else:
            print(f'Ваша ставка не сыграла, вы проиграли: {bet}$ , но получили {consolation}$ как утешительный приз')
            config.money -= bet
            config.money += consolation
            print('Теперь ваша баланс', str(config.money))


    else:

        print(
            """
                                                        ВЫИГРАЛА ПЕРВАЯ МАШИНА!!!!
                                                            ╲╲╲╲┗━━┳┳━━┛╱╱╱╱
                                                            ╲╲╭━━╮╭┻┻╮╭━━╮╱╱
                                                            ╲╲┃┊┊┣┫╭╮┣┫┊┊┃╱╱
                                                            ╲╲╰━╭┻╯┃┃╰┻╮━╯╱╱
                                                            ╲╭━╮╭━╲╭╮╱━╮╭━╮╱
                                                            ╲┃┊┣┻━━╰╯━━┻┫┊┃╱
                                                            ┈╰━┗━━━━━━━━┛━╯╱
                                                        ВЫИГРАЛА ПЕРВАЯ МАШИНА!!!!
        """)
        if select_car==1:
            print(f'Ваша ставка сыграла')
            print(f'Вы поставили {bet}$ на первую машину, с коэфициентом {x_bet}')
            print(f'И вы выиграли: {win_bet}$')
            config.money+=win_bet
        else:
            print(f'Ваша ставка не сыграла, вы проиграли: {bet}$ , но получили {consolation}$ как утешительный приз')
            config.money-=bet
            config.money += consolation
            print('Теперь ваша баланс', str(config.money))





