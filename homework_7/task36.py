# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    matr = []
    for i in range(1, num_rows + 1):
        temp = []
        for j in range(1, num_columns + 1):
            temp.append(operation(i, j))
        matr.append(temp)
    for i in matr:
        i = ''.join(f'{n:>4}' for n in i)
        print(i)

print_operation_table(lambda x, y: x * y)



