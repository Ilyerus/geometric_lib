import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive(self):
        res = area(2, 4)
        self.assertEqual(res, 8)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 10.0)

    def test_area_commutative(self):
        res = area(3, 7)
        self.assertEqual(res, area(7, 3))

    def test_perimeter_positive(self):
        res = perimeter(1, 4)
        self.assertEqual(res, 10)

    def test_perimeter_square(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = perimeter(1.5, 2.5)
        self.assertAlmostEqual(res, 8.0)

    def test_perimeter_commutative(self):
        res = perimeter(3, 7)
        self.assertEqual(res, perimeter(7, 3))