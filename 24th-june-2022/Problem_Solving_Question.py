'''1)Write a Python program whic will accept  Student name,class and subject marks .
It will show the students total marks , percentage ,
which grade the student secured(Percentage>90: Grade=O,Percentage>80:Grade=E like
this u have to calculate and if the student is fail it will show Grade=F) and also
check the student pass or Fail.
If the student is fail in one subject then it will show fail.
If the subject mark is less than 35 then it will show fail and if the percentage is
less than 40 then it will show Grade=F.

Student Name:Rakesh Kumar Sahoo
Student Studying in :X
----------------------------------------
	Subjects	Marks
----------------------------------------
	Eng		67
	Tel		66
	Sci		88
	maths		99
	soc		88
----------------------------------------
	Total Marks=408
	Percentage=81.6
	Status=Pass
	Grade=E
'''
student=input("Student Name: ")
class1=input("Student Studying in:")
print("----------------------------")
print('''Subjects      Marks''')
print("----------------------------")
english=int(input("English    :"))
telugu=int(input("Telugu      :"))
science=int(input("Science    :"))
maths=int(input("Maths        :"))
social=int(input("Social      :"))
print("----------------------------")
total=english+telugu+science+maths+science+social
percentage=total/5
if english < 35 or telugu < 35 or science < 35 or maths < 35 or social < 35:
    print("Fail")
elif percentage>=90:
    print(f"Total Marks={total}")
    print(f"Percentage={percentage}")
    print("status=PASS")
    print("Grade=A+")
elif percentage>=70 and percentage<90:
    print(f"Total Marks={total}")
    print(f"Percentage={percentage}")
    print("status=PASS")
    print("Grade=A")    
elif percentage>=60 and percentage<70:
    print(f"Total Marks={total}")
    print(f"Percentage={percentage}")
    print("status=PASS")
    print("Grade=B")
elif percentage>=35 and percentage<60:
    print(f"Total Marks={total}")
    print(f"Percentage={percentage}")
    print("status=PASS")
    print("Grade=C")
