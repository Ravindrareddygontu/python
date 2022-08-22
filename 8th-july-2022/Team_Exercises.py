'1.Define Multiple inheritance and write an example?'
##class Father:
##    def __init__(self,fname):
##        self.fname = fname
##
##class Mother:
##    def __init__(self,mname):
##        self.mname = mname
##
##class Child(Mother,Father):
##    def __init__(self,mname,fname,cname):
##        super().__init__(mname)
##        Father.__init__(self,fname)
##        self.cname = cname
##        
##    def func(self):
##        print(self.fname,self.mname,self.cname)
##
##obj = Child('gang','bang','teet')
##obj.func()

        
'2.WAP on Duck type polymorphism. with example'
'polymorphism'
##class Father:
##    def show(self):
##        print('father class')
##
##    def fun(self):
##        print('father function')
##
##class Mother:
##    def show(self):
##        print('mother class')
##
##    def fun(self):
##        print('mother function')
##
##obj = Father()
##obj1 = Mother()
##
##'Duck Typing'
##def func(obj):
##    obj.show()
##    
##func(obj)
##func(obj1)
##
##for i in (obj,obj1):
##    i.show()
##    i.fun()


'3.demonstrate strong typing method in polymorphism with example'
##'Strong Typing'
##def func(obj):
##    if hasattr(obj,'show'):
##        obj.show()
##
##    if hasattr(obj,'fun'):
##        obj.fun()
##func(obj)
##func(obj1)


'4.write a program Russian Multiplication using class and object'
##class Multi:
##    def russian(self,a,b):
##        res = 0
##
##        while b>0:
##            if b&1:
##                res = res+a
##
##            a = a<<1
##            b = b>>1
##        return res
##obj = Multi()
##print(obj.russian(4,5))


'5.write a program about ojas organization parent class is ojas and child class is OILC write differnt batches as methods define batchs name with inheritance.'
##class Ojas:
##    def __init__(self,name):
##        self.name = name
##
##    def hr(self):
##        print('hr activities')
##
##    def training(self):
##        print('trainers activities')
##        
##    def payroll(self):
##        print('salary team activities')
##
##    def delivery(self):
##        print('project delivery activities')
##        
##class Oilc(Ojas):
##    pass
##
##obj = Oilc('Ojas')
##obj.hr()
##obj.training()
##obj.payroll()
##obj.payroll()
##obj.delivery()




























