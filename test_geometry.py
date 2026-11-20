import unittest

import circle
import triangle
import square
import rectangle


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 12.5663706)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-2)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("abc")

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_large(self):
        self.assertAlmostEqual(circle.area(1000000), 3141592653589.793)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.5663706)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-2)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("abc")

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_large(self):
        self.assertAlmostEqual(circle.perimeter(1000000), 6283185.307179586)


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle.area(3, 4, 5), 6)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-3, 4, 5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            triangle.area("abc", 4, 5)

    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 0, 0), 0)

    def test_area_large(self):
        self.assertAlmostEqual(triangle.area(3000000, 4000000, 5000000), 6000000000000)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("abc", 4, 5)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_large(self):
        self.assertEqual(triangle.perimeter(3000000, 4000000, 5000000), 12000000)


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            square.area("abc")

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_large(self):
        self.assertEqual(square.area(1000000), 1000000000000)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("abc")

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_large(self):
        self.assertEqual(square.perimeter(1000000), 4000000)


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 4)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("abc", 4)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(0, 4), 0)

    def test_area_large(self):
        self.assertEqual(rectangle.area(1000000, 2000000), 2000000000000)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 4)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("abc", 4)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 4), 8)

    def test_perimeter_large(self):
        self.assertEqual(rectangle.perimeter(1000000, 2000000), 6000000)


if __name__ == '__main__':
    unittest.main()