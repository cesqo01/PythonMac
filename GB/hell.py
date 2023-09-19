k = "laptop"
k = k.upper()
count = 0

for i in k:
    if i in ("A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т", "R"):
        count += 1
    elif i in ("D", "G", "Д", "К", "Л", "М", "П", "У"):
        count += 2
    elif i in ("B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"):
        count += 3
    elif i in ("F", "H", "V", "W", "Y", "Й", "Ы"):
        count += 4
    elif i in ("K", "Ж", "З", "Х", "Ц", "Ч"):
        count += 5
    elif i in ("J", "X", "Ш", "Э", "Ю"):
        count += 8
    elif i in ("Q", "Z", "Ф", "Щ", "Ъ"):
        count += 10

print(count)

# k = k.upper()
# if k.isascii() == True:
#     for i in range(len(k)):
#         if k[i] == "A" or "E" or "I" or "O" or "U" or "L" or "N" or "S" or "T" or "R":
#             count += 1
#         elif k[i] == "D" or "G":
#             count += 2
#         elif k[i] == "B" or "C" or "M" or "P":
#             count += 3
#         elif k[i] == "F" or "H" or "V" or "W" or "Y":
#             count += 4
#         elif k[i] == "K":
#             count += 5
#         elif k[i] == "J" or "X":
#             count += 8
#         elif k[i] == "Q" or "Z":
#             count += 10
# else:
#     for i in range(len(k)):
#         if k[i] == "А" or "В" or "Е" or "И" or "Н" or "О" or "Р" or "С" or "Т" or "R":
#             count += 1
#         elif k[i] == "Д" or "К" or "Л" or "М" or "П" or "У":
#             count += 2
#         elif k[i] == "Б" or "Г" or "Ё" or "Ь" or "Я":
#             count += 3
#         elif k[i] == "Й" or "Ы":
#             count += 4
#         elif k[i] == "Ж" or "З" or "Х" or "Ц" or "Ч":
#             count += 5
#         elif k[i] == "Ш" or "Э" or "Ю":
#             count += 8
#         elif k[i] == "Ф" or "Щ" or "Ъ":
#             count += 10
# print(count)
