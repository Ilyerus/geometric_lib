import math
import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):

    # Тесты на корректность работы

    def test_area_positive(self):
        res = area(4)
        self.assertAlmostEqual(res, 50.26548245743669)

    def test_area_unit(self):
        res = area(1)
        trRes = math.pi
        self.assertAlmostEqual(res,trRes)

    def test_area_float(self):
        res = area(2.5)
        trRes = math.pi * 6,25
        self.assertAlmostEqual(res,trRes)

    def test_perimeter_positive(self):
        res = perimeter(3)
        trRes = math.pi
        self.assertAlmostEqual(res, 18.84955592153876)

    def test_perimeter_unit(self):
        res = perimeter(1)
        trRes = math.pi * 2
        self.assertAlmostEqual(res,trRes)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        trRes = math.pi * 5
        self.assertAlmostEqual(res,trRes)

    # Тесты на коммутативность
    # Неприменимо: функция принимает один аргумент (радиус).

    # Тесты на недопустимые значения

    def test_area_zero_radius_raises(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_zero_radius_raises(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_radius_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-1)

    # Тесты на строки

    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            area("1")

    def test_perimeter_string_raises(self):
        with self.assertRaises(TypeError):
            perimeter("1")