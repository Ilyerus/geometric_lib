import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r
    Параметры:
        r (float) - радиус
    Возвращаемое значение:
        math.pi * r * r (float) - площадь
    Пример вызова:
    input: 4
    output: 50.26548245743669
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности с радиусом r
    Параметры:
        r (float) - радиус
    Возвращаемое значение:
        2 * math.pi * r (float) - периметр
    Пример вызова:
    input: 3
    output: 18.84955592153876
    '''
    return 2 * math.pi * r

