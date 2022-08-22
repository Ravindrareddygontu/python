'1.write a python program in prime number using outer and inner function'
##def outer(m):
##    def inner():
##        count = 1
##        for i in range(1,m):
##            if m%i==0:
##                count += 1
##        if count==2:
##            print('it is prime number')
##        else:
##            print('it is not prime')
##    return inner()
##
##num = int(input('>:'))
##outer()


'2.write a python program in armstrong number using outer and inner function'
##def outer(func):
##    def inner(n):
##        temp = n
##        count = 0
##        while temp:
##            count+=1
##            temp //= 10
##            temp2 = n
##            count2 = 0
##        while temp2:
##               div = temp2%10
##               count2 += div**count
##               temp2 //= 10
##        if count2==n:
##              print('it is armstrong')
##        else:
##           func(n)
##
##    return inner
##
##def second(n):
##    print('it not an armstrong')
##    
##d = outer(second)
##d(154)

'3.write a python program in strong number using outer and inner function'
##def fun(foo):
##    def inner(n):
##        count = 0
##        temp = n
##        while temp:
##            div = temp%10
##            fact = 1
##            for i in range(1,div+1):
##                fact = fact*i
##            count+=fact
##            temp //= 10
##        if count == n:
##            print('it is strong')
##        else:
##            foo(n)
##    return inner
##
##def fun2(n):
##    print('it is not strong')
##
##fun(fun2)(145)



'4.write a python program in palindrome for integers using inner and outer function'
##n = int(input('>:'))
##def fun(foo):
##    def inner(n):
##        num = 0
##        temp = n
##        while n:
##            div = n%10
##            num = num*10+div
##            n//=10
##        
##        if num==temp:
##            foo(n)
##        else:
##            print('it is not a palindrome')
##    return inner
##            
##def foo(num):
##    print('it is a palindrome')
##
##m = fun(foo)
##m(n)

'5.write a python program in perfect number using outer and inner function'
##def outer(fun):
##    def inner(m):
##        for n in range(m):
##            count = 0
##            for i in range(1,n):
##                if n%i == 0:
##                    count += i
##            if count == n:
##                fun(n)
##    return inner
##
##def perfect(m):
##    print(m)
##
##btw = int(input('enter a range of perfect numbers: '))
##outer(perfect)(btw)


'6.write a python program in factorial number using outer and inner function'
##def outer(fun):
##    def inner(m):
##        fact = 1
##        for i in range(1,m+1):
##            fact = fact*i
##        fun(fact)
##    return inner
##
##def factorial(n):
##    print(f'factorial of given number:',n)
##
##n = int(input('>:'))
##j = outer(factorial)
##j(n)



'7.write a python program in odd or even number using outer and inner function'
##def outer():
##    def inner(m):
##        if m%2 != 0:
##            print('odd')
##        else:
##            print('even')
##            
##    return inner
##outer()(7)


'8.write a python program in even or odd number using outer and inner function'
##def outer():
##    def inner(m):
##        if m%2 != 0:
##            print('odd')
##        else:
##            print('even')
##            
##    return inner
##outer()(7)

'9.write a python program convert octal to decimal  using outer and inner function'
##def outer(func):
##    def inner(n):
##        tmp = n
##        count = 0
##        octal = 0
##        while n:
##           div = n%10
##           octal = octal + div*(8**count)
##           count += 1
##           n //= 10
##        func(n)   
##        print(octal)
##    return inner
##        
##def first(n):
##    print('Octal form of a given number is:')
##
##outer(first)(78)



'10.write a python program in lcm number using outer and inner function'

##def outer(func):
##    def inner(*args,**kwargs):
##        num1 = 12
##        num2 = 13
##        high = max(num1,num2)
##        while True:
##            if high%num1==0 and high%num2==0:
##                break
##            high += 1
##        func(high)
##    return inner
##    
##def lcm(num1):
##    print(num1)
##
##n = outer(lcm)
##n()

'''Note:these 10 programs should be write in decorator
and again these 10 should be write in sys module'''
import sys
for i in sys.stdin:
    print(i)

















