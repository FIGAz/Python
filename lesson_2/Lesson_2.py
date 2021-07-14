# Будко Вячеслав

# ДЗ к уроку №2

# 1

type_list = [
    23.3, True, 'String', {12: 'Двенадцать', 1: 'Один'}, {31, 22}, [2, 131],
    (-41 + 0j), 32, range(31), bytearray(b'thirteen'), b'twelve',
    zip(*([26, 2], (1, 3), ('b', 'a'))), TypeError
]
for i, item in enumerate(type_list, 1):
    print(f"{i} {item} - {type(item)}")

# 2

list_num = list(input("Введите числа без белого - "))

for i in range(1, len(list_num), 2):
    list_num[i - 1], list_num[i] = list_num[i], list_num[i - 1]
print(list_num)

# 3

month = int(input("Стыдоба, ну давай расскажу тебе по месяцам года: "))

month_have = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
              9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "декабрь"]

if month in month_have:
    print(f"{month}-й месяц года - это {month_have[month]}")
    print(f"{month}-й месяц года - это {month_list[month - 1]}")
else:
    print("Ты где столько месяцев видел???")

seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

month_num = int(input('Введи цифру, астроном: '))

if month_num in sum(seasons.values(), []):
    for i in seasons.items():
        if month_num in i[1]:
            print(i[0])

# 4

string = input("Введи текст через космос - ").split()

for n, i in enumerate(string, 1):
    print(n, i) if len(i) <= 10 else print(n, i[:10])

# 5

myne_list = [9, 8, 8, 8, 5, 4, 3, 2, 2, 2, 1, 1, 1, 1, 1]

your_number = int(input("Давай мне цифру на сколько ты хороош из 10: "))
i = 0
for n in myne_list:
    if your_number <= n:
        i += 1
    else:
        break
myne_list.insert(i, your_number)
print(myne_list)

# 6

goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Закрыть "Q", "Ептег" для продолжения: ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f"Введите значение свойства '{f}'")
        f_copy[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analitics[f].append(f_copy[f])
    goods.append((num, f_copy))
    print(f"\n Структура товаров\n{goods}")
    print(f'\nТекущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analitics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)
