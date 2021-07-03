# 1
a = "Hi,"
b = "welcome!"

print(f"{a} {b}")

num1 = int(input("Введите число: "))
num2 = int(input("Введите число еще раз: "))

print(f"Вы ввели {num1} и {num2}.")

any_str = input("Здесь могла бы быть Ваша реклама: ")

print(f"{any_str} - могли бы придумать и получше.")

# 2

time = int(input("Ваши секунды мы перевернум во время: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

# 3

numb = input("Введите число: ")
while numb < '0':
    print("Число больше 0, пожалуйста. давай по новой!")
    numb = input("Введите число большЕе 0: ")

print(f"{numb} + {numb + numb} + {numb + numb + numb} = {int(numb) + int(numb + numb) + int(numb + numb + numb)}")

# 4

number = int(input("Кто-нибудь, дайте однозначное число этому Питону: "))
current_max = 0
save_num = number
while save_num > 0:
    last = save_num % 10
    if last > current_max:
        current_max = last
        if current_max == 9:
            break
    save_num = save_num // 10
print(f"Столько цифр {number}, Могли бы и не жадничать, всего то {current_max}")

# 5

income = float(input("Дайте деняг(желательно доллары) - "))
output = float(input("Потери пока рыдали над выручкой(доллары) - "))
itogo = income - output

if itogo > 0:
    print(f"Ну что, взрывай шампанское, у нас приход {itogo} долларов")
    print(f"А если точнее то {itogo * 100 / income:.1f}%")
    rab = int(input("Скольких иждевенцев нам содержать???"))
    print(f"Если ты выжил из ума, то можешь дать им {itogo / rab:.3f} долларов, а нам оно надо?")
elif itogo < 0:
    print(f"Денег как известно нет, а теперь стало на {-itogo} и меньше.")
else:
    print("Работаем в ноль, не палимся перед налоговой...")

# 6

while True:
    days_gone = 1
    start = float(input("А сколько тебе надо?: "))
    end = float(input("Ну и чего ты этим хочешь добиться?: "))
    if start <= 0 or end < 0:
        print("Лежа на диване горб не заработаешь. А тебе надо больше 0.")
    else:
        while start < end:
            start += start * 0.1
            days_gone += 1

        print(f"Ожидается образование грыжи за {days_gone} дней...")
        break
