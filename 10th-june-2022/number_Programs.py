'1.Write a program to find sum of number.'
##number = int(input("Enter a number: "))
##add = 0
##while number > 0:
##
##    modulus = number % 10
##    add = add + modulus
##    number = number // 10
##
##print(add)

'WAP to find the number is strong number or not'
##num = int(input("Enter a number: "))
##add = 0
##temp = num
##while num > 0:
##    
##    modulus = num % 10
##    add += 1
##    num //= 10
##strong = temp
##number = 0
##for i in range(add):
##    quo = temp % 10
##    fact = 1
##    for j in range(1,quo+1):
##        fact = fact * j
##    number = number + fact
##    temp //= 10
##if number == strong:
##    print("It is a strong number")
##
##else:
##    print("It is not a number")
    
    
    
    

'3.Python Program to Find the Square Root'
##num = 81
##num2 = num // 2
##for i in range(num2):
##    if i * i == num:
##        print("Square root of given number is: ",i)
        


'Python Program to Calculate the Area of a Triangle'
##b = 6
##c = 4
##print("Area of a triangle is ",0.5*(b*c))



'Python Program to Solve Quadratic Equation' 
### Solve the quadratic equation ax**2 + bx + c = 0
##import cmath
##
##a = 1
##b = 5
##c = 6
##
### calculate the discriminant
##d = (b**2) - (4*a*c)
##
### find two solutions
##sol1 = (-b-cmath.sqrt(d))/(2*a)
##sol2 = (-b+cmath.sqrt(d))/(2*a)
##
##print('The solution are {0} and {1}'.format(sol1,sol2))




'Python Program to Swap Two Variables'
##a = 10
##b = 20
##a,b = b,a
##print(a,b)



'Python Program to Convert Kilometres to Miles' 
##kilometers = 7
##miles = kilometers/1.609
##print(miles)



'Python Program to Check Leap Year'
##year = 2012
##if year % 4 == 0:
##    
##    if year % 100 == 0:
##        
##        if year % 400 == 0:
##            print("It is a leap year")
##        else:
##            print("it is not a leap year")
##
##    else:
##        print("It is a leap year")
    

        
'Python Program to Check Prime Number '
##num = int(input("Enter a number: "))
##for i in range(2,num):
##    if num % i == 0:
##        print("It is not a prime number")
##        break
##else:
##    print("It is a prime number")
    


'Python Program to Find the Factorial of a Number'
##num = int(input("Enter a number: "))
##fact = 1
##for i in range(1,num+1):
##    fact = fact * i
##print(fact)



'Python Program to Print the Fibonacci sequence'
##fib = int(input("Enter a range of fib sequence: "))
##a = 0
##b = 1
##print(a,b,end = " ")
##for i in range(fib):
##    c = a+b
##    a = b
##    b = c
##    print(c,end = " ")

'Python Program to Check Armstrong Number '
##num = int(input("Enter a number: "))
##string = str(num)
##length = len(string)
##cube = 0
##for i in string:
##    i = int(i)
##    print(i)
##    cube = cube + i**length
##if cube == num:
##    print("It is a Armstrong number")
##else:
##    print("It is not a Armstrong number")


'Python Program to Find Armstrong Number in an Interval'
##min = int(input("Enter a max number: "))
##
##max = int(input("Enter a max number: "))
##
##for num in range(min,max):
##    
##    string = str(num)
##    length = len(string)
##    cube = 0
##    
##    for i in string:
##        i = int(i)
##        cube = cube + i**length
##        
##    if cube == num:
##        print(num)

'Python Program to Find the Sum of Natural Numbers'
##natural = 10
##total = 0
##for i in range(natural+1):
##    total = total + i
##print(total)
    

'Python Program to Find the Factors of a Number'
##num = int(input("enter a number: "))
##
##for i in range(1,num):
##    
##    if num % i == 0:
##        
##        print(i)



'Python Program to Convert Decimal to Binary, Octal and Hexadecimal'
"decimal to binary"
decimal = int(input("enter a number: "))
##
##while decimal > 0:
##    a = decimal % 2
##    decimal = decimal // 2
##    print(a)
    
"decimal to octal"
##octal = " "
##
##while decimal > 0:
##    modlus = decimal % 8
##    decimal = decimal // 8
##    octal = octal + str(modlus)
##    
##print(octal[::-1])

"decimal to hexadecimal"
##print(hex(decimal))

    

'Python Program to Find LCM'
##num1 = 50
##num2 = 75
##lcm = 0 
##for i in range(1,num2+1):
##    first = num1*i
##    for j in range(1,num2+1):
##        second = num2 * j
##        if first == second:
##            break
##    if first == second:
##        print(second)
##        break
        





















































