# Будко Вячеслав

# ДЗ №4

# 1

from sys import argv
from random import randint
from functools import reduce
from itertools import count, cycle


def salary():
    try:
        hours, price, plus = map(float, argv[1:])
        print(f"Salary - {hours * price + plus}")
    except ValueError:
        print("Давай цифры, желательно 3, остальное на мне.")


salary()

# 2

two_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
more_before = [two_list[num] for num in range(1, len(two_list)) if two_list[num] > two_list[num - 1]]

print(more_before)

# 3

three_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(three_list)

# 4

four_list = [randint(-10, 10) for _ in range(20)]
u_list = [el for el in four_list if four_list.count(el) == 1]
print(f"Текущий лист\n{four_list}\nСписок уникальных значений\n{u_list}")


# 5

def five_list(a, b):
    return a * b


five_u_list = [el for el in range(100, 1001, 2)]
print(f"Список\n{five_u_list}\nПеремножаем все что есть\n{reduce(five_list, five_u_list)} ")

# 6

my_count = count(7)
my_cycle = cycle("ABC")

for _ in range(5):
    print("(my_count,my_cycle) = ({}, {})".format(next(my_count), next(my_cycle)))


# 7

def seven(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1


for el in seven(int(input("Факториал: "))):
    print(el)
