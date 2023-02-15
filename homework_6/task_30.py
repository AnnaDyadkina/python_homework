# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_item = int(input("Введите первый элемент "))
dif = int(input("Введите разность элементов "))
sum_items = int(input("Введите количество элементов "))

def ar_progr(a_1, d, n):
    list_items = []
    for i in range(1, n+1):
        list_items.append(a_1 + (i-1) * d)
    return list_items

print(ar_progr(first_item, dif, sum_items))


