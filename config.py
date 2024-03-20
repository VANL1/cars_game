import os
from cars import car



car1 = car('Карыто', 1, 250)
car2 = car('Toyota Corolla(1992)', 2, 1000)



money=500


def shop_ui():
    #Оформление
    os.system('cls')
    print('.' * 156)
    print('''.                                                                                                                                                          .
.                                                     |\  /|   /\   |‾‾‾  /\   ‾‾‾‾| |  /| |  |                                                            .
.                                                     | \/ |  /__\  |    /__\  ----| | / | |--|                                                            .
.                                                     |    | /    \ |   /    \ ____| |/  | |  |                                                            .
.                                                                                                                                                          .''')
    print('.' * 156)

    # Баланс игрока
    print(" " * 67, "Your balance:", money)


    print('0.Выйти из магазина')
    print(" " * 10, f'1.{car1.model}, speed: {car1.speed}/10      {car1.price}$')
    print(" " * 10, f'1.{car2.model}, speed: {car2.speed}/10      {car2.price}$')


