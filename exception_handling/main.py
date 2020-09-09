a = input("Первое значение: ")
b = input("Второе значение: ")
try:
    a = int(a)
    b = int(b)
    c = a + b
    print("Результат:", c)
except:
    a = str(a)
    b = str(b)
    d = a + b
    print("Результат: ", d)
