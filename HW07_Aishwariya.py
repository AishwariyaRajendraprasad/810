import unittest
from collections import defaultdict
from collections import Counter

def anagram(str1,str2):
    'Checking anagrams'

    if sorted(str1.lower().replace(" ",""))==sorted(str2.lower().replace(" ","")):
        return True
    else:
        return False


def anagram_dd(str1,str2):
    'Checking Anagrams using defaultdicts'
    str1 = sorted(str1.lower().replace(" ",""))
    str2 = sorted(str2.lower().replace(" ",""))
    dd = defaultdict(int)

    for k in str1:
        dd[k] +=1

    if str1==str2:    
        for ch in str2:
        
            if ch in dd.keys():
                    
                dd[ch] -=1


    if all(value == 0 for value in dd.values()):
        return True
    else:
        return False
  


def anagram_counter(str1,str2):
    'Checking anagrams using counters'
    
    c1 = Counter(str1.lower().replace(" ",""))
    c2 = Counter(str2.lower().replace(" ",""))
    if c1 == c2:
        return True
    else:
        return False


def covers_alphabets(sentence):
    'checks if sentence includes at least one instance of every character in the alphabet using sets'

    sentence = ''.join(filter(str.isalnum, sentence)) 
    if set(sentence.lower().replace(" ","")) & set('abcdefghijklmnopqrstuvwxyz')== set('abcdefghijklmnopqrstuvwxyz'):
        return True
    else:
        return False


def book_index(words):
    'Words in ascending order with the page numbers they are present in ascending order'

    d =defaultdict(set)
    
    for k, v in words:
       
        d[k].add(v)
        
    return [[k,list(d[k])]for k in sorted(d.keys())]





class AngramCovAlBkIndxTest(unittest.TestCase):

    
    def test_anagram(self):
     
        self.assertTrue(anagram('cinema','iceman'))

        self.assertTrue(anagram('listen','silent'))

        self.assertTrue(anagram('dormitory','Dirty room'))

        self.assertFalse(anagram('AABB','bbaaw'))

    def test_anagram_dd(self):
      
        self.assertTrue(anagram_dd('cinema','iceman'))

        self.assertTrue(anagram_dd('listen','silent'))

        self.assertTrue(anagram_dd('dormitory','Dirty room'))

        self.assertFalse(anagram_dd('AABB','bbaaw'))

    def test_anagramcounter(self):
        
        self.assertTrue(anagram_counter('cinema','iceman'))

        self.assertTrue(anagram_counter('listen','silent'))

        self.assertTrue(anagram_counter('dormitory','Dirty room'))

        self.assertFalse(anagram_counter('AABB','bbaaw'))


    def test_covers_alpabets(self):
        
        self.assertTrue(covers_alphabets('abcdefghijklmnopqrstuvwxyz'))

        self.assertTrue(covers_alphabets('aabbcdefghijklmnopqrstuvwxyzzabc'))

        self.assertTrue(covers_alphabets('The quick brown fox jumps over the lazy dog'))

        self.assertTrue(covers_alphabets('We promptly judged antique ivory buckles for the next prize'))
        
        self.assertFalse(covers_alphabets('xyz'))

        self.assertTrue(covers_alphabets('The quick, brown, fox; jumps over the lazy dog!'))

    def test_bookindex(self):
        self.assertEqual(book_index([('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1),
                             ('woodchuck', 1), ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2),
                             ('could', 2), ('chuck', 1), ('wood', 1)]),[['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
                            ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]])

        self.assertEqual(book_index([('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)] ) ,[['word1', [1, 3]], ['word2', [2]]])
        
        self.assertEqual(book_index([('hi',1),('hi',7),('hi1',8)]),[['hi',[1,7]],['hi1',[8]]])

        self.assertNotEqual(book_index([('hi',1),('hi',7),('hi1',8)]),[['hi',[1,7,8]]])




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
