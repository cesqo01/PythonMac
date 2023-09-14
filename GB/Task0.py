# Задача №1. Общее обсуждение
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
import math

speed = int(input("Enter speed: "))
distance = int(input("Enter distance: "))
print(f"Машина проедет {distance} км за {math.ceil(distance/speed)} дней")

# (distance + speed - 1) // speed








