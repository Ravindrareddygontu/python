'1.Write a Python program to read last n lines of a file.'

##with open('data.txt','r') as f:
##    r = f.read().split('\n')
##    print(r[-4:])


'2.Write a Python program to read a file line by line and store it into a list.'
##with open('data.txt') as f:
##    lst = f.read().split('\n')
##    print(lst)



'3.Write a Python program to read a file line by line store it into a variable.'
##with open('data.txt','r') as f:
##    string = ''
##    for i in f.read():
##        string = string+i
##    print(string)


'5. Write a Python program to count the frequency of words in a file'
##import collections
##with open('data.txt','r') as f:
##    r = f.read()
##    count = collections.Counter(r)
##    print(count)


'6. Write a Python program to read a random line from a file.'
##import random
##with open('data.txt','r') as f:
##    ran = random.randint(1,10)
##    r = f.readlines()[ran]
##    print(r)


'7.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.'
'8.Write a Python program to extract characters from various text files and puts them into a list.'
##alpha = 'abcdefghijklmnopqrstuvwxyz'
##lst = []
##for i in alpha:
##    with open('i','r') as f:
##        for i in f.read:
##            if i == 't':
##                lst.append(i)



'''9.Write a Python program that takes a text file as input and returns the number of words of a given text file
Note: Some words can be separated by a comma with no space.'''
##n = input('>: ')
##with open(n+'.txt','r') as f:
##    lst = f.read().split()
##    print(len(lst))



'10.Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line'
##alpha = 'abcdefghijklmnopqrstuvwxyz'
##
##with open('data2.txt','w') as f:
##        n = 20
##        f.write(alpha[:n])
##













