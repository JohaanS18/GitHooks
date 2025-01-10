import unittest
from ejercicio import max

class TestMax(unittest.TestCase):
    def test_maximo_lista(self):
        self.assertEqual(max([1, 8, 3, 12]), 12)

    def test_lista_vacia(self):
        self.assertEqual(max([]), 0)

if __name__ == '__main__':
    unittest.main()