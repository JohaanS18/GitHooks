import unittest
from ejercicio import divide

class TestDivide(unittest.TestCase):
    def test_division_positiva(self):
        self.assertEqual(divide(8, 2), 4)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(8, 0)

if __name__ == '__main__':
    unittest.main()