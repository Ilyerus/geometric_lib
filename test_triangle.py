import unittest
from triangle import area
from triangle import perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_area_zero_height(self):
        res = area(5, 0)
        self.assertEqual(res, 0)

    def test_area_positive(self):
        res = area(2, 3)
        self.assertEqual(res, 3)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 5.0)

    def test_area_large(self):
        res = area(10, 20)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_unit(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_positive(self):
        res = perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_perimeter_float(self):
        res = perimeter(1.5, 2.5, 3.0)
        self.assertAlmostEqual(res, 7.0)

    def test_perimeter_large(self):
        res = perimeter(100, 200, 300)
        self.assertEqual(res, 600)