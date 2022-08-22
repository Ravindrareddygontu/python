'''1) write a python program on files to check whether the given file exists or not. 
if it is available then print its content?'''
##import os
##if os.path.exists('poem.txt'):
##    with open('poem.txt','r') as f:
##        for i in f:
##            print(i)



'2) Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.'
##a = 'abcdefghijklmnopqrstuvwxyz'
##with open('alpha.txt','w') as f:
##    for i in range(24):
##        f.write(f'{a[i:]},{len(a)}\n')



'3) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt'
##import os
##m = 'abcdefghijklmnopqrstuvwxyz'
##for i in m:
##    open(i+'.txt','w')
        




'4) Write a Python program to interleave multiple lists of the same length. Use itertools module.'
##list1 = [100,200,300,400,500,600,700]
##list2 = [10,20,30,40,50,60,70]
##list3 = [1,2,3,4,5,6,7]
##
##import itertools
##result = itertools.chain(*zip(list1,list2,list3))
##print(list(result))





'''5) Using lambda function print following output.
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
17
fizz
19
buzz
fizz
22
23
fizz
buzz
26
fizz
28
29
fizzbuzz'''
##for i in range(1,31):
##    if i%3==0 and i%5==0:
##        print('fizzbuzz')
##    elif i%3==0:
##        print('fizz')
##    elif i%5==0:
##        print('buzz')
##    else:
##        print(i)






