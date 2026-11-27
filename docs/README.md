# Общее описание решений
Эта библиотека содержит четыре функции для работы с геометрическими фигурами

# Описание файлов
## rectangle.py
### area(a, b)
Возвращает значение площади прямоугольника по формуле $S = a * b $

```
Параметры:
    a (float) - первая сторона
    b (float) - вторая сторона
Возвращаемое значение:
    a * b (float) - площадь
```
**Пример вызова функции**
```python
input: 2 4
output: 8
input: 1.19 13.23
output: 15.7437
```
### perimeter(a, b)
Возвращает значение периметра прямоугольника по формуле $P = 2 * (a + b)$

```
Параметры:
    a (float) - первая сторона
    b (float) - вторая сторона
Возвращаемое значение:
    (a + b) * 2 (float) - периметр
```
**Пример вызова функции**
```python
input: 3 6
output: 18
input: 1.9 5.3
output: 14.399999999999999
```

## circle.py
Для работы функций в файле необходимо импортировать стандартную библиотеку math:
`import math`

### Функции
#### area(r)
Возвращает значение площади круга по формуле $S = \pi * r * r $

```
Параметры:
    r (float) - радиус
Возвращаемое значение:
    math.pi * r * r (float) - площадь
```
**Пример вызова функции**
```python
input: 1
output: 3.141592653589793
input: 4
output: 50.26548245743669
```
#### perimeter(r)
Возвращает значение длины окружности по формуле $C = 2 * \pi * r $

```
Параметры:
    r (float) - радиус
Возвращаемое значение:
    2 * math.pi * r (float) - периметр
```
**Пример вызова функции**
```python
input: 13
output: 81.68140899333463
input: 2.5
output: 15.707963267948966
```

## square.py
### Функции
#### area(a)
Возвращает значение площади квадрата по формуле $S = a * a $

```
Параметры:
    a (float) - сторона
Возвращаемое значение:
    a * a (float) - площадь   
```
**Пример вызова функции**
```python
input: 4
output: 16
input: 2.5
output: 6.25
```
#### perimeter(a)
Возвращает значение периметра квадрата по формуле $P = 4 * a $

```
Параметры:
    a (float) - сторона
Возвращаемое значение:
    4 * a (float) - периметр
```
**Пример вызова функции**
```python
input: 10
output: 40
input: 2.4
output: 9.6
```
##  triangle.py
### Функции
#### area(a, h)
Возвращает значение площади треугольника по формуле $S = \frac{a * h}{2} $

```
Параметры:
    a (float) - сторона
    h (float) - высота
Возвращаемое значение:
    a * h / 2 (float) - площадь
```
**Пример вызова функции**
```python
input: 3 4
output: 6
input: 1.73 1.65
output: 1.42725
```
#### perimeter(a, b, c)
Возвращает значение периметра треугольника по формуле $P = a + b + c $.

```
Параметры:
    a (float) - первая сторона
    b (float) - вторая сторона
    c (float) - третья сторона
Возвращаемое значение:
    a + b + c (float) - периметр
```
**Пример вызова функции**
```python
input: 2 2 3
output: 7
input: 1.2 2.7 3.5
output: 7.4
```

# Тестирование

Вызов unit-тестов:
>python3 -m unittest [исполняемый файл]

