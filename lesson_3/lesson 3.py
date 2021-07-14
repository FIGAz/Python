# Будко Вячеслав

# ДЗ №3

# 1
def div(a, b):
    try:
        a, b = int(a), int(b)
        div_num = a / b
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Мы не в институтеб дели нормально, не ломай математику"
    return round(div_num, 4)


print(div(input("Кто-нибудь, дайте цифру!!! - "), input("И давай её поделим - ")))


# 2

def p_info(**kwargs):
    return ' '.join(kwargs.values())


print(p_info(name=input("Name :"), surname=input("surname: "),
             birthday=input("birtday: "), city=input("city: "), email=input("email: "),
             p_number=input("Phone: ")))


# 3

def three_func(number_1, number_2, number_3):
    three_list = [number_1, number_2, number_3]
    try:
        three_list.remove(min(three_list))
        return sum(three_list)
    except TypeError:
        return "Как ты будешь слагать буквы? Поэт што-ли???"


print(three_func(123, 44, 256))


# 4

def four_func(x, y):
    try:
        grow = x ** y
    except TypeError:
        return "Первое циферное, второе твой баланс на карте."
    return grow


print(four_func(6.3, -26))


# 5
def five_func():
    add = 0
    while True:
        five_list = input("Валяй, кидай мне цифры! - ").split()
        for num in five_list:
            if num == "q":
                return add
            else:
                try:
                    add += int(num)
                except ValueError:
                    print("Законыил? Тыкай 'Q'.")
        print(f"Всего то = {add}")


print(five_func())


# 6

def six_func():
    for word in input("Слова, через пробел, маленькими буквами: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - Маленькими англицкими букавками.")


six_func()
