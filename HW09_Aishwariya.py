import os
from prettytable import PrettyTable
from collections import defaultdict
import unittest

def file_reader(path,expected,sep=',', header = False):
    'Reads the file safely'
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError("Not Found",path)
    else:

        with fp:
                
            for i,line in enumerate(fp):

                token = line.rstrip('\n').split(sep)
                if len(token)!= expected:
                    raise ValueError("{} has {} fields on line {} but expected {}".format(path,len(token),lines,expected))
                elif header and i == 0:
                    continue
                else:
                    yield tuple(token)

class Student:
    'Information about students'
    def __init__(self,cwid,name,major):
        self.cwid = cwid
        self.name = name
        self.major = major

        self.courses = dict()  

    def add_course(self,course,grade):
        self.courses[course]=grade

    def details(self):
        return [self.cwid,self.name,sorted(self.courses.keys())]

    @staticmethod
    def fields():
        return ['CWID','Name','Courses']


class Instructors:
    'Information about Instructors'

    def __init__ (self,cwid,name,dept):
        self.cwid = cwid
        self.name = name    
        self.dept = dept 

        self.courses = defaultdict(int) 

    def add_course(self,course):
        self.courses[course] += 1

    def details(self):

        for course,students in self.courses.items():
            yield [self.cwid,self.name,self.dept,course,students]

    @staticmethod
    def fields():
        return ['CWID','Name','Dept', 'Courses','Students']

class Repository:
    'Information about students, Intructors and grades in one place'

    def __init__(self,path):

        self.student= dict()
        self.instructors = dict()
        self.add_students(os.path.join(path,'students.txt'))
        self.add_instructors(os.path.join(path,'instructors.txt'))
        self.add_grades(os.path.join(path,'grades.txt'))
        self.student_pt()
        self.instructor_pt()
    


    def add_students(self,path):

        for cwid,name,major in file_reader(path,3,'\t',False):
            if cwid in self.student:
                continue
            else:
                self.student[cwid]=Student(cwid,name,major)

    
    def add_instructors(self,path):
        for cwid,name,dept in file_reader(path,3,'\t',False):
            if cwid in self.student:
                continue
            else:
                self.instructors[cwid]=Instructors(cwid,name,dept)

    def add_grades(self,path):
        for scwid,course,grades,icwid in file_reader(path,4,'\t',False):
            self.student[scwid].add_course(course,grades)
            self.instructors[icwid].add_course(course)

    def student_pt(self):
        pt= PrettyTable(field_names = Student.fields())

        for s in self.student.values():
            pt.add_row(s.details())
        print(pt)


    def instructor_pt(self):
        pt= PrettyTable(field_names = Instructors.fields())

        for i in self.instructors.values():
            for c in i.details():
                pt.add_row(c)
        print(pt)


def main():
    path = 'C:/Users/aishw/OneDrive - stevens.edu/SSW 810A'
    rep = Repository(path)

#main()


class RTest(unittest.TestCase):
    'Test Cases'
    

   
    def test(self):
        ins_val = []
        stu_val=[]
        rep = Repository('C:/Users/aishw/OneDrive - stevens.edu/SSW 810A')
        for s in rep.student.values():
            stu_val.append(s.details())
        
        for i in rep.instructors.values():
            for c in i.details():
                ins_val.append(c)

        expected_inst=[['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
            ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
            ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
            ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        expected_stu= [['10103','Baldwin, C',['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                    ['10115','Wyatt, X',['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    ['10172','Forbes, I',['SSW 555', 'SSW 567']],
                    ['10175','Erickson, D',['SSW 564', 'SSW 567', 'SSW 687']],
                    ['10183','Chapman, O',['SSW 689']],
                    ['11399','Cordova, I',['SSW 540']],
                    ['11461','Wright, U',['SYS 611', 'SYS 750', 'SYS 800']],
                    ['11658','Kelly, P',['SSW 540']],
                    ['11714','Morton, A',['SYS 611', 'SYS 645']],
                    ['11788','Fuller, E',['SSW 540']]]

        self.assertEqual(ins_val,expected_inst)
        self.assertEqual(stu_val,expected_stu)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)


