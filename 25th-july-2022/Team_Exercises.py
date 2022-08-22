'1) wap to create class and create two objects from that class and add those two objects using _add_ (operator overloading)'
##class Add:
##    def __new__(cls,a):
##        print('new method is called')
##        return super().__new__(cls)
##        
##    def __init__(self,a):
##        self.a = a
##        print('this is init method')
##
##    def __add__(self,other):
##        print(self.a + other.a)
##
##    def __call__(self):
##        return('this class is called')
##
##    def __str__(self):
##       return 'this is string'
##
##    def __repr__(self):
##        print( 'this is repr onject')
##        
##c = Add(3)
##d = Add(5)
##c+d


'2) wap to create a generator by using send method'
##def foo(x):
##    for i in range(10):
##        x = yield x
##        print(x)
##        x += 8
##       
##n = foo(2)
##print(next(n))
##print(n.send(5))
##print(n.send(6))
##print(n.send(76))


'3) wap to create the generator comprehension'
##lst = (i for i in range(10) if i%2==0)
##
##for i in lst:
##    print(i)



'4) print a function n number of times using decorator'
##def ntimes(n):
##    def outer(fun):
##        def inner(*args, **kwargs):
##            for i in range(n):
##                fun(*args,**kwargs)
##        return inner
##    return outer
##
##@ntimes(6)
##def fun():
##    print('fun repeated')
##
##fun()


'5) write a python program to check the how many instance variables are there in a class.'
##class A:
##    def __init__(self,a,b):
##        self.a = a
##        self.b = b
##
##    def fun(self):
##        print(f'variables are {self.a,self.b}')
##        
##o = A(4,5)
##o.fun()
##print(o.__dict__)







