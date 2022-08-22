'1. What about two asterisks (**)?'
"** takes the keyword arguments to the function"
##def student(**marks):
##    
##    percentage = marks
##    
##    print(percentage)
##
##    
##student(physics=23,maths = 34, science =23)



'''2.Write a function called fizz_buzz that takes a number.
-If the number is divisible by 3, it should return “Fizz”.
-If it is divisible by 5, it should return “Buzz”.
-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
-Otherwise, it should return the same number.'''
##def fizz_buzz(number):
##    
##    if number % 3 == 0 and number % 5 == 0:
##        return 'Fizz Buzz'
##    
##    elif number % 3 == 0:
##        return 'Fizz'
##        
##    elif number % 5==0:
##        return 'Buzz'
##    
##    else:
##        return number
##    
##result = fizz_buzz(293)
##print(result)


'''3.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the
even and odd numbers. For example, if the limit is 3, it should print:
-0 EVEN
-1 ODD
-2 EVEN
-3 ODD'''
##def showNumbers(limit):
##
##    for i in range(limit):
##
##        if i % 2 == 0:
##            print('-',i,'EVEN')
##        else:
##            print('-',i,'ODD')
##
##showNumbers(6)
        
    

'''4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.'''
##def multiples(limit):
##    a = 3
##    b = 5
##    i= 0
##
##    while i<limit:
##        
##        if a < b and a <= limit:
##            print(a)
##            a = a + 3
##        else:
##            if b <= limit:
##                print(b)
##                b = b+5
##        i = i+1
##        
##multiples(20)
        


'5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.'

##def prime_Range(limit):
##    
##    for j in range(2,limit):
##        
##        for i in range(2,j):
##            if j % i == 0:
##                break
##        else:
##            print(j)
##
##prime_Range(23)



'''6.Write a function for checking the speed of drivers. This function should have one parameter: speed.
1.If speed is less than 70, it should print “Ok”.
2.Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
3.If the driver gets more than 12 points, the function should print: “License suspended”'''
##def check_Speed(speed):
##    
##    if speed < 70:
##        return "Ok"
##    else:
##        over = speed - 70
##        limit = over // 5
##        if limit > 12:
##            return 'License suspended'
##        else:
##            return limit,'points'
##        
##check = check_Speed(180)
##print(check)



'7. What is the result of “bag” > “apple”?'
##print("bag" < "cpple")#result is true because it compares the a and b which is b is greater than a



'8.What is the result of f“{2+2}+{10%3}”?'
##print(f"{2+2}+{10%3}")#returns 4+1



'''9.Write a function calculation() such that it can accept two variables and calculate the addition and
subtraction of it. And also it must return both addition and subtraction in a single return''' 
##def calculation(first, second):
##    addition = first + second
##    subtraction = first - second
##    return addition, subtraction
##
##result = calculation(5,3)
##print(result)


    
'''10. Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it.'''
##def outer(a,b):
##
##    def inner():
##        c = a+b
##        return c
##    inner()
##    return inner()+5
##
##result = outer(2,14)
##print(result)



'11.Write a recursive function to calculate the sum of numbers from 0 to 10'

##def add(n):
##    
##    if n == 0:
##        return n
##    else:
##        return n + add(n-1)
##
##plus = add(10)
##
##print(plus)
    


'12. Assign a different name to function and call it through the new name'
##def variable():
##    
##    a = 6
##    b = 3
##    return a+ b
##
##newname = variable()
##print(newname)



'13.Generate a Python list of all the even numbers between 4 to 30'
##def even(first, second):
##    list = []
##    for i in range(first, second):
##        if i % 2 == 0:
##            list.append(i)
##    return list
##first = 4
##second = 30
##evens = even(first, second)
##print(evens)
    


'14.Return the largest item from the given list'
##def largest(list):
##    
##    max = 0
##    for i in list:
##        if max < i:
##            max = i
##    return max
##
##items = [2,3,1,1,2,12,34,23,12,7]
##item = largest(items)
##print(item)



'''15.Create a function showEmployee() in such a way that it should accept employee name,
and it’s salary and display both, and if the salary is missing in function call it should show it as 9000'''
##
##def showEmployee(name,salary = 9000):
##
##    print(name)
##    print(salary)
##
##showEmployee('reddy')
