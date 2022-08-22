'1.write a program to count elements in a file?'
##with open('data.txt', 'r') as f:
##    c = f.read().split(' ')
##    print(c.count())



'2.write a python program on atleast three magic methods?'
##class Magic:
##    def __new__(cls,num):
##       
##        return super().__new__(cls)
##        
##    def __init__(self,num):
##        
##        self.num = num
##        
##    def __str__(self):
##        return('this is Magic class')
##
##    def __add__(self,other):
##        return self.num+other.num
##
##    def __iadd__(self,add):
##        self.num += add
##
##    def __lt__(self,other):
##        return self.num < other.num
##    
##ob = Magic(56)
##ob2 = Magic(45)
##print(ob)
##print(ob+ob2)
##print(ob<ob2)
##ob+=34
##print(ob)

'3.Write python program on multithreading?'
##import threading
##
##def fun():
##    for i in range(5):
##        print('hurry up')
##
##    for i in range(3):
##        print('good bye')
##
##t = threading.Thread(target=fun)
##t2 = threading.Thread(target=fun)
##t.start()
##t2.start()
##t.join()
##t2.join()
##
##for i in range(4):
##    print('after thread')




'4.Write a dictionary to a file in Python'
##capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}
##
##with open('file.txt', 'w') as f:
##    f.write(f'{capitals}')


'5.write the program to Get Yesterday’s date using Python?'
##import datetime
##
##d = datetime.datetime.today()
##
##yesterday = d - datetime.timedelta(10)
##
##print(yesterday)





