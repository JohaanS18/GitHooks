import unittest
from ejercicio import total

class TestTotal(unittest.TestCase):
    def test_sumatoria_positiva(self):
        self.assertEqual(total([1, 2, 3]), 6)

    def test_sumatoria_vacia(self):
        self.assertEqual(total([]), 0)

    def test_sumatoria_negativa(self):
        self.assertEqual(total([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()