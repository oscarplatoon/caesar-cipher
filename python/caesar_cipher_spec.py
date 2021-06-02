from caesar_cipher import caesar_cipher
import unittest


class CaesarCipher(unittest.TestCase):
    ''' tests for caesar_cipher.py'''
    
    ''' when you call caesar_cipher, you get a string back.'''
    def test_returns_a_string(self):
        self.assertTrue(type(caesar_cipher("test", 0) == str))
    
    ''' when you call caesar_cipher, output accuracy is correct.'''
    def test_output_accuracy(self):
        self.assertTrue(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
        self.assertTrue(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
        
    ''' Challenge questions'''
    def test_function_challenge(self):
        self.assertTrue(caesar_cipher("Hello Zach168! Yes here.", -39) == "Uryyb Mnpu168! Lrf urer.")
        self.assertTrue(caesar_cipher("What. Is. This... ?!", 2) == "Yjcv. Ku. Vjku... ?!")
        self.assertTrue(caesar_cipher("Gut check, folks!", 24) == "Esr afcai, dmjiq!")
        
if __name__ == '__main__':
    unittest.main()
        


