# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

import random

rnd = random.randint(1, 11)
print(rnd)
list_1 = []
for i in range(rnd):
    n = random.randint(1, 11)
    list_1.append(n)
print(list_1)

for i in list_1:
    for j in list_1:
        if list_1[i] == list_1[j]:
            list_1.pop(j)
