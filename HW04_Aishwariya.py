import unittest
import HW03Aishwariya

def count_vowels(s):
    'To count number of vowels present in a string'
    s = s.lower()
    vowels=0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels+=1
    return vowels

def position(li,c):
    'To count the last occurence of the target item in the list'
    
    flag = -1
    for i in range(len(li)):
        if(li[i] == c):
            flag = i

    if(flag == -1):
        return None
    else:
        return flag

def my_enumerate(seq):
    'My method for enumerating using yield'
   
    yield from seq

def counter():
    'To keep count of the items'
    i = 0
    while True:
        yield i
        i +=1
gen = counter()
for item in my_enumerate("Aishwariya"):
    print(next(gen),item)

def simplify(self):
    'Simplifies the given fraction'
    num = self.num
    denom = self.denom
    Fraction =f"{self.num} / {self.denom}"

    gcf = min(abs(num),abs(denom))
    
    if num%gcf == 0 and denom%gcf == 0:
        return num/gcf, denom/gcf
    else:
        return Fraction



class CpgeTest(unittest.TestCase):
    'Test Cases'

    def test_count_vowels(self):

        self.assertEqual(count_vowels('hello world'), 3)

        self.assertEqual(count_vowels('hEllO wrld'), 2)

        self.assertEqual(count_vowels('hll wrld'), 0)

        self.assertEqual(count_vowels('Aishwariya1'),5)

    def test_position(self):

        self.assertEqual(position([1,2,3,4,4,4],4),5)
        self.assertEqual(position([42,31,33,55,33],33),4)
        self.assertEqual(position(['apple','and','poem'],'p'),None)
        self.assertEqual(position('apple','p'),2)

    def test_enumerate(self):
        list(my_enumerate("Aishwariya")) == list(enumerate("Aishwariya"))
        list(my_enumerate("12345")) == list(enumerate("12345"))
        list(my_enumerate("hello12hi46")) == list(enumerate("hello12hi46"))

    def test_gcf(self):
        'returns a new instance of class Fraction with the appropriate numerator and denominator.'
    
        str(HW03Aishwariya.Fraction(9, 27).simplify()) == str(HW03Aishwariya.Fraction(1, 3))
        str(HW03Aishwariya.Fraction(9, 3).simplify()) == str(HW03Aishwariya.Fraction(3, 1))
        str(HW03Aishwariya.Fraction(1, 2).simplify()) == str(HW03Aishwariya.Fraction(1, 2))
        str(HW03Aishwariya.Fraction(-5, 10).simplify()) == str(HW03Aishwariya.Fraction(-1,2))
        str(HW03Aishwariya.Fraction(2, -10).simplify()) == str(HW03Aishwariya.Fraction(1,-5))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)