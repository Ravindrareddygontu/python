##'polymorphism'
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
##
##'Strong Typing'
##def func(obj):
##    if hasattr(obj,'show'):
##        obj.show()
##
##    if hasattr(obj,'fun'):
##        obj.fun()
##func(obj)
##func(obj1)
