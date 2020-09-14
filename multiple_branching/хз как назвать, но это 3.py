i = input("Введите число - ")
try:
    i = int(i)
    if i > 0:
        print(" 1")
    elif i < 0:
        print(" -1")
    if i == 0:
        print(" 0")
except ValueError:
    i = str(i)
    print("Введенное вами значение не является число")