list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input('Введите минимальное число диапазона: '))
max = int(input('Введите максимальное число диапазона: '))
result = []
for i in range(len(list)):
    if min <= list[i] <= max:
        result.append(i)
print(result)
