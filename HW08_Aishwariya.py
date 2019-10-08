import os
import glob
import sys
import unittest
from prettytable import PrettyTable
import datetime

def dtime():
    "1.1 What is the date three days after Feb 27, 2000?"

    "1.2 What is the date three days after Feb 27, 2017?"

    "1.3 How many days passed between Jan 1, 2017 and Oct 31, 2017?"




    date1 = "Feb 27 2000"
    date2 = "Feb 27 2017"
    date3 = "Jan 1 2017"
    date4 = "Oct 31 2017"

    dt1 = datetime.datetime.strptime(date1,"%b %d %Y")
    dt2 = datetime.datetime.strptime(date2,"%b %d %Y")
    dt3 = datetime.datetime.strptime(date3,"%b %d %Y")
    dt4 = datetime.datetime.strptime(date4,"%b %d %Y")

    dt1_str = dt1.strftime('%m/%d/%Y')
    dt2_str = dt2.strftime('%m/%d/%Y')
    dt3_str = dt3.strftime('%m/%d/%Y')
    dt4_str = dt4.strftime('%m/%d/%Y')

    num_days = 3
    dt5 = dt1 + datetime.timedelta(days=num_days)
    print('{} days after {} is {}'.format(num_days,dt1_str,dt5.strftime('%m/%d/%Y')))

    dt6 = dt2 + datetime.timedelta(days=num_days)
    print('{} days after {} is {}'.format(num_days,dt2_str,dt6.strftime('%m/%d/%Y')))



    delta = dt4 - dt3
    print('{} days passed between {} and {}'.format(delta.days,dt3_str,dt4_str))

dtime()


def mycsv(dir,sep=',',expected=0, header = False):
    'Reads data with some seperator and returns us each line after removing the seperator'
   
    try:
        fp = open(dir,'r')
    except FileNotFoundError:
        print("Can't open",dir)
    else:
 
        with fp:
            lines=0
            if header== True:
                next(fp)         
            
            for line in fp:
                lines+=1
                line = line.strip()
                token = line.split(sep)
                if len(token)!= expected:
                    raise ValueError("{} has {} fields on line {} but expected {}".format(dir,len(token),lines,expected))
                else:
                    yield tuple(token)

mycsv(dir, expected=3, sep=',', header=True)


class mycsvTest(unittest.TestCase):
    def test(self):
 
        dir = "C:/Users/aishw/Desktop/810/arrw.txt"
 
        with self.assertRaises(ValueError) as context:
            list(mycsv(dir, expected=3, sep=',', header=True))

        self.assertEqual(str(context.exception), "C:/Users/aishw/Desktop/810/arrw.txt has 2 fields on line 2 but expected 3")
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)



def files(dir):
    'Returns the name of files, counts classes, charaters, lines and functions'
   
    results = dict()

    if os.path.exists(dir)==False:
        raise FileNotFoundError("Please enter a valid directory")

    
    for file in glob.glob(f"{dir}/**/*.py",recursive=True):
        with open(file) as infile:
            lines=0
            characters=0
            countClass=0
            countFunc=0
            for line in infile:
                
                lines+=1
                characters+= len(line)
                line = line.strip()
                if line.startswith("class "):
                   
                    countClass+=1
                if line.startswith("def "):
                    
                    countFunc+=1

    
        results[file] = [file, lines, characters,countClass,countFunc]

    return results

def pt(dir):

    x = PrettyTable()


    x.field_names = ["Files", "Lines", "Charaters", "Classes", "Function"]
 
    
    results = files(dir)   # returns a dict[file] = [file, lines, characters,countClass,countFunc]

    for file in results:
        x.add_row(results[file])

    print(x)


