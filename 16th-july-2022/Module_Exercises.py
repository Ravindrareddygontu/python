'1.functools module'

##from functools import *
##import time

'partial'
##def foo(a,b):
##    print(a)
##    print(b)
##
##c = partial(foo,4)
##c(6)

'lru_cache()'

##@lru_cache(maxsize=None)
##def fib(num):
##    if num<2:
##        return num
##    return fib(num-1)+fib(num-2)
##
##s = time.time()
##for i in range(10):
##    print(fib(i))
##g = time.time()
##print(g-s)
##
##def fib(num):
##    if num<2:
##        return num
##    return fib(num-1)+fib(num-2)
##
##h = time.time()
##for i in range(10):
##    print(fib(i))
##n = time.time()
##print(n-h)

'reduce()'
##lis = [1,2,3,4,5]
##n = reduce(lambda x,y:x+y,lis)
##print(n)

'total_ordering()'
##@total_ordering
##class N:
##    def __init__(self,value):
##        self.value = value
##
##    def __eq__(self,other):
##        return self.value == other.value
##
##    def __lt__(self,other):
##        print(other)
##        print(other.value)
##        return self.value > other.value
##        
##obj = N('str')
##ob2 = N('str')
##print(obj < ob2)
##print(obj>=ob2)
##print(obj==ob2)
        

'2.collections'
##from collections import *

'Counter()'
##lst = 'hello world welcome to the coding'
##n = Counter(lst)
##print(n.most_common(4))

'ChainMap()'
##d1 = {'a': 1, 'b': 2}
##d2 = {'c': 3, 'd': 4}
##d3 = {'e': 5, 'f': 6}
##
##c = ChainMap(d1,d2,d3)
##print(c)

'namedtuple()'
##country = namedtuple('country',['country','code','continent'])
##d = country('india', '+91', 'asia')
##print(repr(d))

'defalutdict()'
##d = defaultdict(int)
##l = [1,2,3,4,5,6,78]
##for  i in l:
##    d[i]=[2]
##print(d)
##
##d2 = defaultdict(list)
##for i in range(10):
##    d2[i]={1,2}
##
##print(d2)

'deque()'
##d4 = deque(['name','age','gender'])
##d4.appendleft(23)
##print(d4)
##d4.append('area')
##print(d4)
##d4.pop()
##print(d4)
##d4.popleft()
##print(d4)

import requests
##n = requests.get('https://google.com',cookies={'favcolor':'white'})
##print(n.text)#it gives that page text in html

'methods'
##x = requests.delete('https://google.com',timeout = 2.04)    #requests.delete
##print(x.text)

##y = requests.head('https://google.com')        #requests.head
##print(y.headers)

##url = 'https://www.w3schools.com/python/demopage.php'
##myobj = {'somekey': 'somevalue'}
##
##x = requests.post(url, json = myobj)       #request.head
##
###print the response text (the content of the requested file):
##
##print(x.text)












