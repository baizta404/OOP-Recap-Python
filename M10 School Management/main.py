from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school  = School('HJ Pilot',"14 GRAM")
eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student('Rahim',eight)
karim = Student('Karim',nine)
nahid = Student('Nahid',ten)
hamim = Student('Hamim',ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(nahid)
school.student_admission(hamim)


abul = Teacher('Abul Bhai')
mizan = Teacher('Mizan')
nuru = Teacher('Nuru')
kuddus = Teacher('Kuddus')

bangla = Subject('Bangla',abul)
math = Subject('Math',nuru)
chemistry = Subject('Chemistry',kuddus)
english = Subject('English',mizan)

eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(english)

nine.add_subject(bangla)
nine.add_subject(math)
nine.add_subject(english)
nine.add_subject(chemistry)

ten.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(english)
ten.add_subject(chemistry)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)

