# Будко Вячеслав

# ДЗ №5

from random import randint
import json

# 1

with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введи ВСЁ или НИЧЕГО!: ')
        if not line:
            break
        f.write(f"{line}\n")
        print(line, file=f)

# 2

with open("text_2.txt", "r", encoding="utf-8") as f_two:
    useful = [f'{line}.{" ".join(count.split())} - {len(count.split())} слов(о\а)'
              for line, count in enumerate(f_two, 1)]
    print(*useful, f"Итого - {len(useful)}.", sep="\n")

# 3

with open("text_3.txt", "r", encoding="utf-8") as f_three:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f_three}
    print(f"Средний оклад = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n"
          f"Сотрудники с зарплатой менее 20к {[e[0] for e in employees_dict.items() if e[1] < 20000]}")

# 4

rus_dic = {'One': "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding="utf-8") as f_four:
    with open("text_4.txt", encoding="utf-8") as f_four_two:
        f_four.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in f_four_two])

# 5

with open("text_5.txt", "w", encoding="utf-8") as f_five:
    five_list = [randint(1, 100) for _ in range(100)]
    f_five.write(" ".join(map(str, five_list)))
print(f"Сумма элементов - {sum(five_list)}")

# 6

my_dict = {}
with open("text_6.txt", encoding="utf-8") as f_six:
    for line in f_six:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")

# 7

with open("text_7.json", "w", encoding="utf-8") as f_seven:
    with open("text_7.txt", encoding="utf-8") as f_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        result = [profit, {"average_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(result, f_seven, ensure_ascii=False, indent=4)
