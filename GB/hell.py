n = 123456

sum1 = 0
count = 0
while (count != 3):
    sum1 += n % 10
    n //= 10
    count += 1

sum2 = 0
count = 0
while (count != 3):
    sum2 += n % 10
    n //= 10
    count += 1

# happy = sum1 == sum2
if sum1 == sum2:
    print("yes")
else:
    print("no")