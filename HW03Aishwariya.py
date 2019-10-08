import sys
import unittest
'Lets add, subtract, multiply, divide or compare Fractions!'
class Fraction:
   
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
        if denom == 0:
            raise ZeroDivisionError('0 is an invalid denominator')

      
       
        
    def __str__(self):
        'To represent our fraction'
        return f"{self.num} / {self.denom}"
        
    def __add__(self, other):
        'Does addition of fractions'

        numerator = self.num * other.denom + other.num * self.denom
        denominator = (self.denom * other.denom)
        
        common = gcd(numerator,denominator)
       
        return Fraction(numerator//common, denominator//common)
        
      
        
        
    def __sub__(self, other):
        'Does subtraction of fractions'
        numerator = self.num * other.denom - other.num * self.denom
        denominator = (self.denom * other.denom)

    
        common = gcd(numerator,denominator)
        
      
        return Fraction(numerator//common, denominator//common)

    def simplify(self):
        num = self.num
        denom = self.denom
        Fraction =f"{self.num} / {self.denom}"

        gcf = min(abs(num),abs(denom))
        
        if num%gcf == 0 and denom%gcf == 0:
            return num/gcf, denom/gcf
        else:
            return Fraction
        
      
        
        
    def __mul__(self, other):
        'Does multiplication of fractions'
        numerator = self.num * other.num 
        denominator = self.denom * other.denom

        common = gcd(numerator,denominator)

      
        return Fraction(numerator//common, denominator//common)
        
      
       
        
    def __truediv__(self, other):
        'Does division of fractions'
        numerator = self.num * other.denom
        denominator = self.denom * other.num

        common = gcd(numerator,denominator)

      
        return Fraction(numerator//common, denominator//common)
     
        
    def __eq__(self, other):
        'Checks if the fractions are of equal value'
        Y = (self.num * other.denom - other.num * self.denom)/(self.denom * other.denom)
        if Y == 0:
            return True
        if self.num/self.denom == other.num/other.denom:
            return True
        else:
            return False

   

        'Not equal'
    def __ne__(self, other):
        n1 = self.num/self.denom
        n2 = other.num/other.denom

        if n1 != n2:
            return True
        else :
            return False
        
        
        
        'less than'
    def __lt__(self, other):
        n1 = self.num/self.denom
        n2 = other.num/other.denom

        if n1 < n2:
            return True
        else:
            return False



        'Less than or equal to'
    def __le__(self, other):
        n1 = self.num/self.denom
        n2 = other.num/other.denom
        if n1 <= n2:
            return True

        else:
            return False

        'Greater than'
    def __gt__(self, other):
        n1 = self.num/self.denom
        n2 = other.num/other.denom

        if n1 > n2:
            return True
        else:
            return False

        'Greater than or equal to'
    def __ge__(self, other):
            
        n1 = self.num/self.denom
        n2 = other.num/other.denom

        if n1 >= n2:
            return True
        else:
            return False
   



'Finds the greatest common divisor'
def gcd(numerator, denominator):

        if(denominator == 0):
            return numerator
        else:
            return gcd(denominator, numerator%denominator)


    
class FractionTest(unittest.TestCase): 
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.denom, 4)
        
    def test_str(self):
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3 / 4')
        
        
    

    def test_add(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))
        self.assertTrue((f1 + f2 + f3) == Fraction(19, 12))
        

    def test_sub(self):
        """ test fraction subtraction """

        f1 = Fraction(3, 4)
        f2 = Fraction(3, 8)
        f3 = Fraction(1, 3)

        
        self.assertTrue((f1 - f2) == Fraction(3, 8))
        self.assertTrue((f1 - f3) == Fraction(5, 12))
        self.assertTrue((f3 - f1) == Fraction(-5, 12))
        self.assertTrue((f1 - f2 + f3) == Fraction(17, 24))

    def test_mul(self):
        """ test fraction multiplication """

        f1 = Fraction(3, 4)
        f2 = Fraction(3, 8)
        f3 = Fraction(1, 3)
        
        self.assertTrue((f1 * f2) == Fraction(9, 32))
        self.assertTrue((f1 * f3) == Fraction(3, 12))
        self.assertTrue((f3 * f2) == Fraction(1, 8))
        self.assertTrue((f1 * f2 + f3) == Fraction(59, 96))


    def test_truediv(self):
        """ test fraction division """

        f1 = Fraction(3, 4)
        f2 = Fraction(3, 8)
        f3 = Fraction(1, 3)
        
        self.assertTrue((f1 / f2) == Fraction(2, 1))
        self.assertTrue((f1 / f3) == Fraction(9, 4))
        self.assertTrue((f3 / f1) == Fraction(4, 9))
        self.assertTrue((f1 / f2 / f3) == Fraction(6, 1))

    def test_equal(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 ==f3)
        self.assertFalse(f1 == Fraction(3, 5))
        self.assertTrue((f1 - f2 + f3) == Fraction(9, 12))

    def test_notequal(self):
        """test fraction notequal """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 7)
        self.assertFalse(f1 != f1)
        self.assertFalse(f1 != f2)
        self.assertTrue(f1 != f3)
        self.assertTrue(f2 !=f3)
        self.assertTrue(f1 != Fraction(3, 5))
        self.assertTrue((f1 + f2 + f3) != Fraction(15, 12))

    def test_lt(self):
        """test fraction less than """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 10)
        self.assertFalse(f1 < f1)
        self.assertFalse(f1 < f2)
        self.assertTrue(f1 < f3)
        self.assertTrue(f2 < f3)
        self.assertFalse(f1 < Fraction(3, 5))
        self.assertFalse((f1 + f3) < Fraction(13, 12))

    def test_gt(self):
        """test fraction greater than """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 10)
        self.assertFalse(f1 > f1)
        self.assertFalse(f1 > f2)
        self.assertFalse(f1 > f3)
        self.assertFalse(f2 > f3)
        self.assertTrue(f1 > Fraction(3, 5))
        self.assertTrue((f1 + f3) > Fraction(13, 12))

    def test_le(self):
        """test fraction less than equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 10)
        self.assertTrue(f1 <= f1)
        self.assertTrue(f1 <= f2)
        self.assertTrue(f1 <= f3)
        self.assertTrue(f2 <= f3)
        self.assertFalse(f1 <= Fraction(3, 5))
        self.assertFalse((f1 + f3) <= Fraction(13, 12))
        


    def test_ge(self):
        """test fraction greater than equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 10)
        self.assertTrue(f1 >= f1)
        self.assertTrue(f1 >= f2)
        self.assertFalse(f1 >= f3)
        self.assertFalse(f2 >= f3)
        self.assertTrue(f1 >= Fraction(3, 5))
        self.assertTrue((f1 + f3) >= Fraction(13, 12))

    def test_exception(self):

        with self.assertRaises(ZeroDivisionError):
            Fraction(3, 0)
        with self.assertRaises(TypeError):
            0 + Fraction(2,4)
           
 

        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    
    