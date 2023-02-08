berries = [1, 2, 3, 4]

def find_max_berries (n):
    max_berries = 0
    for i in range(len(n)):
        if i == 0:
            index_right = i + 1
            index_left = -1
        elif i == len(n) - 1:
            index_right = 0
            index_left = i - 1
        else:
            index_right = i + 1
            index_left = i - 1

        sum_berries = n[index_left] + n[i] + n[index_right]
        if sum_berries > max_berries:
            max_berries = sum_berries
    return max_berries

res_max = find_max_berries(berries)

print(res_max)




