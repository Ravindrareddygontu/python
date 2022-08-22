'1.WAP to call parent class static static method from child class static method.'
##class Parent:
##    def func():
##        print('this is Parent class')
##
##class Child(Parent):
##    def foo():
##        Parent.func()
##
##obj = Child.foo()


'2.write demo programs for method overriding,constructor overriding,program with variable number of arguments.'
##class Parent():
##    def __init__(self,name):
##        self.value = "Inside Parent"
##          
##    def show(self):
##        print(self.value)
##
##class Child(Parent):
##    def __init__(self):
##        self.value = "Inside Child"
##    
##    def show(self):
##        print(self.value)
##          
##obj1 = Parent()
##obj2 = Child()
##  
##obj1.show()
##obj2.show()


'3.create one object for child class and using that object print both constructor print statemts from parent classes.'
##class Parent:
##    def __init__(self):
##        print('parent class')
##
##class Parent1(Parent):
##   
##        print('parent2 class')
##
##class Child(Parent1):
##    pass
##    
##obj = Child()



'''4.wap that take a two two strings from input and return the combination of the two string characters like below:
input:
string1="harry"
string2="micheal"
output:
['hm','ai','rc','rh','ae','ya','l']'''
##string = 'harry'
##string2 = 'micheal'
##dic = list(zip(string,string2))
##mylist = []
##for i in dic:
##    s = ''.join(i)
##    mylist.append(s)
##print(mylist)
  

'''5.wap to take a list and sort the list not using the sorted or sort() method
input:  [2,5,12,6,1,4]
output:   [1,2,4,5,6,12]
and not using max() or min() method'''
##mylist = [5,2,45,24,457,234,32,16,5,26]
##n =1
##while n:
##    count = 0
##    for i in range(1,len(mylist)):
##        if mylist[i-1]>mylist[i]:
##            mylist[i-1],mylist[i] = mylist[i],mylist[i-1]
##            mylist
##            count += 1
##    
##    if count == 0:
##        print(mylist)
##        n = 0














