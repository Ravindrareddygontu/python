'1. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'
##a = 'abcdefghijklmnopqrstuvwxyz'
##with open('alpha.txt','w') as f:
##    for i in range(24):
##        f.write(f'{a[i:]},{len(a)}\n')



'2.Write a Python program to combine each line from first file with the corresponding line in second file.'
##with open('first.txt','r') as f:
##    with open('second.txt','r') as t:
##        for i in f.readlines():
##            for j in t.readlines():
##                print(i+j)
##


'''3.Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class.
Create a function to display the entire 
attribute and their values in Student class.'''
##class Student:
##    
##    def display(self):
##        self.student_id = 22060
##        self.student_name = 'ravindra'
##
##        for i in self.__dict__:
##            print(i)
##           
##            
##obj = Student()
##obj.age = 35
##
##obj.display()
##print(obj.__dict__)



'''4. Write a Python program to convert an array to an ordinary list with the same items. 
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Convert the said array to an ordinary list with the same items:
[1, 3, 5, 3, 7, 1, 9, 3]'''
##from array import array
##arr = array('i',[1,3,5,3,7,1,9,3])
##print(list(arr))



'5. Write a Python program to print yestarday date,day before yestarday and next 5 days starting from today.'
##from datetime import date,timedelta
##t = date.today()
##y = t.strftime('%d')
##for i in range(5):
##    t = t-timedelta(1)
##    print(t)
