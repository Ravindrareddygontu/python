'1.write a python program on logging'
##import logging
##logging.basicConfig(filename='pythonw.log', level=logging.INFO,
##                    format='%(lineno)s::%(asctime)s::%(levelname)s::%(message)s::%(name)s')
##logger = logging.getLogger('ravindra')
##
##def decor(fun):
##    logger.info('Enter user input validation')
##    def fun(user):
##        lst = ['ravindra', 'reddy']
##        if user in lst:
##            logging.info('user data is in the database')
##            return 'welcome'+' '+user
##        else:
##            logger.debug('User name not presented in the database')
##            return 'invalid user'
##    return fun
##
##@decor
##def login_user(user):
##    return user
##
##user = input('>: ')
##print(login_user(user))



'2.write a python program to remove all the occurances of the given number'
##lst = [2,3,4,5,4,5,3,5,2,5,2,5,5,2,6,36,6,2,5,2]
##element = 2
##
##for i in lst:
##    if i==element:
##        lst.remove(i)
##print(lst)


'3.write a python program to exact the numbers in a given string and print sum,minimum and maximum of those numbers'
##string = input('>:').split()
##print(string)
##print(min(string))
##print(max(string))
##s = 0
##for i in string:
##    s += int(i)
##print(s)



'''4.write a python program on sprial number 
eg:-9 8 7     
    2 1 6        
    3 4 5'''
##spi = int(input('enter the range of spiral:'))
##lst = []
##lst2 = []
##n = 3
##for i in range(spi-1,0,-1):
##    for j in range(n):
##        lst.append(i)
##    if n==3:
##        n=2
##
##lst.append(1)
##print(lst)
##for i in lst:
##    for j in range(i):
##        lst2.append(j)
##
##m = 1
##k = 0
##element = spi*spi
##for i in lst:
##    for j in range(i):
##        lst2[k] = element
##        element -= 1
##        k += m
##    if m == 1:
##        m = spi
##    elif m == -1:
##        m = -spi
##    elif m == -spi:
##        m = 1
##    else:
##        m = -1
##
##print(lst2)
##
##for i in range(1,len(lst2)+1):
##   print(lst2[i-1],end=' ')
##   if i%spi==0:
##       print()






'''5.create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,33,33,22,22,1,1,1]'''

##n = int(input('>:'))
##m = 3
##lst = []
##for i in range(n-1,0,-1):
##    
##    if i==n-1 or i==1:
##        lst.append(i)
##        lst.append(i)
##        lst.append(i)
##    else:
##        lst.append(i*11)
##        lst.append(i*11)
##    
##print(lst)














