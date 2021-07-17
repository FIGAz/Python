# Будко Вячеслав

# ДЗ №6

# 1

from time import sleep

class TrafficLight:
    __color = " "

    def run(self):
        while True:
            print("Red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(7)


trafficlight = TrafficLight()
trafficlight.run()

# 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f"{(self._length * self._width * weight * thickness / 1000)} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())

# 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


meneger = Position("Ingvar", "Bread", "VMaker", 150000, 50000)
print(meneger.get_full_name())
print(meneger.get_full_profit())

# 4

class Car:
    '''Автомобиль'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: Врум-Врум")

    def stop(self):
        print(f"{self.name}: Выбросили рельсу")

    def turn(self):
        print(f"{self.name}: Включай поворотники@*!#$@!!!")

    def show_speed(self):
        return f"{self.name}: Жми на гашетку, катимся как лохи: {self.speed}."

class TownCar(Car):
    '''Городской транспорт'''

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}, Куда торопимся, таки ты видел те штрафы?'\
            if self.speed > 60 else f"{self.name}: А мы разве не спешим?"

class WorckCar(Car):
    """Грузовой транспорт"""

    def show_speed(self):
        return f'{self.name}: Скорость авто: {self.speed}, У нас учет в рублях?'\
            if self.speed > 40 else f"{self.name}: У нас учет в сутках?"

class SportCar(Car):
    """Спортивный автомобиль"""

class PoliceCar(Car):
    """Полицейский транспорт"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town = TownCar("Труппер", "черный", 100)
town.go()
town.turn()
print(town.show_speed())
town.turn()
town.stop()
print()

work = WorckCar("Камаз", "Оранж", 80)
work.go()
work.turn()
print(work.show_speed())
work.stop()
print()

sport = SportCar("Велосипед", "Красный", 200)
sport.go()
sport.turn()
print(f"Скорость авто - {sport.speed}")
sport.stop()
print()

police = PoliceCar("ГИБДД", "Какой есть", 90)
police.go()
print(police.show_speed())
police.turn()
police.stop()
print()

# 5

class Stationery:
    def __init__(self, title="Будем рисовать"):
        self.title = title

    def draw(self):
        print(f"Что нам стоит дом дом построить, нарисуем будем жить! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Давай рисовать {self.title} ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Давай рисовать {self.title} кандарашом")


class Marker(Stationery):
    def draw(self):
        print(f"Давай рисовать {self.title} маркером")


stat = Stationery()
stat.draw()
pen = Pen("Шариковой")
pen.draw()
pencil = Pencil("Зелененьким")
pencil.draw()
marker = Marker("Перманентным")
marker.draw()