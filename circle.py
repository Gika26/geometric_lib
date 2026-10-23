import math


def area(r):
    '''
    Принимает радиус r и возвращает площадь круга.

    Пример вызова:
    area(2)
    Вывод: 12,56637
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус r и возвращает периметр круга.

    Пример вызова:
    perimeter(3)
    Вывод: 18,849555
    '''
    return 2 * math.pi * r

