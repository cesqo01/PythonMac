# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. Для этого Петя делает две подсказки.
#  Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(1, 1001)
y = random.randint(1, 1001)
print(x, y)

sum = x + y
mul = x * y
print(sum, mul)

second_dig = 0
first_dig = 0

for i in range(1, mul + 1):
    if second_dig + first_dig == sum:
        break
    if mul % i == 0 and i != mul:
        first_dig = i
        for j in range(i, mul + 1):
            if mul % j == 0:
                if first_dig + j == sum:
                    if first_dig * j == mul:
                        second_dig = j
                        break


print(first_dig, second_dig)
