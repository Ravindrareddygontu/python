'''1. Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given
string.Return True/False.'''
##string = '00001111000'
##zero = 0
##one = 0
##for i in string:
##    if i == '0':
##        zero += 1
##    if i == '1':
##        one += 1
##
##if zero==one:
##    print(True)
##else:
##    print(False)



'2. Write a Python program to add more number of elements to a deque object from an iterable object.'

##from collections import deque
##lst = [1,2,3,4,5]
##d = deque(lst)
##print(d)
##lst2 = [12,13,14,15]
##d.extend(lst2)
##print(d)


'3.Reverse a list without using inbuit method and [::-1]'
##lst = [1,2,3,4,5,6]
##count = len(lst)-1
##for i in range(len(lst)//2):
##    lst[i],lst[count] = lst[count],lst[i]
##    count -= 1
##print(lst)



'4.cummulative sum of a list'

##lst = [1,2,3,4,5,6]
##n = 0
##lst2 = []
##for i in range(len(lst)):
##    n += lst[i]
##    lst2.append(n)
##print(lst2)


'5.write one example for pickling and unpickling?'
##import pickle
##dic = {'name':'redy','age':30, 'class':7, 'gender':'male'}
##with open('data.txt','wb') as f:
##    pickle.dump(dic,f)
##
##with open('data.txt','rb') as f:
##    h = pickle.load(f)
##    print(h)














