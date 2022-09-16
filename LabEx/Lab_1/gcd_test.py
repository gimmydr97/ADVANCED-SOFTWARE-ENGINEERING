import calculator as c
import unittest
 
class Testgcd(unittest.TestCase):
 
    def test_gcd_integers_positive(self):
        result = c.gcd(6, 3)
        self.assertEqual(result, 3)

    def test_gcd_integers_positive2(self):
        result = c.gcd(64, 30)
        self.assertEqual(result,2)    
 
 
 
if __name__ == '__main__':
    unittest.main()