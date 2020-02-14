import unittest
from vector import *


class TestVectorFunction(unittest.TestCase):
    """
    class Vector function and method test
    """

    def test_float(self):
        """Test __float__"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result_a = float(a)
        result_b = float(b)
        mustbe_a = 5.38516
        mustbe_b = 6.48074
        print(f'\nResult: float(a): {result_a}\nValue test: {mustbe_a}')
        self.assertEqual(result_a, mustbe_a)
        print(f'Result: float(b): {result_b}\nValue test: {mustbe_b}')
        self.assertEqual(result_b, mustbe_b)

    def test_add(self):
        """Test __add__"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result = a + b
        mustbe = Vector(7, 7, 5)
        print(f'\nResult: a + b: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)

    def test_sub(self):
        """Test __sub__"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result = a - b
        mustbe = Vector(-3, -1, 3)
        print(f'\nResult: a - b: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)
        result = b - a
        mustbe = Vector(3, 1, -3)
        print(f'\nResult: b - a: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)

    def test_mul(self):
        """Test __mul__"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result = a * 2.5
        mustbe = Vector(5.0, 7.5, 10.0)
        print(f'\nResult: a * 2.5: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)
        result = a * b
        mustbe = 26.0
        print(f'\nResult: a * b: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)

    def test_eq(self):
        """Test __eq__, __lt__, __le__, __qt__, __qe__"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        print(f'\na = {float(a)}\nb = {float(b)}')
        print(f'Result: a==b: {a == b}')
        self.assertFalse(a == b)
        print(f'Result: a>b: {a > b}')
        self.assertFalse(a > b)
        print(f'Result: a>=b: {a >= b}')
        self.assertFalse(a >= b)
        print(f'Result: a<b: {a < b}')
        self.assertTrue(a < b)
        print(f'Result: a<=b: {a <= b}')
        self.assertTrue(a <= b)

    def test_get_vector_mul(self):
        """Test function get_vector_mul"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result = get_vector_mul(a, b)
        mustbe = Vector(-13, 18, -7)
        print(f'\nResult: [a * b]: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)

    def test_get_angle(self):
        """Test function get_angle"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        result = get_angle(a, b, 'd')
        mustbe = 41.84
        print(f'\nDegrees:\nResult: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)
        result = get_angle(a, b)
        mustbe = 0.73
        print(f'Radians:\nResult: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)
        a = Vector(4, -2, 0)
        b = Vector(7.5, 0, 4)
        result = get_angle(a, b, 'd')
        mustbe = 37.89
        print(f'\nDegrees:\nResult: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)
        result = get_angle(a, b)
        mustbe = 0.66
        print(f'Radians:\nResult: {result}\nValue test: {mustbe}')
        self.assertEqual(result, mustbe)

    def test_get_vector(self):
        """Test function get_vector"""
        x1, y1, z1 = 7, -3, 5
        x2, y2, z2 = 0, 5.5, -9
        b = get_vector((x1, y1, z1), (x2, y2, z2))
        mustbe = Vector(-7, 8.5, -14)
        print(f'\nResult: A{x1,y1,z1},B{x2,y2,z2}: {b}\nValue test: {mustbe}')
        self.assertEqual(b, mustbe)

    def test_is_collinear(self):
        """Test function is_collinear"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        e = a * 2.5
        print(f'\nResult: a{a} || b{b}: {is_collinear(a, b)}')
        self.assertFalse(is_collinear(a, b))
        print(f'Result: a{a} || e{e}: {is_collinear(a, e)}')
        self.assertTrue(is_collinear(a, e))

    def test_get_projection(self):
        """Test function get_projection"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        projection_ab = get_projection(a, b)
        projection_ba = get_projection(b, a)
        mustbe_ab = 4.01189
        mustbe_ba = 4.82808
        print(f'\nResult: a{a} on b{b}: {projection_ab}')
        print(f'Test value: {mustbe_ab}')
        self.assertEqual(projection_ab, mustbe_ab)
        print(f'Result: b{b} on a{a}: {projection_ba}')
        print(f'Test value: {mustbe_ba}')
        self.assertTrue(projection_ba, mustbe_ba)

    def test_is_aligned(self):
        """Test function is_aligned"""
        a = Vector(2, 3, 4)
        b = Vector(5, 4, 1)
        print(f'\nResult: a{a} aligned b{b}: {is_aligned(a, b)}')
        self.assertFalse(is_aligned(a, b))
        a = Vector(3, 6, 3)
        b = Vector(12, 24, 12)
        print(f'\nResult: a{a} aligned b{b}: {is_aligned(a, b)}')
        self.assertTrue(is_aligned(a, b))


if __name__ == '__main__':
    unittest.main(verbosity=2)



