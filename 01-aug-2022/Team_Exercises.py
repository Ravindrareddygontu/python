'1.write a python program do multiplication program using generators and use sys module to find memory size'
##import sys
##def gen(n):
##    for i in range(10):
##        m = f'{n} x {i} = {n*i}'
##        yield m
##        
##n = gen(700)
##for i in n:
##    print(i)
##    
##print(sys.getsizeof(gen))


'2..write a python program do multiplication program using function'
##def gen(n):
##    for i in range(10):
##        m = f'{n} x {i} = {n*i}'
##        print(m)
##
##gen(12)

'3.Write a Python program to extract characters from various text files and puts them into a list.'
##a = 'abcd'
##lst = []
##for i in a:
##    with open(i+'.txt','r') as f:
##        k = f.read()
##        lst.append(k)



'4. Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'
##import string
##string = string.ascii_lowercase

##n = 8
##with open('data.txt','w') as f:
##    f.write(string[:n])




'5.write a python program in twin prime using outer and inner functions'
##def outer(n):
##    def inner():
##        for i in range(n):
##            for j in range(2,i):
##                if i%j==0:
##                    break
##            else:
##                k = i+2
##                for y in range(2,k):
##                    if k%y==0:
##                        break
##                else:
##                    print(i,k)
##    return inner()
##
##outer(30)
