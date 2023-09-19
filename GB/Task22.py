# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

import random

num1 = input("Enter sum elems for first set:  ")
while not num1.isdigit():
    print("You entered incorrect number")
    num1 = input("Enter correct number: ")

num2 = input("Enter sum elems for second set:  ")
while not num2.isdigit():
    print("You entered incorrect number")
    num2 = input("Enter correct number: ")

num1, num2 = int(num1), int(num2)

set1 = set()
set2 = set()

for _ in range(num1):
    set1.add(random.randint(1, 20))
for _ in range(num2):
    set2.add(random.randint(1, 20))

print(set1, set2)

if set1 & set2:
    print(set(set1 & set2))  # sorted
else:
    print("No intersection")
