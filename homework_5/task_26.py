# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


num_a = int(input('Введите первое число '))
num_b = int(input('Введите второе число '))

def exp (x, y):
    if y >= 0:
        if y == 0:
            return 1
        elif y == 1:
            return x
        return x * exp(x, y-1)
    else:
        if y == -1:
            return x
        return 1 / (x * exp(x, y+1))

print(exp(num_a, num_b))