def ab():
    a = 1
    b = 1
    a = int(input('Введите число :'))
    b *= a
    while a != 0:
        a = int(input('Введите число 0 :'))
        if a == 0:
            break
            c *= b
    return b, c
print(ab())