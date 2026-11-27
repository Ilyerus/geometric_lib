import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    '''
       Тесты, которые проверяют правильность формулы
    '''
    def test_area_positive(self):
        res = area(2, 3)
        self.assertEqual(res, 3)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 5.0)

    def test_area_large(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_perimeter_positive(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_perimeter_equilateral(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_float(self):
        res = perimeter(1.5, 2.5, 3.0)
        self.assertAlmostEqual(res, 7.0)

    '''
        Тесты, которые проверяют корректность значения
    '''

    def test_area_zero_side_raises(self):
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_area_zero_height_raises(self):
        with self.assertRaises(ValueError):
            area(5, 0)

    def test_area_negative_side_raises(self):
        with self.assertRaises(ValueError):
            area(-1, 5)

    def test_perimeter_zero_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(0, 2, 3)

    def test_perimeter_negative_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 3)

    def test_perimeter_inexistent_triangle_raises(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)

    def test_perimeter_inexistent_triangle_raises_2(self):
        with self.assertRaises(ValueError):
            perimeter(1, 1, 10)

    '''
        Тесты, проверяющие корректность типа входных данных
    '''

    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            area("1", 5)

    def test_perimeter_string_raises(self):
        with self.assertRaises(TypeError):
            perimeter("1", 5, 10)