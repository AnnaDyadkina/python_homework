# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


num_a = int(input('Введите первое число '))
num_b = int(input('Введите второе число '))

def sum_nums(a, b):
    a = a + 1
    if b == 1:
        return a
    return sum_nums(a, b-1)

print(sum_nums(num_a, num_b))