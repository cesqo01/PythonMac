# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

import random

k = int(input("Enter k: "))
rnd = random.randint(4, 11)
print(rnd)
list_1 = []
for i in range(rnd):
    n = random.randint(1, 11)
    list_1.append(n)
print(list_1)

temp = 0
for i in range(len(list_1) - k):
    for j in range(len(list_1) - 1):
        list_1[j], list_1[j - 1] = list_1[j - 1], list_1[j]

print(list_1)
