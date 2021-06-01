import unittest
from caesar_cipher import caesar_cipher

class CaesarTestCase(unittest.TestCase):
    """Tests for caesar_cipher.py."""
    def test_string1(self):
        self.assertEqual(caesar_cipher("Boy! What a string!", -5) , "Wjt! Rcvo v nomdib!")

    def test_string2(self):
        self.assertEqual(caesar_cipher("Hello zach168! Yes here.", 5) , "Mjqqt efhm168! Djx mjwj.")

    def test_string2_reverse(self):
        self.assertEqual(caesar_cipher("Hello zach168! Yes here.", -5) , "Czggj uvxc168! Tzn czmz.")

    def test_string3(self):
        self.assertEqual(caesar_cipher("BbBbB123!", -5) , "WwWwW123!")


if __name__ == '__main__':
    unittest.main()
