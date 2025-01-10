import unittest
from ejercicio import remove_letter

class TestRemoveLetter(unittest.TestCase):
    def test_remover_letra(self):
        self.assertEqual(remove_letter("a", "banana"), "bnn")

    def test_sin_letra(self):
        self.assertEqual(remove_letter("x", "banana"), "banana")

if __name__ == '__main__':
    unittest.main()