# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь
# перед некоторым кустом заданной во входном файле грядки.

import random

sum_bush = random.randint(5, 10)
print(sum_bush)
berrys = []
for _ in range(sum_bush):
    berrys.append(random.randint(5, 15))
print(berrys)
big_bushes = []
big_bush = 0
for i in range(len(berrys)):
    if i == 0:
        if berrys[i] + berrys[i + 1] + berrys[i + 2] > berrys[i] + berrys[i + 1] + berrys[len(berrys) - 1]:
            big_bush = berrys[i] + berrys[i + 1] + berrys[i + 2]
        if big_bush < berrys[i] + berrys[len(berrys) - 1] + berrys[len(berrys) - 2]:
            big_bush = berrys[i] + \
                berrys[len(berrys) - 1] + berrys[len(berrys) - 2]
        big_bushes.append(big_bush)
    elif i == 1:
        if berrys[i] + berrys[i + 1] + berrys[i + 2] > berrys[i] + berrys[i + 1] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[i + 1] + berrys[i + 2]
        if big_bush < berrys[i] + berrys[len(berrys) - 1] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[i] + \
                berrys[len(berrys) - 1] + berrys[i - 1]
        big_bushes.append(big_bush)
    elif i == len(berrys) - 1:
        if berrys[i] + berrys[0] + berrys[1] > berrys[i] + berrys[0] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[0] + berrys[1]
        if big_bush < berrys[i] + berrys[i - 2] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[i - 2] + berrys[i - 1]
        big_bushes.append(big_bush)
    elif i == len(berrys) - 2:
        if berrys[i] + berrys[i + 1] + berrys[0] > berrys[i] + berrys[i + 1] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[0] + berrys[i + 1]
        if big_bush < berrys[i] + berrys[i - 2] + berrys[i - 1]:
            big_bush = berrys[i] + berrys[i - 2] + berrys[i - 1]
        big_bushes.append(big_bush)

    elif berrys[i] + berrys[i + 1] + berrys[i + 2] > berrys[i] + berrys[i + 1] + berrys[i - 1]:
        big_bush = berrys[i] + berrys[i + 1] + berrys[i + 2]
    if big_bush < berrys[i] + berrys[i - 1] + berrys[i - 2]:
        big_bush = berrys[i] + berrys[i - 1] + berrys[i - 2]
    big_bushes.append(big_bush)

print(big_bushes)
print(set(big_bushes))
print(max(set(big_bushes)))
