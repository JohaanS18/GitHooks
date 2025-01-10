import unittest
from ejercicio import mult

class TestMult(unittest.TestCase):
    def test_mult_positivo(self):
        self.assertEqual(mult(2), 14)  # 2 * (2 + 5)

    def test_mult_negativo(self):
        self.assertEqual(mult(-3), -24)  # -3 * (-3 + 5)

if __name__ == '__main__':
    unittest.main()