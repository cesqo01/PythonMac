# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# 2028, 2024, 2020, 2016, 2012, 2008, 2004, 2000, 1996, 1992, 1988, 1984, 1980, 1976, 1972, 1968, 1964, 1960,
# 1956, 1952, 1948, 1944, 1940, 1936, 1932, 1928, 1924, 1920, 1916, 1912, 1908, 1904

# year = int(input("Введите год: "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Yes")
# else:
#     print("No")


# Дано натуральное число - год. Требуется определить,
# является ли год с данным номером високосным.
# Если год является високосным, то выведите YES,
# иначе выведите NO. Напомним, что в соответствии
# с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100), а также если он кратен 400.
# Input: 2016
# Output: YES

# 2028, 2024, 2020, 2016, 2012, 2008, 2004, 2000,
# 1996, 1992, 1988, 1984, 1980, 1976, 1972, 1968, 1964, 1960, 19
# 56, 1952, 1948, 1944, 1940, 1936, 1932, 1928, 1924, 1920, 1916, 1912, 1908, 1904,

# year = int(input("Enter year: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Yes")
# else:
#     print("No")

# print(16 % 4 == 0)


if not 16 % 4:
    print("yes")


else:
    print("no")