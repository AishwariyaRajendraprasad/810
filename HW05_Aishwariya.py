import unittest
def my_reverse(s):
    'Reverse the string without using reversed()'
    
    x=""
    for i in range(len(s)-1,-1,-1):
        x += s[i]
    return x

def rev_enumerate(seq):
    'My enumerate function in reverse'
    for i in range(len(seq)-1, -1, -1):
        item = seq[i]
        yield i,item

def second_occur(str,s):
    'Finds the second occurence of the string'
    second_occur = str.find(s)
    return str.find(s,second_occur +1 )
    # chote code ke liye theek hai.











class ReverseTest(unittest.TestCase):

    def test_my_reverse(self):
        
        self.assertTrue(my_reverse("Hello")=="".join(reversed("Hello")))
        self.assertTrue(my_reverse("01234")=="".join(reversed("01234")))
        self.assertTrue(my_reverse("Ashu")=="".join(reversed("Ashu")))
        self.assertTrue(my_reverse("1+2=3")=="".join(reversed("1+2=3")))

    def test_rev_enum(self):

        self.assertEqual(list(rev_enumerate("Aishwariya")),list(reversed(list(enumerate(("Aishwariya"))))))
        self.assertEqual(list(rev_enumerate("12345")),list(reversed(list(enumerate(("12345"))))))
        self.assertEqual(list(rev_enumerate("Hi1Bye2")),list(reversed(list(enumerate(("Hi1Bye2"))))))
        self.assertEqual(list(rev_enumerate("010101")),list(reversed(list(enumerate(("010101"))))))

    def test_second_occur(self):

        self.assertEqual(second_occur('aafindoutaa','aa'),9)
        self.assertEqual(second_occur('012345012101','01'),6)
        self.assertEqual(second_occur('abbabba','abba'),3)
        self.assertEqual(second_occur('smart31art3','art3'),7)
       

           
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)