import unittest
from ejercicio import even_numbers, odd_numbers

class TestEvenNumbers(unittest.TestCase):
    def test_pares(self):
        self.assertEqual(even_numbers([1, 2, 3, 4]), [2, 4])

class TestOddNumbers(unittest.TestCase):
    def test_impares(self):
        self.assertEqual(odd_numbers([1, 2, 3, 4]), [1, 3])

if __name__ == '__main__':
    unittest.main()