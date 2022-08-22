'Create a Class with instance attributes'
##class Cls:
##    def __init__(self, name , age):
##        self.name = name
##        self.age = age
##        
##    def foo(self):
##        print(self.name, self.age)
##
##s = Cls('ravi',23)
##s.foo()



'Write a Program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.'
##class Students:
##    def __init__(self, name, age, grade):
##        self.age = age
##        self.name = name
##        self.grade = grade
##    def foo(self):
##        print(self.name,self.age,self.grade)
##
##n = Students('rdeeg',34,'C')
##n.foo()


'Write a Program to create an empty valid class by name Students, with no properties '
##class Students:
##    pass
##
##empty = Students()


'Write a program that prints the class name using its object.'
##class Student:
##    pass
##obj = Student()
##print(type(obj))


'Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff'
##class Parent:
##    def __init__(self,surname,address):
##        self.surname = surname
##        self.address = address
##        
##class Child(Parent):
##    def foo(self):
##        print(self.surname)
##        print(self.address)
##        
##obj = Child('sindhu',6776)
##obj.foo()

        

'Create a Vehicle class without any variables and methods '
##class Vehicle:
##    pass
##
##obj = Vehicle()


'Create a child class Bus that will inherit all of the variables and methods of the Vehicle class'
##class Vehicle:
##    def __init__(self, tires, city, driver):
##        self.tires = tires
##        self.city = city
##        self.driver = driver
##    def foo(self):
##        print(self.tires, self.city, self.driver)
##
##class Bus(Vehicle):
##    print('vehicle class inherited')
##
##obj = Bus(4, 'hyderabad', 'sourav')
##Bus.foo(obj)


'Define a property that must have the same value for every class instance (object)'
##class Cls:
##    org = 'ojas'
##   
##
##obj = Cls()
##obj2 = Cls()
##print(obj.org)
##print(obj2.org)


'Check type of an object '
##class Member:
##    pass
##
##obj = Member()
##print(type(obj))


'Write a Python program that checks if one class is a subclass of another?' 
##class Parent:
##    def __init__(self, name):
##        self.name = name
##
##class Child(Parent):
##   pass
##print(issubclass(Child,Parent))



'Determine if School_bus is also an instance of the Vehicle class '
##class Vehicle:
##    pass
##
##schoolbus = Vehicle()
##print(isinstance(schoolbus,Vehicle))

 















