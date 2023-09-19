# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

import random
rnd = random.randint(5, 10)
k = int(input("Enter number: "))
list_2 = [random.randint(10, 15) for _ in range(rnd)]
print(list_2)
count = 0
for el in list_2:
    if el == k:
        count += 1
print(count)

res_list = [1 for el in list_2 if el == k]
print(sum(res_list))

res_list = [1 if el == k else 0 for el in list_2]
print(sum(res_list))

res_set = {el for el in list_2 if el == k}
print(sum(res_set))

res_dict = {el: el*el for el in list_2 if el == k}
print(sum(res_dict))
