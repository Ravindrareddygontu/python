'1) using functools write a program on partialmethod, url_cache and total_ordering'
from functools import *

'partial'
##def foo(a,b):
##    return a+b
##
##d = partial(foo,6)
##print(d(3))
##print(d(8))


'partial method'
##class Switch:
##    def __init__(self):
##        self.state = False
##
##    def self_state(self,new_state):
##        self.state = new_state
##        
##    
##    def states(self):
##        return self.state
##
##    switch_on = partialmethod(self_state,True)
##    switch_off = partialmethod(self_state,False)
##    
##
##s = Switch()
##
##s.switch_on()
##print(s.state)
##s.switch_off()
##print(s.state)

'lru_cache'
##import time
##
##@lru_cache(maxsize=12)
##def foo(num):
##    if num<2:
##        return num
##    return foo(num-1)+foo(num-2)
##start = time.time()
##print(foo(8))
##print(foo(5))
##stop = time.time()
##print(stop-start)
##
##def foo1(num):
##    if num<2:
##        return num
##    return foo1(num-1)+foo1(num-2)
##
##start = time.time()
##print(foo1(8))
##print(foo1(5))
##stop = time.time()
##print(stop-start)

'total_ordering'
##@total_ordering
##class Plus:
##    def __init__(self,a):
##        self.a = a
##
##    def __eq__(self,other):
##        return self.a == other.a
##
##    def __lt__(self,other):
##        return self.a >other.a
##
##n = Plus(2)
##m = Plus(5)
##print(n==m)
##print(n>=m)









