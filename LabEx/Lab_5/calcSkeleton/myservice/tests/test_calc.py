import unittest
import json
from flask import request, jsonify
from myservice import app 

app.testing = True

#TODO: Extend these component tests for the calc view 
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):

    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3&n=5').get_json()
        self.assertEqual(reply['result'], '8')
        
    def test_sum2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=-1&n=-2').get_json()
        self.assertEqual(reply['result'], '-3')  
    
    def test_sum3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=1&n=-2').get_json()
        self.assertEqual(reply['result'], '-1')
    
    def test_sum4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=-1&n=2').get_json()
        self.assertEqual(reply['result'], '1')
    
    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=3&n=5').get_json()
        self.assertEqual(reply['result'], '15')
        
    def test_mul2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-1&n=-2').get_json()
        self.assertEqual(reply['result'], '2')  
    
    def test_mul3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=1&n=-2').get_json()
        self.assertEqual(reply['result'], '-2')
    
    def test_mul4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-1&n=2').get_json()
        self.assertEqual(reply['result'], '-2')
    

    def test_mul5(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=0&n=2').get_json()
        self.assertEqual(reply['result'], '0')
    

    def test_mul4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-1&n=0').get_json()
        self.assertEqual(reply['result'], '0')
    
    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=8&n=5').get_json()
        self.assertEqual(reply['result'], '3')
        
    def test_sub2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=-1&n=-2').get_json()
        self.assertEqual(reply['result'], '1')  
    
    def test_sub3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=1&n=-2').get_json()
        self.assertEqual(reply['result'], '3')
    
    def test_sub4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sub?m=-1&n=2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=3&n=0').get_json()
        self.assertEqual(reply['result'], 'DivisionByZeroError')

    def test_div2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=6&n=3').get_json()
        self.assertEqual(reply['result'], '2')
    
    def test_div3(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=7&n=3').get_json()
        self.assertEqual(reply['result'], '2')
        
    def test_div4(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=-6&n=-2').get_json()
        self.assertEqual(reply['result'], '3')
    
    def test_div5(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=6&n=-2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_div6(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=-6&n=2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_div7(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/divide?m=0&n=2').get_json()
        self.assertEqual(reply['result'], '0')