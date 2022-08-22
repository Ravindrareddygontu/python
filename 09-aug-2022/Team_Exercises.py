'1. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.'
##def make_bold(fn):
##    def wrapped():
##        return "<b>" + fn() + "</b>"
##    return wrapped
##
##def make_italic(fn):
##    def wrapped():
##        return "<i>" + fn() + "</i>"
##    return wrapped
##
##def make_underline(fn):
##    def wrapped():
##        return "<u>" + fn() + "</u>"
##    return wrapped
##@make_bold
##@make_italic
##@make_underline
##def hello():
##    return "hello world"
##print(hello()) 


'''2. Write a Python program to extract specified size of strings from a give list of string values using lambda.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
length of the string to extract:
8
After extracting strings of specified length from the said list:
['practice', 'solution']'''
##lst = ['Python', 'list', 'exercises', 'practice', 'solution']
##
##fil = list(filter(lambda x: len(x)==8, lst))
##print(fil)



'3. Write a Python program to create a deep copy of a given dictionary. Use copy.copy'
##import copy 
##
##words = {
##    "Hello": 56,
##    "at" : 23 ,
##    "test" : 43,
##    "this" : 43,
##    "who" : [56, 34, 44]
##    }
##
##dic = copycopy(words)
##words['at'] = 45
##print(words)
##print(dic)


'4. Write a Python Program to Check a Number is a Spy Number or Not? note:- without  forloop.'
##num = int(input('>:'))
##plus = 0
##product = 1
##
##while num>0:
##    div = num%10
##    plus += div
##    product *= div
##    num = num//10
##
##if plus==product:
##    print('it is a spy number')
##    
##else:
##    print('it is not a spy number')


'''5. Write a Python program to find the XOR of two given strings interpreted as binary numbers.
Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111'''


##first = '100011101100001'
##second = '100101100101110'
##s = ''
##
##for i in range(len(first)-1,-1,-1):
##    if first[i] == second[i]:
##        s += '0'
##    else:
##        s += '1'
##
##print(s[::-1])



'using bin'

##lst = ['0001', '1011']
##lst2 = ['100011101100001', '100101100101110']
##print(bin(int(lst2[0],2) ^ int(lst2[1],2)))























    





























