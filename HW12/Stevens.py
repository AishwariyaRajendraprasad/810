from flask import Flask, render_template
import sqlite3
app = Flask(__name__)



@app.route('/students_instructors')
def students_instructors():

    
    DB_file = 'C:/Users/aishw/810_start.db'


    Query = """select CWID,Name, Dept,Course,count(Student_CWID) as cnt
        from HW11_instructors
        left join HW11_grades
        on CWID = Instructor_CWID
        group by Name, CWID, Dept, Course
        order by cnt desc
    """
    db = sqlite3.connect(DB_file)
    results = db.execute(Query)

    data = [{'cwid':cwid , 'name': name, 'dept' : dept, 'course': course, 'cnt':cnt}
            for cwid,name,dept,course,cnt in results]

    db.close()

    return render_template('student_instructors.html',
                           title = 'Stevens Repository',
                           table_title = 'Number of students in the course',
                           instructors=data)

    
app.run(debug=True)