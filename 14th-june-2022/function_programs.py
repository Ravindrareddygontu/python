'''1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
##def divisible(x,y):
##    for i in range(x,y):
##        if i%7 == 0 and i%5 != 0:
##            print(i,end = ",")
##
##divisible(2000,3200)



'''2.Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320'''

##def fact(mylist):
##    for i in mylist:
##        factorial = 1
##        for j in range(1,i+1):
##            factorial *= j
##        print(factorial,end = ",")
##
##mylist = [2,4,5,7,8]
##fact(mylist)
            

'''3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

##def diction(n):
##    mydict2 = dict()
##    
##    for i in range(1,n+1):
##        
##        mydict = {i:i*i}
##        mydict2.update(mydict)
##    print(mydict2)
##    
##diction(9)
    


'''4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''

##def sequence(mylist):
##    mytuple = tuple(mylist)
##    print(mylist)
##    print(mytuple)
##    
##num = input("Enter a list: ")
##mylist = num.split(",")
##sequence(mylist)


'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

'''6.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''


##def my_function(D):
##    for i in D:
##        C = 50
##        H = 30
##        formula = (2* C* i)/H
##        formula = int(formula)
##        for i in range(formula):
##            if i*i > formula:
##                print(i-1)
##                break
##
##mylist = 100,150,180
##my_function(mylist)



'''7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''



'''8.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''
##def my_function(string):
##    string2 = sorted(string)
##    for i in string2:
##        print(i,end=",")
##
##num = input("Enter numbers: ")
##mylist = num.split(",")
##my_function(mylist)



'''9.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT'''
##def my_function(string):
##    string.upper()
##    print(string.upper())
##
##string = input(" ")
##string2 = input(" ")
##my_function(string)
##my_function(string2)




'''10.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''
##def my_function(string):
##    list1 = []
##    
##    for i in string:
##        if i not in list1:
##                list1.append(i)
##                
##    string = sorted(list1)
##    
##    for i in string:
##        print(i,end = " ")
##        
##string2 = input(" ")
##mylist = string2.split(" ")
##print(mylist)
##my_function(mylist)  



'''11.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.'''
##def my_function(binaryList):
##    for binary in binaryList:
##        binary2 = binary[::-1]
##        k = 0
##        digit = 0
##        for i in binary2:
##            twos = 2**k
##            k = k+1
##            if i == "1":
##                digit = digit + twos
##        if digit%5 == 0:
##            print(binary)
##            
##binary = ["0100","0011","1010","1001"]
##my_function(binary)



'''12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''
##def my_function(smaller,greater):
##    
##    for i in range(smaller,greater):
##        count = 0
##        even = i
##        
##        while i>0:
##            divide = i%10
##            if divide % 2 == 0:
##                count = count +1
##            i = i//10
##            
##        if count == len(str(even)):
##           print(even,end = ",")
##       
##smaller = 1000
##greater = 3000
##my_function(smaller,greater)




'''13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''
##string = input(" ")
##letters, digits = 0,0
##
##for i in string:
##    if i.isalpha():
##        letters = letters + 1
##    elif i.isdigit():
##        digits = digits + 1
##
##print("LETTERS ",letters)
##print("DIGITS", digits)
    

'''14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''

##string = input(" ")
##
##upper, lower = 0,0
##
##for i in string:
##    if i.isupper():
##        upper += 1
##    if i.islower():
##        lower += 1
##
##print("UPPER ",upper)
##print("LOWER ",lower)






'''15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

##def my_function(a):
##    i = 0
##    k = 0
##    n = a
##    while i<4:
##        k = k+a
##        a = a*10+n
##        i = i+1
##    print(k)
##
##my_function(9)
    





























