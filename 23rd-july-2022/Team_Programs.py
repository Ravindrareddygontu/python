'1.Write a Python program to get all possible combinations of the elements of a given list using itertools module.'
##import itertools
##lst = [1,2,3,4,5]
##nation = []
##for i in lst:
##    comb = list(itertools.combinations(lst,i))
##    print(comb)



'2.Write a python program to create an iterator that returns consecutive keys and groups from an iterable.'
##lst = [1,2,3,4,5,5,6]
##x = iter(lst)
##for i in lst:
##    print(next(x))




'3. Write a Python program to find the years where 25th of December be a Sunday between 2000 and 2150.'
##from datetime import timedelta,date
##import sys
##
##def days(start,end):
##    for n in range(int((end-start).days)):
##        day = start + timedelta(n)
##        if day.strftime('%m-%d') == '12-25':
##            if day.strftime('%A') == 'Sunday':
##                yield(day.strftime('%Y'))
##   
##            
##start = date(2000,3,4)
##end = date(2150,3,4)
##c = days(start,end)
##for i in c:
##    print(i)
##print(sys.getsizeof(c))






'4.write a python program using generator write armstrong.'
##num = int(input('>: '))
##def arm(num):
##    temp = num
##    count = 0
##    while temp>0:
##        div = temp%10
##        count = count+1
##        temp = temp//10
##    temp2 = num
##    cube = 0
##    while temp2>0:
##        div = temp2%10
##        cube = cube+div**count
##        temp2 = temp2//10
##        
##    if cube == num:
##        yield('armstrong')
##    else:
##        yield('not armstrong')
##
##for i in arm(num):
##    print(i)

'5.write a python program by using math module use 3 function for each function one example.'
##import math
##b = math.pow(2,4)
##n = math.floor(b)
##m = math.ceil(b)
##print(b)
##print(m)
##print(n)












