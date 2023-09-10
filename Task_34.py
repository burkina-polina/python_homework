def rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in "aeиоуыэюя":
                result += 
        list.append(result)
    return len(list) == list.count(list[0])

str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-да'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print(Пам парам)