import os
from prettytable import PrettyTable
from collections import defaultdict
import unittest
import sqlite3

def file_reader(path,expected,sep=',', header = False):
    'Reads the file safely'
    try:
        fp = open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError("Not Found",path)
    else:

        with fp:
            lines=0  
            for i,line in enumerate(fp):
                lines+=1
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
        
        self.required = set()
        self.electives = set()

        self.completed_courses = dict()  

    def add_course(self,course,grade):
        grades = ['A','A-','A+','B','B+','B-','C','C+']
        if grade in grades:
            self.completed_courses[course]=grade

    def details(self):
        if self.required is None:
            self.required = set()
        if self.electives is None:
            self.electives = set()
        return [self.cwid,self.name,self.major,sorted(self.completed_courses.keys()),sorted(self.required),sorted(self.electives)]

    @staticmethod
    def fields():
        return ['CWID','Name','Major','Completed courses','Remaining Required','Remaining Electives']


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
        self.majors = defaultdict(Major)
        self.add_students(os.path.join(path,'students.txt'))
        self.add_instructors(os.path.join(path,'instructors.txt'))
        self.add_grades(os.path.join(path,'grades.txt'))
        self.add_majors(os.path.join(path,'majors.txt'))
        self.major_pt()
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
            if cwid in self.instructors:
                continue
            else:
                self.instructors[cwid]=Instructors(cwid,name,dept)

    def add_grades(self,path):
        for scwid,course,grades,icwid in file_reader(path,4,'\t',False):

            self.student[scwid].add_course(course,grades)
            self.instructors[icwid].add_course(course)


    def add_majors(self,path):
        for dept,flag,course in file_reader(path,3,'\t',False):
            self.majors[dept].dept = dept
            if flag == 'R':
                self.majors[dept].required.add(course)
            elif flag == 'E':
                self.majors[dept].electives.add(course)

            

    def student_pt(self):
        pt= PrettyTable(field_names = Student.fields())

        print("Student Summary")

        for s in self.student.values():
            pt.add_row(s.details())
        print(pt)


    def instructor_pt(self):
       

        pt= PrettyTable(field_names = Instructors.fields())

        print("Instructor Summary")

        for i in self.instructors.values():
            for c in i.details():
                pt.add_row(c)
        print(pt)
    
        


    def major_pt(self):
        pt = PrettyTable(field_names=Major.fields())
        print("Major Summary")
        for student in self.student.values():
            student.required = self.majors[student.major].required.difference(set(student.completed_courses.keys()))
            

            if len(student.required) == 0:
                student.required = None
            if self.majors[student.major].electives & set(student.completed_courses.keys()):
                student.electives = None
            else: 
                student.electives = self.majors[student.major].electives

        for major in self.majors.values():
            
            pt.add_row([major.dept, major.required, major.electives])
        print(pt)

class Major:
  

    def __init__(self):
        self.dept = set()
        self.required = set()
        self.electives = set()

    @staticmethod
    def fields():
        return ["Dept", "Required", "Electives"]


def main():
    path = 'C:/Users/aishw/OneDrive - stevens.edu/SSW 810A'
    rep = Repository(path)

#main()

class RTest(unittest.TestCase):
    'Test Cases'
    

   
    def test(self):
        self.maxDiff = None
        ins_val = []
        maj = []
        stu = []

        rep = Repository('C:/Users/aishw/OneDrive - stevens.edu/SSW 810A')

      
        for major in rep.majors.values():
            maj.append([major.dept, major.required, major.electives])

        for s in rep.student.values():
            stu.append(s.details())

        for i in rep.instructors.values():
            for c in i.details():
                ins_val.append(c)
        

          

        expected_inst=[['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
            ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
            ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
            ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
            ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        expected_maj = [['SFEN',{'SSW 540','SSW 564','SSW 567','SSW 555'},{'CS 545','CS 501','CS 513'}],['SYEN',{'SYS 671', 'SYS 800', 'SYS 612'},{'SSW 540', 'SSW 810', 'SSW 565'}]]

        expected_stu = [['10103', 'Baldwin, C','SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], []],

                        ['10115', 'Wyatt, X', 'SFEN',['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], []],

                        ['10172', 'Forbes, I', 'SFEN',['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545']],

                        ['10175', 'Erickson, D', 'SFEN',['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513','CS 545']],

                        ['10183', 'Chapman, O', 'SFEN',['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],

                        ['11399', 'Cordova, I', 'SYEN',['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], []],

                        ['11461', 'Wright, U', 'SYEN',['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810']],

                        ['11658', 'Kelly, P', 'SYEN',[], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']],

                        ['11714', 'Morton, A', 'SYEN',['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']],

                        ['11788', 'Fuller, E', 'SYEN',['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], []]]



        self.assertEqual(maj,expected_maj)
        self.assertEqual(stu,expected_stu)
        self.assertEqual(ins_val,expected_inst)

      

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

