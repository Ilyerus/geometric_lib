import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(2, 4)
        self.assertEqual(res, 8)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 10.0)

    def test_area_commutative(self):
        res1 = area(3, 7)
        res2 = area(7, 3)
        self.assertEqual(res1, res2)

    def test_perimeter_positive(self):
        res = perimeter(1, 4)
        self.assertEqual(res, 10)

    def test_perimeter_square(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_perimeter_float(self):
        res = perimeter(1.5, 2.5)
        self.assertAlmostEqual(res, 8.0)

    def test_perimeter_commutative(self):
        res1 = perimeter(3, 7)
        res2 = perimeter(7, 3)
        self.assertEqual(res1, res2)

    def test_area_zero_side_raises(self):
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_area_negative_side_raises(self):
        with self.assertRaises(ValueError):
            area(-1, 5)

    def test_perimeter_zero_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(0, 5)

    def test_perimeter_negative_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-1, 5)