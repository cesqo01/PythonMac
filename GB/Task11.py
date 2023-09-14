# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

num = input("Enter number > 1: ")
while not num.isdigit():
    print("You entered incorrect number")
    num = input("Enter correct number: ")
    if num < 2:
        num = input("Enter correct number: ")

num = int(num)
fib1 = 0
fib2 = 1
fib = 1
count = 2

while fib < num:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    count += 1
if fib == num:
    print(count)
else:
    print(-1)
