'''1.. Write a Python program that invoke a given function after specific milliseconds. 
inputs:100ms-16
1000ms-100
2000ms-25100
Sample Output:
Square root after specific miliseconds:
4.0
10.0
158.42979517754858'''
##import inspect
##import time
##import itertools
##import math
##
##def square(num):
##    print(math.sqrt(num))
##
##ms = int(input('enter milliseconds: '))
##num = int(input('enter a square root number: '))
##length = len(str(ms))
##t = ms/100
##print('sleeping time is:',t)
##time.sleep(t)
##square(num)


'''2  we will provide two lists list_1 and list_2.
 The list_1 and list_2 of this function represent the initial list. Need to comprehend by list:
1Multiply each value in the two lists separately
2Add each value in the two lists separately
3Multiply the values in the two lists
by using inner and outer functions''' 
lst1 = [1,2,3,4]
lst2 = [6,7,8,9]





'''3.Write a Python program to build a list, using an iterator function and an initial seed value.

1.The iterator function accepts one argument (seed) and must always return a list with two elements ([value, nextSeed]) or False to terminate.
2.Use a generator function, fn_generator, that uses a while loop to call the iterator function and yield the value until it returns False.
3.Use a list comprehension to return the list that is produced by the generator, using the iterator function.'''
##def iterator(seed):
##    lst = [4]
##    lst.append(seed)
##    return lst
##
##def gener(num):
##    while True:
##        yield iterator(num)
##
##lst2 = [next(gener(i)) for i in range(10)]
##print(lst2)
      




'4.Write a Python program to create Cartesian product of two or more given lists using itertools.'
##import itertools
##lst1 = [1,2,3]
##lst2 = [5,6]
##print(list(itertools.product(lst1,lst2)))


'5.Write a Python program to count the frequency of the elements of a given unordered list by using itertools' 
##import itertools
##lst = [1,1,1,1,2,2,2,1,1,5,5,5]
##for i,j in itertools.groupby(lst):
##    print(len(list(j)))




