# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random

list_num = []
count_numbers = input("Введите количество чисел ")

if count_numbers.isdigit():
    count_numbers = int(count_numbers)
    for i in range(count_numbers):
        list_num.append(random.randint(1,10))
        i += 1
    print(list_num)

    number = input("Введите искомое число ")

    if number.isdigit():
        number = int(number)
        print(f'Искомое число встречается {list_num.count(number)} раз')
    else:
        print("Введите число")
else:
    print("Введите число")