Выход все тестов:
```pyton
test_area_float (test_circle.CircleTestCase.test_area_float) ... ok
test_area_negative_radius_raises (test_circle.CircleTestCase.test_area_negative_radius_raises) ... FAIL
test_area_positive (test_circle.CircleTestCase.test_area_positive) ... ok
test_area_string_raises (test_circle.CircleTestCase.test_area_string_raises) ... ok
test_area_unit (test_circle.CircleTestCase.test_area_unit) ... ok
test_area_zero_radius_raises (test_circle.CircleTestCase.test_area_zero_radius_raises) ... FAIL
test_perimeter_float (test_circle.CircleTestCase.test_perimeter_float) ... ok
test_perimeter_negative_radius_raises (test_circle.CircleTestCase.test_perimeter_negative_radius_raises) ... FAIL
test_perimeter_positive (test_circle.CircleTestCase.test_perimeter_positive) ... ok
test_perimeter_string_raises (test_circle.CircleTestCase.test_perimeter_string_raises) ... ok
test_perimeter_unit (test_circle.CircleTestCase.test_perimeter_unit) ... ok
test_perimeter_zero_radius_raises (test_circle.CircleTestCase.test_perimeter_zero_radius_raises) ... FAIL
test_area_commutative (test_rectangle.RectangleTestCase.test_area_commutative) ... ok
test_area_float (test_rectangle.RectangleTestCase.test_area_float) ... ok
test_area_negative_side_raises (test_rectangle.RectangleTestCase.test_area_negative_side_raises) ... FAIL
test_area_positive (test_rectangle.RectangleTestCase.test_area_positive) ... ok
test_area_square (test_rectangle.RectangleTestCase.test_area_square) ... ok
test_area_string_raises (test_rectangle.RectangleTestCase.test_area_string_raises) ... FAIL
test_area_zero_side_raises (test_rectangle.RectangleTestCase.test_area_zero_side_raises) ... FAIL
test_perimeter_commutative (test_rectangle.RectangleTestCase.test_perimeter_commutative) ... ok
test_perimeter_float (test_rectangle.RectangleTestCase.test_perimeter_float) ... ok
test_perimeter_negative_side_raises (test_rectangle.RectangleTestCase.test_perimeter_negative_side_raises) ... FAIL
test_perimeter_positive (test_rectangle.RectangleTestCase.test_perimeter_positive) ... ok
test_perimeter_square (test_rectangle.RectangleTestCase.test_perimeter_square) ... ok
test_perimeter_string_raises (test_rectangle.RectangleTestCase.test_perimeter_string_raises) ... ok
test_perimeter_zero_side_raises (test_rectangle.RectangleTestCase.test_perimeter_zero_side_raises) ... FAIL
test_area_float (test_square.SquareTestCase.test_area_float) ... ok
test_area_large (test_square.SquareTestCase.test_area_large) ... ok
test_area_negative_side_raises (test_square.SquareTestCase.test_area_negative_side_raises) ... FAIL
test_area_positive (test_square.SquareTestCase.test_area_positive) ... ok
test_area_string_raises (test_square.SquareTestCase.test_area_string_raises) ... ok
test_area_unit (test_square.SquareTestCase.test_area_unit) ... ok
test_area_zero_side_raises (test_square.SquareTestCase.test_area_zero_side_raises) ... FAIL
test_perimeter_float (test_square.SquareTestCase.test_perimeter_float) ... ok
test_perimeter_large (test_square.SquareTestCase.test_perimeter_large) ... ok
test_perimeter_negative_side_raises (test_square.SquareTestCase.test_perimeter_negative_side_raises) ... FAIL
test_perimeter_positive (test_square.SquareTestCase.test_perimeter_positive) ... ok
test_perimeter_string_raises (test_square.SquareTestCase.test_perimeter_string_raises) ... FAIL
test_perimeter_unit (test_square.SquareTestCase.test_perimeter_unit) ... ok
test_perimeter_zero_side_raises (test_square.SquareTestCase.test_perimeter_zero_side_raises) ... FAIL
test_area_float (test_triangle.TriangleTestCase.test_area_float) ... ok
test_area_large (test_triangle.TriangleTestCase.test_area_large) ... ok
test_area_negative_side_raises (test_triangle.TriangleTestCase.test_area_negative_side_raises) ... FAIL
test_area_positive (test_triangle.TriangleTestCase.test_area_positive) ... ok
test_area_string_raises (test_triangle.TriangleTestCase.test_area_string_raises) ... ok
test_area_zero_height_raises (test_triangle.TriangleTestCase.test_area_zero_height_raises) ... FAIL
test_area_zero_side_raises (test_triangle.TriangleTestCase.test_area_zero_side_raises) ... FAIL
test_perimeter_equilateral (test_triangle.TriangleTestCase.test_perimeter_equilateral) ... ok
test_perimeter_float (test_triangle.TriangleTestCase.test_perimeter_float) ... ok
test_perimeter_inexistent_triangle_raises (test_triangle.TriangleTestCase.test_perimeter_inexistent_triangle_raises) ... FAIL
test_perimeter_inexistent_triangle_raises_2 (test_triangle.TriangleTestCase.test_perimeter_inexistent_triangle_raises_2) ... FAIL
test_perimeter_negative_side_raises (test_triangle.TriangleTestCase.test_perimeter_negative_side_raises) ... FAIL
test_perimeter_positive (test_triangle.TriangleTestCase.test_perimeter_positive) ... ok
test_perimeter_string_raises (test_triangle.TriangleTestCase.test_perimeter_string_raises) ... ok
test_perimeter_zero_side_raises (test_triangle.TriangleTestCase.test_perimeter_zero_side_raises) ... FAIL
```



# Коммиты проекта

```cmd
479c162 (HEAD -> main) Documentation added into files
83d2ee0 Docs upgated
e8fd508 Files Added
d078c8d (origin/main, origin/HEAD) L-03: Docs added
8ba9aeb L-03: Circle and square added
```