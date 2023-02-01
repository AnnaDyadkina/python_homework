# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

import random
n = input('Введите количество монет ')
if n.isdigit():
    n = int(n)
    if n > 1:
        coins = []
        for i in range(n):
            coins.append(random.randint(0,1))
            i += 1
        print(coins)
        eagle_coins = coins.count(1)
        tails_coins = coins.count(0)
        if eagle_coins <= tails_coins:
            print(f'Нужно перевернуть {eagle_coins} монет/монету')
        elif tails_coins <= eagle_coins:
            print(f'Нужно перевернуть {tails_coins} монет/монету')
    else:
        print('Одна монетка. Введите большее количество монет')
else:
    print('Введите коректное количество монет')