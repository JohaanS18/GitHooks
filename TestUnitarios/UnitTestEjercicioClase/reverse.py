import unittest
from ejercicio import reverse

class TestReverse(unittest.TestCase):
    def test_string_reverso(self):
        self.assertEqual(reverse("casa"), "asac")

    def test_string_vacio(self):
        self.assertEqual(reverse(""), "")

if __name__ == '__main__':
    unittest.main()