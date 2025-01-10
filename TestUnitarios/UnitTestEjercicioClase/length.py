import unittest
from ejercicio import length

class TestLength(unittest.TestCase):
    def test_menor_cinco(self):
        self.assertEqual(length([1, 2]), "Less than 5")

    def test_mayor_o_igual_cinco(self):
        self.assertEqual(length([1, 2, 3, 4, 5]), "Longer than 5")

if __name__ == '__main__':
    unittest.main()