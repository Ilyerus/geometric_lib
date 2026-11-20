import math
import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_unit(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_positive(self):
        res = area(4)
        self.assertAlmostEqual(res, 50.26548245743669)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25 * math.pi)

    def test_area_quadratic(self):
        res = area(3)
        self.assertAlmostEqual(res, 9 * math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_unit(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_positive(self):
        res = perimeter(3)
        self.assertAlmostEqual(res, 18.84955592153876)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 5 * math.pi)

    def test_perimeter_linear(self):
        res = perimeter(4)
        self.assertAlmostEqual(res, 8 * math.pi)