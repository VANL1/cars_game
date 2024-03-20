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



    print('Выберете на какую машину ставить:')
    print("1.На первую                                             2.На вторую")
    select_car = int(input())

    print(" " * 67, "Your balance:", config.money)
    print('Сделайте ставку:')
    bet = int(input())
    while config.money>config.money-bet:
        select_car=select_car
        if select_car==1:
            select_car = 1
            if bet > config.money:
                print("Недостаточно стредств")
                bet = int(input())
                select_car = 0
            else:
                config.money-=bet
                print(f"Вы поставили {bet}$ на первую машину")
                sleep(3)
        elif select_car==2:
            if bet > config.money:
                print("Недостаточно стредств")
                bet = int(input())
                select_car = 2
            else:
                config.money -= bet
                print(f"Вы поставили {bet}$ на вторую машину")
                sleep(3)



    while int(y)<=137 and int(z)<=137:
        carsMatch(x,y,z)
        z,y=carsMatch(x,y,z)

    x_bet = random.uniform(9, 18)
    x_bet = x_bet / 10
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
        if select_car == 1:
            print(f'Ваша ставка сыграла, вы выиграли: {win_bet}$')
            config.money += win_bet
        else:
            print(f'Ваша ставка не сыграла, вы проиграли: {win_bet}$ , но получили {consolation}$ как утешительный приз')
            config.money -= win_bet
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
            print(f'Ваша ставка сыграла, вы выиграли: {win_bet}$')
            config.money+=win_bet
        else:
            print(f'Ваша ставка не сыграла, вы проиграли: {win_bet}$ , но получили {consolation}$ как утешительный приз')
            config.money-=win_bet
            config.money += consolation
            print('Теперь ваша баланс', str(config.money))





