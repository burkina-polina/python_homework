first_num = int(input('Введите первый элемент: '))
step = int(input('Введите шаг прогрессии: '))
length = int(input('Введите длинну прогрессии: '))
progression = []
for i in range(length):
    next_num = first_num + i * step
    progression.append(next_num)
print(progression)