i = int(input("Введите степень - "))
a = 0
b = 1
while a <= i:
    if a == 0:
        b = 1
        print("2^",a," = ",b)
    elif a > 0:
        b = b*2
        print("2^",a," = ",b)
    a += 1

