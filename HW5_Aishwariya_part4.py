import unittest
def get_lines(path):

    try:
        fp = open(path,'r')
    except FileNotFoundError:
        print("Can't open",file_name)
    else:

        for line in fp:
            line = line.rstrip('\n')
            while line.endswith('\\'):
                line = line[:-1] + next(fp).rstrip('\n')
           
            line = line.partition('#')[0]
            if line != "":
                yield line
        
file_name = 'C:/Users/aishw/Desktop/810/readme.txt'     
  
for line in get_lines(file_name):
    print(line)
class GetLinesTest(unittest.TestCase):
    def test_get_lines(self):
        file_name = 'C:/Users/aishw/Desktop/810/readme.txt' 

        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertTrue(result==expect)
           
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)