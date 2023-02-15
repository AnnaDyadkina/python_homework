# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

len_list = int(input("Введите длину списка "))

def create_list(sum_items):
    input_list = []
    for _ in range(sum_items):
        input_list.append(int(input("Введите элемент списка ")))
    return input_list

list_nums = create_list(len_list)

print(list_nums)

input_min = int(input("Введите минимальное значение "))
input_max = int(input("Введите максимальное значение "))

def find_index(list_items, min_item, max_item):
    res_list = []
    for i in range(len(list_items)):
        if list_items[i] >= min_item and list_items[i] <= max_item:
            res_list.append(i)
    if len(res_list) > 0:
        return res_list
    else:
        return "Ни одно число не входит в диапазон"

if input_min < input_max:
    index_list = find_index(list_nums, input_min, input_max)
    print(index_list)
else:
    print("Введите корректный диапазон")

