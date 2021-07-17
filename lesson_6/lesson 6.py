# Будко Вячеслав

# ДЗ №6

# 1

# from time import sleep
#
# class TrafficLight:
#     __color = " "
#
#     def run(self):
#         while True:
#             print("Red")
#             sleep(7)
#             print("yellow")
#             sleep(2)
#             print("green")
#             sleep(7)
#
#
# trafficlight = TrafficLight()
# trafficlight.run()

# 2

# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def get_full_profit(self, weight=25, thickness=5):
#         return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
#                f"{(self._length * self._width * weight * thickness / 1000)} т"
#
#
# road_1 = Road(5000, 20)
# print(road_1.get_full_profit())

# 3

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"profit": wage, "bonus": bonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f"{self.name} {self.surname}"
#
#     def get_full_profit(self):
#         return f"{sum(self._income.values())}"
#
#
# meneger = Position("Ingvar", "Bread", "VMaker", 150000, 50000)
# print(meneger.get_full_name())
# print(meneger.get_full_profit())

# 4