'''ChildThreadConstructor.'''
##from threading import Thread
##
##class mythread(Thread):
##    def __init__(self):
##        Thread.__init__(self)
##        print("child thread")
##    def run(self):
##        pass
##t=mythread()
##t.start()
##print("main thread")


''' Creating a thread by creating a child class to Thread class'''

##from threading import Thread
##
##class mythread (Thread):
##    def __init__(self,a):
##        Thread.__init__(self)
##        
##print("Thread Constructor",a)
##    def run(self):
##        pass
##t=mythread(10)
##t.start()
##print("main thread")


'''Creating a thread Without creating a child class to Thread class'''

##from threading import Thread
##class mythread:
##    def disp(self,a,b):
##        print(a,b)
##my=mythread()
##
##t=Thread(target=my.disp,args=(10,29))
##t.start()


# Single Tasking using a Thread

##from threading import Thread
##from time import*
##class myexam:
##    def solve_question(self):
##        self.task1()
##        self.task2()
##        self.task3()
##        
##    def task1(self):
##        print("Question 1")
##    def task2(self):
##        print("Question 2")
##    def task3(self):
##        print("Question 3")
##my=myexam()
##t=Thread(target=my.solve_question)
##t.start()

'''MultitaskingUsingMultiThread'''

##from threading import Thread
##class Hotel:
##	def __init__(self, t):
##		self.t = t
##
##	def food(self):
##            for i in range(1, 6):
##	      print(self.t, i)
##			
##h1 = Hotel('Take Order From Table: ')
##h2 = Hotel('Serve Order to Table: ')
##t1 = Thread(target=h1.food)
##t2 = Thread(target=h2.food)
##
##t1.start()
##t2.start()

'''Multitasking using Multiple Thread
# Two Threads acting on same method'''


##from threading import Thread, current_thread
##class Flight:
##	def __init__(self, available_seat):
##		self.available_seat = available_seat
##		
##	def reserve(self, need_seat):
##		print('Available Seats:', self.available_seat)
##		if(self.available_seat >= need_seat):
##			name = current_thread().name
##			print(f'{self.available_seat} seat is alloted for {name}')
##			self.available_seat -= need_seat
##			
##		else:
##			print('Sorry! All seats has alloted')
##f = Flight(1)
##t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
##t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
##t1.start()
##t2.start()



'''Multitasking using Multiple Thread
# Two Threads acting on same method'''

##from threading import*
##class Flight:
##    def __init__(self,avail_seat):
##        self.avail_seat=avail_seat
##        self.l=Lock()
##    def reserve(self,need_seat):
##        self.l.acquire(blocking=True)
##        print("available seats are:",self.avail_seat)
##        if (self.avail_seat>=need_seat):
##            name=current_thread().name
##            print(f"{need_seat}seat is allocated for {name}")
##            self.avail_seat-=need_seat
##        else:
##            print("sorry! All seats are alloted")
##        self.l.release()
##f=Flight(2)
##t1=Thread(target=f.reserve ,args=(1,),name='Rahul')
##t2=Thread(target=f.reserve,args=(1,),name="venu")
##t3=Thread(target=f.reserve,args=(1,),name="janu")
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("should print at the end")


# Multitasking using Multiple Thread
# Two Threads acting on same method
##from threading import *
##class Flight:
##	def __init__(self, available_seat):
##		self.available_seat = available_seat
##		self.l = Lock()
##		print(self.l)
##		
##	def reserve(self, need_seat):
##		self.l.acquire()
##		self.l.acquire()
##		print(self.l)
##		print('Available Seats:', self.available_seat)
##		if(self.available_seat >= need_seat):
##			name = current_thread().name
##			print(f'{need_seat} seat is alloted for {name}')
##			self.available_seat -= need_seat
##		else:
##			print('Sorry! All seats has alloted')
##		self.l.release()
##		self.l.release()
##f = Flight(2)
##t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
##t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
##t3 = Thread(target=f.reserve, args=(1,), name='Raj')
##t1.start()
##t2.start()
##t3.start()
##t1.join()
##t2.join()
##t3.join()
##print("Main Thread")

'Dead Lock Example'
##import threading
##l = threading.Lock()
##l.acquire()
##l.acquire()
##def fun1():
##        print('this is function one')
##
##def fun2():
##        print('this is function two')
##l.release()
##l.release()
##
##
##t1 = threading.Thread(target=fun2)
##t2 = threading.Thread(target=fun1)
##t1.start()
##t2.start()
##t1.join()
##t2.join()















