# 2) Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

max = -1000
min = 1000
num = int(input("Enter num: "))
for i in range(num):
    kg = int(input())
    if kg > max: max = kg
    if kg < min: min = kg
   
print(max, min)

# import random


# num = random.randint(5, 10)
# min_num_kg = 1000
# max_num_kg = -1000
# for i in range(num):
#     kg = int(input())
#     if kg < min_num_kg:  
#         min_num_kg = kg 
#     elif kg > max_num_kg:
#         max_num_kg = kg
# print(min_num_kg)
# print(max_num_kg)