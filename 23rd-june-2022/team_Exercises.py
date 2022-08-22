'''1)Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
##def my_function(string):
##    upper,lower = 0,0
##    for i in string:
##        if i.isupper():
##            upper+=1
##        elif i.islower():
##            lower+=1
##    print("UPPER CASE", upper)
##    print("LOWER CASE", lower)
##string = input("enter a sentence: ")
##result = my_function(string)
##print(result)


'2)Python Program to Remove the ith Occurrence of the Given Word in a List.'
##my_list = input("enter a string: ").split(" ")
##n = int(input("enter the ith number: "))
##for i in range(len(my_list)):
##    if i == n:
##        my_list.pop(i)
##print(my_list)


'3)Python Program to Merge Two Lists and Sort it.'
##list1 = [1,24,3,46,5]
##list2 = [63,7,81,9,12]
##list3 = list1+list2
##print(list3)
##print(sorted(list3))

     
'4)Python Program to Find the Gravitational Force between Two Objects.'
##mass1 = float(input("enter mass1 value: "))
##mass2 = float(input("enter mass2 value: "))
##distance = float(input("enter distance between two masses: "))
##G = 6.673*(10**-11)#gravitational constant
##formula = (G*mass1*mass2)/(distance**2)
##print("the gravitational force of two masses is: ", round(formula,2),"N")


'5) Write a Python Program for Even Number Pyramid Pattern'
##n = 6
##even = 0
##for i in range(n):
##    print(n*" ", end =" ")
##    n-=1
##    for j in range(i):
##        print(even,end=" ")
##        even+=2
##    print()

import itertools
##for i in itertools.accumulate([0,0,1,2,3,5,3,6,4,]):
##    print(i)
for i,j in itertools.groupby("aaaabbbbccccbaaabssss"):
    print(list(j))










