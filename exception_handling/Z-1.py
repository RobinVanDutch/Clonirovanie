a = input("Значение 1 -")
b = input("Значение 1 -")

try:
    a = int(a)
    b = int(b)
    c = a + b
    print("Результат", c)
except:
    a = str(a)
    b = str(b)
    c = a + b
    print(c)