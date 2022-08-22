#================================================================
# single inheritance
#================================================================
''' 1. single inheritance '''
##class School:
##    class1='1st'
##    def show(self):
##        print("it is a govet high school")
##    @classmethod
##    def show1(cls):
##        print("it is a :",cls.class1)
##    @staticmethod
##    def show2():
##        print("it is also",School.class1)
##class Student(School):
##    def show3(self):
##        print("it is all student",School.class1)
##obj=Student()
##obj.show()
##obj.show1()
##obj.show2()
##        
##obj.show3()

''' 2. single inheritance constructor '''

##class Ojas:
##    def __init__(self):
##        self.salary=15000
##    def show(self):
##        print("it is Ojas emplayee")
##class Emplayee(Ojas):
##    def show1(self):
##        print("it is ojas employee salary is :",self.salary)
##obj=Emplayee()
##obj.show1()
##obj.show()

''' 3. single inheritance constructor with parameters '''

##class Ojas:
##    def __init__(self,sal,empname):
##        self.sal=sal
##        self.empname=empname
##    def disp(self):
##        print("it is Ojas")
##class Emp(Ojas):
##    def hello(self):
##        print("the emplayee name is ;",self.empname)
##        print("the salary is :",self.sal)
##
##obj=Emp(15000,'vadeppa')
##obj.hello()
##obj.disp()

''' 4. single inheritance constructor over riding '''

##class University:
##    def __init__(self):
##        self.sub="chemistry"
##    def show(self):
##        print("it is a :",self.sub,"student")
##class Collage(University):
##    def __init__(self):
##        self.sub="math"
##    def show1(self):
##        print("it ia a :",self.sub,"student")
##obj=Collage()
##print(obj.sub)
##
##obj.show()
##
##obj.show1()

''' 5.  single inheritance constructor over riding with parameters '''

##class University:
##    def __init__(self,s,p):
##        self.marks=s
##        self.persantage=p
##    def show(self):
##        print("it is a :",self.marks,self.persantage,"student")
##class Collage(University):
##    def __init__(self,m,p):
##        self.marks=m
##        self.persantage=p
##    def show1(self):
##        print("it ia a :",self.marks,self.persantage,"student")
##obj=Collage(79,7.5)
##obj.show1()

'''6. single inheritance Constructor with Super Method '''

##class Father:
##    def __init__(self):
##        self.salary=15000
##    def show(self):
##        print("it is father salary:",self.salary)
##class Son(Father):
##    def __init__(self):
##        super().__init__()
##    def show1(self):
##        print("it is a son of salary:",self.salary)
##obj=Son()
##obj.show1()

'''7. single inheritance Constructor  Super Method with parameters '''

##class Father:
##    def __init__(self,s,n):
##        self.salary=s
##        self.name=n
##    def show(self):
##        print("it is father salary:",self.salary)
##        print("it is father salary:",self.name)
##
##class Son(Father):
##    def __init__(self,s,n):
##        self.salary=s
##        self.name=n
##        super().__init__(s,n)
##    def show1(self):
##        print("it is a son of salary:",self.salary)
##        print("it is son of salary:",self.name)
##obj=Son(25000,'vadeppa')
##obj.show1()

#=================================================================================
# maltilevel inheritance
#=================================================================================

''' 1. maltilevel inheritance '''
##
##class Father:
##	
##	def showF(self):
##		print("Father Class Method")
##		
##class Son(Father):
##	
##	def showS(self):
##		print("Son Class Method")
##		
##class GrandSon(Son):
##	
##	def showG(self):
##		print("GrandSon Class Method")
##		
##g = GrandSon()
##g.showF()
##g.showS()
##g.showG()

''' 2. maltilevel inheritance with constructur '''
##
##class University:
##    def __init__(self):
##        print("it is university")
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    def __init__(self):
##        print("it is collage ")
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    def __init__(self):
##        print("it is student ")
##    def show2(self):
##        print("it is student method")
##obj=Student()
##obj.show()
##obj.show1()
##obj.show2()

''' 3. maltilevel inheritance  constructur with parametrs '''

##class University:
##    def __init__(self,name):
##        self.name=name   
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    
##    def show2(self):
##        print("the student name is ",self.name)
##       
##obj=Student('vadeppa')
##
##obj.show2()

''' 4. multi_leve inheritance constructor over riding '''

##
##class University:
##    def __init__(self):
##        self.name="vadeppa"  
##    def show(self):
##        print("it is university method",self.name)
##class Collage(University):
##    def __init__(self):
##        self.name="rakesh"
##    def show1(self):
##        print("it is collage method",self.name)
##class Student(Collage):
##    def __init__(self):
##        self.name="Tharak"
##    def show2(self):
##        print("the student name is ",self.name)
##      
##
##obj=Student()
##
##obj.show2()
##
''' 5.  multi_level inheritance constructor over riding with parameters '''


