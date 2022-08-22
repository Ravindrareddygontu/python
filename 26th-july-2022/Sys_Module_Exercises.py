import sys

'1.write a python program in prime number using outer and inner function'
##def outer(func):
##    def inner(m):
##        count = 1
##        for i in range(1,m):
##            if m%i==0:
##                count += 1
##        if count==2:
##            print('it is prime number')
##        else:
##            func(m)
##    return inner
##
##@outer
##def first(m):
##    print('it is not a prime')
##    
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            first(int(num))
##    except ValueError:
##        print('wrong entry')
##        break
        
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
##@outer
##def second(n):
##    print('it not an armstrong')
##
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            second(int(num))
##    except ValueError:
##        print('wrong entry')
##        break


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
##@fun
##def fun2(n):
##    print('it is not strong')
##
##print('Ente a number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            fun2(int(num))
##    except ValueError:
##        print('wrong entry')
##        break


'4.write a python program in palindrome for integers using inner and outer function'

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
##@fun          
##def foo(num):
##    print('it is a palindrome')
##    
##n = int(input('>:'))
##print('Ente a number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            f00(int(num))
##    except ValueError:
##        print('wrong entry')
##        break

'5.write a python program in perfect number using outer and inner function'
##def outer(fun):
##    def inner(m):
##        for n in range(1,m):
##            count = 0
##            for i in range(1,n):
##                if n%i == 0:
##                    count += i
##            if count == n:
##                fun(n)
##    return inner
##
##@outer
##def perfect(m):
##    print(m)
##
##print('Ente a range number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            perfect(int(num))
##    except ValueError:
##        print('wrong entry')
##        break



'6.write a python program in factorial number using outer and inner function'
##def outer(fun):
##    def inner(m):
##        fact = 1
##        for i in range(1,m+1):
##            fact = fact*i
##        fun(fact)
##    return inner
##
##@outer
##def factorial(n):
##    print(f'factorial of given number:',n)
##
##n = int(input('>:'))
##print('Ente a number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            factorial(int(num))
##    except ValueError:
##        print('wrong entry')
##        break



'7.write a python program in odd or even number using outer and inner function'
##def outer():
##    def inner(m):
##        if m%2 != 0:
##            print('odd')
##        else:
##            print('even')
##            
##    return inner
##
##print('Ente a number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            outer()(int(num))
##    except ValueError:
##        print('wrong entry')
##        break


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
##@outer        
##def first(n):
##    print('Octal form of a given number is:')
##
##print('Ente a number:')
##for i in sys.stdin:
##    try:
##        if int(i):
##            num = i
##            first(int(num))
##    except ValueError:
##        print('wrong entry')
##        break

'10.write a python program in lcm number using outer and inner function'

##def outer(func):
##    def inner(*args,**kwargs):
##        print('sys')
##        high = max(num1,num2)
##        print(int(num1))
##        while True:
##            if high%num1==0 and high%num2==0:
##                break
##            high += 1
##        func(*args,**kwargs)
##        print(high)
##    return inner
##
##@outer    
##def lcm(*args,**kwargs):
##    print('lcm of given two numbers are:')
##
##num1 = sys.argv[1]
##num2 = sys.argv[2]
##num1 = int(num1)
##num2 = int(num2)
##lcm(num1,num2)














