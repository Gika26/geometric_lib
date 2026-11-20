import unittest
import math

import circle
import triangle
import square
import rectangle


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle.area(3, 4, 5), 6)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)


if __name__ == '__main__':
    unittest.main()