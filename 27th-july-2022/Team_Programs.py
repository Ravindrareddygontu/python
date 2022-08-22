'1.write a python program in shutil module using copy method'
##import shutil
##import os
##source = 'Problem_Solving_Question.py'
##destination = 'hii.py'
##d = shutil.copy(source,destination)
##print(d)

'2.write a pthon program in os module using rename method'
'3.write a python program in fibonacci series using outer and inner functions'
##def outer(n):
##    def inner(n):
##        if n<2:
##            return n
##        else:
##            m = inner(n-1)+inner(n-2)
##            return m
##    return inner(n)
##
##for i in range(10):
##    print(outer(i))


'4.write a python program in heapq module'
##import heapq
##lst = [2,45,2,6,2,3,5,23,5]
##v = heapq.heapify(lst)
##print(lst)


'5.write a python program in shallow copy and deep copy'

##lst = [[1,2],[3,4,5]]
##print(lst)
##'shallow copy'
##lst[1] = 5
##lst[0][1] = 8
##lst2 = lst.copy()
##print(lst)
##print(lst2)
##
##'deepcopy'
##import copy  
##x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
##z = copy.deepcopy(x)  
##  
##x[2][2] = 'Hello'  
##print(x)
##print(z)
