import unittest
from square import area
from square import perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_unit(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_positive(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    def test_area_large(self):
        res = area(100)
        self.assertEqual(res, 10000)

    def test_perimeter_unit(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_positive(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)

    def test_perimeter_large(self):
        res = perimeter(100)
        self.assertEqual(res, 400)

    def test_area_zero_side_raises(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_side_raises(self):
        with self.assertRaises(ValueError):
            area(-1)

    def test_perimeter_zero_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_side_raises(self):
        with self.assertRaises(ValueError):
            perimeter(-1)