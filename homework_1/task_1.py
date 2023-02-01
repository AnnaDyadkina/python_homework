# Задача 2: Найдите сумму цифр трехзначного числа.
n = input('Введите трехзначное число: ')

if n.isdigit() and 99 < int(n) < 1000:
    sum = 0
    for i in range(3):
        sum = sum + int(n[i])
    print(sum)
else:
    print('Нужно ввести трехзначное число')
