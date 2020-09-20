def test():
    int_x = int(input('Введите целое число: '))
    if int_x > 0:
        positive()
    else:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')

test()
