import unittest
import copy

def remove_vowels(str):
    'Removes the vowels present in the string'

    vowels = ('a','e','i','o','u')
    return "".join([x for x in str.lower() if x not in vowels])

def check_pwd(pwd):
    'To check the password, if it has at least a uppercase, a lowercase and a digit'

    return all([any(c.isupper()for c in pwd),any(c.islower()for c in pwd),any(c.isdigit()for c in pwd)])

class BTree:
    'Binary Tree to insert, find and traverse the tree'

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value


    def insert(self, value):
        'Inserts values to the tree'

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def find(self, Fval):
        'Finds values if present in the tree'

        if Fval < self.value:
            if self.left is None:
                return False
            return self.left.find(Fval)
        elif Fval > self.value:
            if self.right is None:
                return False
            return self.right.find(Fval)
        else:
            return True

    def Traverse(self,bt):
        'Traverses the tree'
        
        Traverse = []
        if bt:
            Traverse = self.Traverse(bt.left)
            Traverse.append(bt.value)
            Traverse += self.Traverse(bt.right)
        return Traverse

def my_sort(l):
    'my sort function which saves a copy of sorted list without using sort'

    l2 = copy.copy(l)

    for i in range(len(l2)):
        for j in range(i + 1, len(l2)):

            if l2[i] > l2[j]:
                l2[i], l2[j] = l2[j], l2[i]

    return l2

def insertion_sort(l2):
    'Inserts sorted lists into an empty list'

    lst = list()

    for item in l2:
        offset = 0
        while offset<len(lst) and item >lst[offset]:
            offset+=1
        lst.insert(offset,item)
    return lst


class RvCpBtIsTest(unittest.TestCase):

    def test_remove_vowels(self):
        'Tests for remove_vowels'

        self.assertEqual(remove_vowels('hello world'), 'hll wrld')

        self.assertEqual(remove_vowels('Aishwariya'), 'shwry')

        self.assertEqual(remove_vowels('Harishjitu'), 'hrshjt')

        self.assertEqual(remove_vowels('Hi1Bye2'),'h1by2')


    def test_check_pwd(self):
        'Tests for check_pwd'

        self.assertTrue(check_pwd('Abcd333'))

        self.assertTrue(check_pwd('AAAABbbcc44'))

        self.assertFalse(check_pwd('aaaa22'))

        self.assertFalse(check_pwd('AABB'))

        self.assertFalse(check_pwd('2222222'))
            



    def test_BTree(self):
        'Tests for Binary Tree'


        bt = BTree(27)
        bt.insert(1)
        bt.insert(15)
        bt.insert(5)
        bt.insert(30)
        bt.insert(-4)

        self.assertTrue(bt.find(1))

        self.assertTrue(bt.find(5))

        self.assertTrue(bt.find(15))

        self.assertFalse(bt.find(9))
        
        self.assertEqual(bt.Traverse(bt),[-4,1,5,15,27,30])



    def test_check_insertionsort(self):
        'Tests for insertion_sort'

        self.assertEqual(insertion_sort([1,7,4,2,5,7]),[1,2,4,5,7,7])

        self.assertEqual(insertion_sort([1000,4,44,66,2,4,6,7,2]),[2,2,4,4,6,7,44,66,1000])

        self.assertEqual(insertion_sort([-1,-2,0,22,4,3,5,6,7,7]),[-2,-1,0,3,4,5,6,7,7,22])

        self.assertEqual(insertion_sort([0,000,9]),[0,000,9])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    

    