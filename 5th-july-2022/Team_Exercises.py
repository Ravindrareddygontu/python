'1.write a python program using oops concept finding prime number or not'
##class Prime:
##    def foo(self,num):
##        for i in range(2,num):
##            if num%i == 0:
##                print('it is not prime')
##                break
##        else:
##            print('it is prime')
##number = int(input('>:'))
##obj = Prime()
##obj.foo(number)


'2.write a program on instance method, static method, class method using some examples'
##class Student:
##    org = 'ojas'
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age
##        
##    def foo(cls):
##        print(cls.name)
##        print(cls.org)
##
##    def fun(self):
##        print(self.age)
##    
##    def static():
##        print('this is static method')
##       
##obj = Student('sindu',23)
##obj.foo()
##obj.fun()
##obj = Student.static()


'3.write a program on single inheritance'
##class Parent:
##    def __init__(self, surname, village):
##        self.surname = surname
##        self.village = village
##
##class Child(Parent):
##    def foo(self):
##        print(self.surname, self.village)
##
##obj = Child('mamidala', 'giddalur')
##obj.foo()
        

'4.write a python program using oops concepts find a fibonacci series'
##class Series:
##    def fib(self,num):
##        a = 0
##        b = 1
##        print(a,b,end=' ')
##        for i in range(num):
##            c = a+b
##            a = b
##            b = c
##            print(c,end=' ')
##num = 8
##obj = Series()
##obj.fib(num)


'5.write a python program using oops concepts find armstrong number'
##class Number:
##    def armstrong(self,num):
##        count = 0
##        temp = num
##        while temp>0:
##            div = temp%10
##            count += 1
##            temp = temp//10
##        arm = num
##        cube = 0
##        while arm>0:
##            mod = arm%10
##            cube = cube+mod**count
##            arm = arm//10
##        if cube==num:
##            print('armstrong number')
##        else:
##            print('not an armstrong number')
##
##num = int(input('>:'))
##obj = Number()
##obj.armstrong(num)









            




















