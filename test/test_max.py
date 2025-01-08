import unittest
from ejercicio import max

class TestMax(unittest.TestCase):
    def test_lista_positiva(self):
        resultado = max([1, 8, 3, 0, 12])
        self.assertEqual(resultado, 12)

    def test_lista_negativa(self):
        resultado = max([-1, -5, -3])
        self.assertEqual(resultado, -1)

if __name__ == '__main__':
    unittest.main()
