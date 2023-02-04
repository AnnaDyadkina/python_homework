# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

import random

count_numbers = input("Введите количество чисел ")
list_num = []

if count_numbers.isdigit():
    count_numbers = int(count_numbers)
    for i in range(count_numbers):
        list_num.append(random.randint(1,count_numbers))
    print(list_num)
    list_num = list(set(list_num))
    num = input("Введите число ")
    if num.isdigit():
        num = int(num)
        if num in list_num:
            print(f"Ближайшее число {num}")
        else:
            min_dif = abs(num - list_num[0])
            min_number = list_num[0]
            for j in list_num:
                if abs(num - j) < min_dif:
                    min_dif = abs(num - j)
                    min_number = j
            print(f"Ближайшее число {min_number}")
    else:
        print("Введите число")
else:
        print("Введите число")



