def function():
    a = int(input("Введите числа:"))
    print("Чтобы закончить подсчет произведения, введите 0 ")
    b = a
    while a != 0:
        a = int(input())
        if a == 0:
            break
        c = a * b
        b = c
    return b
print(function())