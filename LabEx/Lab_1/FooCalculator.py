import calculator as c 

class FooCalculator:

    #empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m, n)
    
    def subtract(self, m, n):
        return c.subtract(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def divide(self, m, n):
        return c.divide(m, n)
    
    def gcd(self, m, n):
        return c.gcd(m, n)