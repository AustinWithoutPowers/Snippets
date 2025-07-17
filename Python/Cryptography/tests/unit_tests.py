import unittest
from core.key_classes import PrivateKey

class TestKeys(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_get_private_key(self):
        test_key = PrivateKey(bit_size=32)
        self.assertIsNotNone(test_key.get_private_key())
    
    def test_non_prime_key(self):
        with self.assertRaises(ValueError) as context:
            test_key = PrivateKey(private_key=58983, bit_size=16)
        self.assertTrue('Key is not a prime number!' in str(context.exception))
    
    def test_key_too_big(self):
        with self.assertRaises(ValueError) as context:
            test_key = PrivateKey(private_key=131, bit_size=4)
        self.assertTrue('Key is too big!' in str(context.exception))

if __name__ == '__main__':
    unittest.main()