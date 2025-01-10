import unittest
from ejercicio import is_even

class TestIsEven(unittest.TestCase):
    def test_par(self):
        self.assertTrue(is_even(2))

    def test_impar(self):
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    unittest.main()