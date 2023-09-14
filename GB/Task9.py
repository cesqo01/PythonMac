num = input("Enter number: ")
while not num.isdigit():
    print("You entered incorrect number")
    num = input("Enter number: ")
num = int(num)
fact = 1
while (num != 0):
    fact *= num
    num -= 1
print(fact)
