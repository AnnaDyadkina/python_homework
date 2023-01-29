# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

number_ticket = input('Введите шесть цифр ')

if len(number_ticket) == 6 and number_ticket.isdigit():
    sum_first = 0
    sum_second = 0
    for i in range(3):
        sum_first = sum_first + int(number_ticket[i])
        sum_second = sum_second + int(number_ticket[len(number_ticket) - i - 1])
    if sum_first == sum_second:
        print('yes')
    else:
        print('no')
else:
    print('Ошибка. Нужно ввести шесть цифр')
