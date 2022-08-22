'''1).Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''

##lst = ['0100','0011','1010','1001']
##a = '0100'
##
##for a in lst:
##    b = 0
##    c = 0
##    for i in reversed(a):
##        if i=='1':
##            b = b+2**c
##        c+=1
##    if b%5==0:
##        print(a)

##for i in lst:
##    if int(i,2)%5==0:
##        print(i)





'''2).Write a menu driven program which shows all operations on Binary File 

Add Record 

Display All Record 

Display Specific Record 

Modify Record 

Delete Record 

Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type'''
##class Binary:
##    def __init__(self,lst):
##        self.lst = lst
##
##    def display(self):
##        with open('mobile.dat','r') as f:
##            print(f.read())
##
##    def specific(self,n):
##        with open('mobile.dat','r') as f:
##            lst = f.read.split('\n')
##            for i in lst:
##                lst2 = i.split(',')
##                if lst2[2]==n:
##                    print(lst)
##
##    def modify(self,price):
##        with open('mobile.dat','a') as f:
##            lst = f.read.split('\n')
##            for i in lst:
##                lst2 = i.split(',')
##                lst2[3] == price
##                
##    def delete(self,item):
##        with open('mobile.dat','r') as f:
##            lst = f.read.split('\n')
##            for i in lst:
##                lst2 = i.split(',')
##                lst2[i] == item:
##                    del lst2
##
##lst = [401,6000,'4 sharing']
##obj = Binary()
##                
    


'''3).Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat”
whoose model number (integer type) is passed as an argument.
Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price]'''

##mobileid = [220,224,112,445,667]
##mobilebrand = ['nokia','samsung','moto','windows','mi']
##modelno = [1,2,3,4,5]
##price = [100,200,300,2000,4500]
##with open('mobile.dat','w') as f:
##    for i in range(5):
##        lst = f'{mobileid[i]},{mobilebrand[i]},{modelno[i]},{price[i]}\n'
##        f.write(lst)
##        
##def foo(n):
##    with open('mobile.dat','r') as f:
##        for i in f.readlines():
##            lst = i.split(',')
##            if lst[2]==n:
##                print(lst)
##
##foo('5')



'''4).Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and
the values are square of keys.'''
##def foo(n):
##    dic = dict()
##    for i in range(n):
##        dic[i]=i**2
##    print(dic)
##
##foo(4)



'''5).Please write a program using generator to print the numbers which can be
divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100
Then, the output of the program should be:

0,35,70'''

##def gen(n):
##    for i in range(n):
##        if i%5==0 and i%7==0:
##            yield(i)
##
##for i in gen(100):
##    print(i)












