'''1). wap take one example duck typing,
 in this methods you must take 3 defferent classes names and in each one class you must take 3 defferent methods'''
##class Parent:
##    def info(self):
##        print('it slows')
##    def fly(self):
##        print('it flys')
##
##class Child:
##    def info(self):
##        print('it quarel')
##    def fly(self):
##        print('child cant fly')
##obj = Parent()
##obj1 = Child()
##
##'duck typing'
##def func(obj):
##    obj.info()
##    obj.fly()
##
##func(obj)
##func(obj1)

'2). wap take one example wrong method overloding'




'''3). wap solve this pattern

  5 5 5 5 5
   * * * *
    3 3 3 
     * *
      1'''
##n = 5
##g = 0
##for i in range(n,0,-1):
##    print(g*' ',end=' ')
##    for j in range(i):
##        if n%2!=0:
##            print(n,end=' ')
##        else:
##            print('*',end=' ')
##    g += 1
##    print()
##    n -= 1


'4).wap  take one eaxmple in hierarchical method'
##class Parent:
##    def info(self):
##        print('it slows')
##    def fly(self):
##        print('it flys')
##
##class Child(Parent):
##    def info(self):
##        print('it quarel')
##    def fly(self):
##        print('child cant fly')
##
##class Child2(Parent):
##    pass
##
##obj = Child()
##obj2 = Child2()
##obj.info()
##obj2.info()


'5). What is the difference between Python Arrays and lists take one eaxmple ?'
##from array import array
##mylist = [1,2,3,4,5]
##arr = array('i',[9,8,7,6,5])
##print(mylist)
##print(arr)