##class University:
##    def __init__(self,name):
##        self.name=name
##       
##        
##    def show(self):
##        print("it is university method")
##class Collage(University):
##    def __init__(self,sal):
##        self.sal=sal
##
##    def show1(self):
##        print("it is collage method")
##class Student(Collage):
##    def __init__(self,idno,name,sal):
##        self.idno=idno
##        self.name=name
##        self.sal=sal
##    def show2(self):
##        
##        print("the student job is ",self.idno)
##        print("the student name is ",self.name)
##        print("the student sal is ",self.sal)
##
##
##obj=Student(22070,'vadeppa',25000)
##
##obj.show2()
##


'''6.multi_level inheritance Constructor with Super Method '''

##
##class GrandFather:
##    def __init__(self):
##        self.surename="vadeppa"
##    def show(self):
##        print("it is grand father method",self.surename)
##class Father(GrandFather):
##    def __init__(self):
##        super().__init__()
##        
##    def show2(self):
##        print("the surename is ",self.surename)
##        
##      
##class Son(Father):
##    def __init__(self):
##   
## 
##        super().__init__()
##        
##    def show3(self):
##        print("it is sure name is ",self.surename)
##       
##obj=Son()
##obj.show3()
##obj.show2()
##


'''7. multi_level inheritance Constructor  Super Method with parameters '''
##class GrandFather:
##    def __init__(self, surename):
##        self.surename=surename
##    def show(self):
##        print("it is grand father method",self.surename)
##class Father(GrandFather):
##    def __init__(self,surename,car):
##        super().__init__(surename)
##        self.car=car
##    def show2(self):
##        print("the surename is ",self.surename)
##        
##        print("the surename is ",self.car)
##class Son(Father):
##    def __init__(self,surename,car,hit):
##        #super().__init__(surename,car)
##        self.hit=hit
##        super().__init__(surename,car)
##        
##    def show3(self):
##        print("it is sure name is ",self.surename)
##        print("it is car name is ",self.car)
##        print("it is hit name is ",self.hit)
##
##obj=Son("Ambani","BMW",12)
##obj.show3()
##obj.show2()

#===============================================================
## Hierarchical Inheritance
#===============================================================
'''1. Hierarchical Inheritance '''

##class Father:
##	
##	def showF(self):
##		print("Father Class Method")
##class Son(Father):
##	
##	def showS(self):
##		print("Son Class Method")
##		
##class Daughter(Father):
##	
##	def showD(self):
##		print("Daughter Class Method")
##		
##d = Daughter()
##d.showF()
##d.showD()
##s = Son()
##s.showF()
##s.showS()


''' 2. hierarchical inheritance with constructur '''

##class Father:
##	def __init__(self):
##		print("Father Class Constructor")
##	def showF(self):
##		print("Father Class Method")
##class Son(Father):
##	def __init__(self):
##		print("Son Class Constructor")
##	def showS(self):
##		print("Son Class Method")
##		
##class Daughter(Father):
##	def __init__(self):
##		print("Daughter Class Constructor")
##	def showD(self):
##		print("Daughter Class Method")
##		
##d = Daughter()
##d.showF()
##d.showD()
##s = Son()
##s.showF()
##s.showS()
##
##
'''3. hierarchical inheritance with constructur with parameters '''

##
##class Father:
##    def __init__(self,surname):
##        self.surname=surname
##    def showF(self):
##        print("Father surname is",self.surname)
##class Son(Father):
##   
##    def showS(self):
##        print("Son surname is ",self.surname)
##		
##class Daughter(Father):
##   
##    def showD(self):
##        print("Daughter surname is",self.surname)
##		
##d = Daughter("chakali")
##d1=Son("chakali")
##d.showF()
##d.showD()
##d1.showS()
##
'''4. hierarchical inheritance with constructur over riding '''
                          

##
##class Father:
##    def __init__(self):
##        
##        self.surname="chakali"
##    def showF(self):
##        print("Father surname is",self.surname)
##class Son(Father):
##    def __init__(self):
##        self.surname="madiwal"
##   
##    def showS(self):
##        print("Son surname is ",self.surname)
##		
##class Daughter(Father):
##    def __init__(self):
##        self.surname="mallula"
##   
##    def showD(self):
##        print("Daughter surname is",self.surname)
##		
##d = Daughter()
##d1=Son()
##d1.showF()
##d.showF()
##d.showD()
##d1.showS()
##


''' 5.  hierarchical inheritance constructor over riding with parameters '''

##
##class Father:
##    def __init__(self,n):
##        
##        self.age=n
##    def showF(self):
##        print("Father name is  is",self.age)
##class Son(Father):
##    def __init__(self,m):
##        self.age=m
##   
##    def showS(self):
##        print("Son age is ",self.age)
##		
##class Daughter(Father):
##    def __init__(self,s,m):
##        self.name=s
##        self.age=m
##        self.car="bmw"
##   
##    def showD(self):
##        print("Daughter name is",self.name)
##        print("the car name is:",self.car)
##        print("the daughter is :",self.age)
##		
##d = Daughter("harini",12)
##print(d.age)
##d.showD()
##d1=Son(25)
##print(d1.age)
##d1.showS()


'''6.hierarchical inheritance Constructor with Super Method '''

