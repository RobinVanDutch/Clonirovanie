old = input('Ваш возраст: ')
try:
    old = int(old)
    print('Рекомендовано:', end=' ')
    if 3 <= old < 6:
        print('"Ребенок"')
    elif 6 <= old < 12:
        print('"шкет"')
    elif 12 <= old < 16:
        print('"малолетка"')
    elif 16 <= old:
        print('"ты вырос чтоли?"')
    else:
        print("Старпер")
except ValueError:
    print("Введите число позязя")