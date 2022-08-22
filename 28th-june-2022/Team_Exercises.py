'1.write a python program to find the Nth term in a fibonacci series using recursion.'
##def fib(num):
##   if num <= 1:
##       return num
##   else:
##       j = fib(num-1)+fib(num-2)
##       return j
##num = int(input("enter a number: "))
##x = fib(num)
##print(x)

'2.write a python program to implement matrix multiplication.'
##list1 = [[3,2,1],
##         [2,3,4],
##         [3,2,1]]
##list2 = [[1,2,3],
##         [2,3,2],
##         [2,1,0]]
##list3 = []
##for i in list1:
##    n,k,m,l= 0,0,0,0
##    for j in list2:
##       k = k+(i[n]*j[0])
##       m = m+(i[n]*j[1])
##       l = l+(i[n]*j[2])
##       n+=1
##       
##    b = [k,m,l]
##    list3.append(b)
##print(list3)
       
'3.write a python program to draw a circle of square using turtle.'
##from turtle import *
##for i in range(60):
##    for j in range(4):
##        fd(100)
##        rt(90)
##    rt(6)


'4.write a python program even and odd using list comprehension.'
##mylist = [i for i in range(10)]
##odds = [i for i in mylist if i%2!=0]
##evens = [j for j in mylist if j%2==0]
##print(odds)
##print(evens)


'5.write a python program  to print the number from a given number N till 0 using recursion.'
##n = int(input())
##def rec(n):
##    if n==0:
##        print(0)
##    else:
##        print(n)
##        rec(n-1)
##    
##rec(n)










