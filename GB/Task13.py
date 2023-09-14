# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

num = input("Enter number: ")
while num not in "1, 2, 3, 4, 5, 6, 7, 8, 9, 10":
    print("You entered incorrect number")
    num = input("Enter correct number: ")
num = int(num)
count = 0
max_count = 0

for t in range(num):
    tem = int(input("Enter number -50 - 50: "))
    if tem > 0:
        count += 1
    elif tem <= 0:
        count = 0
    if count > max_count:
        max_count = count    

print(max_count)        



   