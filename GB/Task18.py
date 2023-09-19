# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

import math

list_1 = [1, 2, 3, 4, 5]
k = 1
list_2 = []
list_min = []

for i in range(len(list_1)):
    if k == list_1[i]:
        print(k)
        exit

for i in range(len(list_1)):
    list_min.append(abs(k - list_1[i]))
    list_2.append(list_1[i])

b = min(list_min)
index = 0
for i in range(len(list_min)):
    if b == list_min[i]:
        index = i
print(list_2[index])
