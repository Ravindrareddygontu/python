'''Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes.
Print all the attributes of student1, student2 instances with their values in the given format.

Input values of the instances:
student_1:
student_id = "V12"
student_name = "Ernesto Mendez"
student_2:
student_id = "V12"
marks_language = 85
marks_science = 93
marks_math = 95
Expected Output:
student_id -> V12
student_name -> Ernesto Mendez
student_id -> V12
marks_language -> 85
marks_science -> 93
marks_math -> 95'''
class Student:
     def __init__(self, s_id, name, science, math, english):
         self.s_id = s_id
         self.name = name
         self.science = science
         self.math = math
         self.english = english

     def details(self):
        print(self.s_id, self.name, self.science, self.math, self.english)

student1 = Student(220,'ravindra',34,35,36)
student2 = Student(660,'reddy',45,46,49)
student1.details()
student2.details()
