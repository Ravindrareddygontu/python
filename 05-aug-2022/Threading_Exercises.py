##import threading
##import time

'without threading'
##start = time.time()
##def fun():
##    print(threading.main_thread())
##    time.sleep(1)
##    n =10000000
##    while n>0:
##        n-=1
##    print('end fun')
##
##
##fun()
##fun()
##
##end = time.time()
##print('time consumed:',end-start)



'with multithreading'
##start = time.time()
##def fun():
##    print(threading.main_thread())
##    time.sleep(1)
##    n =10000000
##    while n>0:
##        n-=1
##    print('end fun')
##
##
##f = threading.Thread(target=fun)
##f1 = threading.Thread(target=fun)
##f.start()
##f1.start()
##f.join()
##f1.join()
##
##end = time.time()
##print('time consumed:',end-start)

'threading in without childclass'
##from threading import Thread
##
##class Stu:
##    def __init__(self, a):
##        self.a = a
##
##    def display(self):
##        for i in range(5):
##            print(self.a,i)
##
##
##        
##obj = Stu('ravindra')
###obj = obj.display()
##t = Thread(target=obj.display)
##t.start()
##t.join()
##
##
##h = Stu('reddy')
##t2 = Thread(target=h.display)
##t2.start()
##t2.join()



'threading in child class'
##import threading
##class mythread(threading.Thread):
##    def run(self):
##        for x in range(7):
##            print("Hi from child")
##
##a = mythread()
##b = mythread()
##b.start()
##a.start()
##a.join()
##b.join()
##print("Bye from",threading.current_thread())


'threading in child class using time'
##import threading
##import time
##class mythread(threading.Thread):
##    def run(self):
##        for x in range(7):
##            print("Hi from child")
##
##s = time.time()
##            
##a = mythread()
##b = mythread()
##b.start()
##a.start()
##a.join()
##b.join()
##
##e = time.time()
##print("Bye from",threading.current_thread())
##print(e-s)
















