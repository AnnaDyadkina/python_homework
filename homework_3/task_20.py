# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

scrabble = {}
list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
list_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

for i in list_1:
    scrabble.setdefault(i, 1)

for i in list_2:
    scrabble.setdefault(i, 2)

for i in list_3:
    scrabble.setdefault(i, 3)

for i in list_4:
    scrabble.setdefault(i, 4)

for i in list_5:
    scrabble.setdefault(i, 5)

for i in list_8:
    scrabble.setdefault(i, 8)   

for i in list_10:
    scrabble.setdefault(i, 10) 

input_value = input('Введите слово ')
if input_value.isalpha():
    input_value = input_value.upper()
    total = 0
    for i in input_value:
        total = total + scrabble[i]
    print(total)
else:
    print("Ошибка. Введите слово")