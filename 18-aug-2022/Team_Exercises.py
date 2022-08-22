'1).Write a Python program to remove and print every third number from a list of numbers until the list becomes empty'
##lst = [1,2,3,4,5,6,7,8,9]
##
##for i in lst:
##    print(lst[3])
##    lst.remove(lst[3])




'''2).. Write a Python program to count the number of students of individual class.
Sample Output:
Counter({'VI': 3, 'V': 2, 'VII': 1})'''
##import collections
##
##classes = {
##    'V': 1,
##    'VI': 1,
##    'V': 2,
##    'VI': 2,
##    'VI': 3,
##    'VII': 1,
##}
##
##n = collections.Counter(classes)
##print(n)



'3).Write a Python program to concatenate all elements in a list into a string and return it'

##def con(n):
##    return str(n)
##
##lst = [1,2,3,4,5,6]
##
##m = ''.join(list(map(con,lst)))
##print(m)



'''4).Write a Python program to convert a float to ratio. 

Expected Output :

21/5'''
##from fractions import Fraction
##value = 4.2
##n = Fraction(value).limit_denominator()
##print(n)



'5).Write a Python function that prints out the first n rows of Pascal’s triangle'
##lst = [1,1]
##print(lst)
##lst2 = []
##m = 5
##for j in range(5):
##    lst2.append(lst[0])
##    for i in range(len(lst)-1):
##        n = lst[i]+lst[i+1]
##        lst2.append(n)
##    lst2.append(lst[-1])
##    for i in lst2:
##       
##        print(i,end=' ')
##   
##    print()
##    lst = lst2
##    lst2 = []




















