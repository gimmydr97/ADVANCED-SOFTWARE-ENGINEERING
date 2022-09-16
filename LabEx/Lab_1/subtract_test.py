import calculator as c
import unittest
 
class TestSubtract(unittest.TestCase):
 
    def test_subtract_integers_positive(self):
        result = c.subtract(3, 2)
        self.assertEqual(result, 1)

    def test_subtract_integers_negative(self):
        result = c.subtract(-1, -2)
        self.assertEqual(result, 1)    

    def test_subtract_integers_pos_neg(self):
        result = c.subtract(1, -2)
        self.assertEqual(result, 3)  

    def test_subtract_integers_neg_pos(self):
        result = c.subtract(-1, 2)
        self.assertEqual(result, -3)  
 
 
if __name__ == '__main__':
    unittest.main()