##class Father:
##    def __init__(self):
##        self.surname="chakali"
##    def showF(self):
##        print("Father surname",self.surname)
##class Son(Father):
##    def __init__(self):
##        super().__init__()
##        
##    def showS(self):
##        print("Son surname",self.surname)
##		
##class Daughter(Father):
##    def __init__(self):
##        super().__init__()
##    def showD(self):
##        print("Daughter surname",self.surname)
##		
##d = Daughter()
##d.showF()
##d.showD()
##d1 = Son()
##d1.showF()
##d1.showS()
'''7.hierarchical inheritance Constructor with Super Method  with parameters'''

##
##class Father:
##    def __init__(self,surname):
##        self.surname=surname
##    def showF(self):
##        print("Father surname",self.surname)
##class Son(Father):
##    def __init__(self,surname,age):
##        super().__init__(surname)
##        self.age=age
##        
##    def showS(self):
##        print("Son surname",self.surname)
##        print("is age ia", self.age)
##		
##class Daughter(Father):
##    def __init__(self,surname,age):
##        super().__init__(surname)
##        self.age=age
##    def showD(self):
##        print("Daughter surname",self.surname)
##        print("the doughter age is ",self.age)
##		
##d = Daughter("chakali",19)
##d.showF()
##d.showD()
##d1 = Son("ckakali",25)
##d1.showF()
##d1.showS()
## 
#=====================================================
#multiple inheritance
#=====================================================
'''1. multipul inheritance'''
##class Father:
##    def Driving(self):
##        print("Father Enjoys Driving")
##class Mother:
##    def Cooking(self):
##        print("Mother Enjoys Cooking")
##class Child(Father, Mother):
##    def Playing(self):
##        print("Child Loves Playing")
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()
''' 2. multipul inheritance with constructor'''

##class Father:
##    def __init__(self):
##        self.salary=25000
##    def Driving(self):
##        print("Father Enjoys Driving")
##class Mother:
##    def __init__(self):
##        self.salary=30000
##    def Cooking(self):
##        print("Mother Enjoys Cooking")
##class Child(Father,Mother):
##    def Playing(self):
##        print("Child Loves Playing",self.salary)
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()
##

''' 3. multipul inheritance with constructor with parameters'''


##class Father:
##    def __init__(self,age):
##        self.age=age
##    def Driving(self):
##        print("Father age is")
##class Mother:
##    def __init__(self,weight):
##        self.weight=weight
##    def Cooking(self):
##        print("Mother Enjoys Cooking")
##class Child(Mother,Father):
##    def Playing(self):
##        print("the children wight is",self.weight)
##c = Child(65)
##c.Driving()
##c.Cooking()
##c.Playing()
##

''' 4. multipul inheritance with constructor ovr riding'''

##class Father:
##    def __init__(self):
##        self.age='56'
##    def Driving(self):
##        print("Father age is")
##class Mother:
##    def __init__(self):
##        self.age='45'
##    def Cooking(self):
##        print("Mother age is")
##class Child(Mother,Father):
##    def __init__(self):
##        self.age='20'
##    def Playing(self):
##        print("the children age is is",self.age)
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()

''' 5. multipul inheritance with constructor ovr riding parameters'''

##class Father:
##    def __init__(self,m):
##        self.age=3542
##    def Driving(self):
##        print("Father age is")
##class Mother:
##    def __init__(self,n):
##        self.age=52
##    def Cooking(self):
##        print("Mother age is")
##class Child(Mother,Father):
##    def __init__(self):
##        self.age=12
##        self.car='benz'
##    def Playing(self):
##        print("the children age is is",self.age)
##        print("the car is ",self.car)
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()

''' 6. multipul inheritance with constructor super method'''

##class Father:
##    def __init__(self):
##        print("the father class constructor")
##    def Driving(self):
##        print("Father method is")
##class Mother:
##    def __init__(self):
##        print("the mother class constrotur")
##    def Cooking(self):
##        print(" it is Mother method")
##class Child(Father,Mother):
##    def __init__(self):
##        
##        super().__init__()
##    def Playing(self):
##        print("the children  methodis")
##        
##c = Child()
##c.Driving()
##c.Cooking()
##c.Playing()


''' 7. multipul inheritance with constructor super
method wirh parameters'''

##class Father:
##    def __init__(self,m):
##        self.money=m
##        print("the father class constructor")
##    def Driving(self):
##        print("Father money is",self.money)
##class Mother:
##    def __init__(self,n):
##        self.name=n
##        print("the mother class constrotur")
##    def Cooking(self):
##        print(" it is Mother name is",self.name)
##class Child(Father,Mother):
##    def __init__(self,m,k):
##        self.fees=k
##        
##        
##        super().__init__(m)
##    def Playing(self):
##        print("the children  methodis",self.fees)
        
##c = Child(2500,1200)
##c.Driving()
##c.Cooking()
##c.Playing()


##'super in multiple inheritance'
##
##class Parent:
##    def __init__(self):
##        print("This is")
##        
##class Parent1:
##    def __init__(self):
##        print("This is the parent1 class")
##        
##class Child(Parent, Parent1):
##    def __init__(self):
##        ##Calling constructor of the Parent 1 class
##       super(Parent, self).__init__()
##       
##ob = Child()






        
        




















