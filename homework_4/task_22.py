m = int(input('Введите количество чисел первого множества '))

n = int(input('Введите количество чисел второго множества '))

def input_numbers (message, x):
    number_list = []
    i = 1
    while i <= x:
        item = int(input(message))
        number_list.append(item)
        i = i +1
    return number_list


numbers_1 = input_numbers('Введите число первого множества ', m)
numbers_2 = input_numbers('Введите число второго множества ', n)

print(numbers_1)
print(numbers_2)

numbers_1 = set(numbers_1)
numbers_2 = set(numbers_2)

res_numbers = numbers_1.union(numbers_2)

res_numbers = sorted(res_numbers)
print (res_numbers)

