from person import Teacher
from school import School
class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.mx_marks =100
        self.pass_marks = 33
    
    def exam(self,students): #students er list dimu
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name]= mark
            student.subject_grade[self.name]= School.calculate_grade(mark)