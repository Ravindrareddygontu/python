'1.Write a Python class to convert an integer to a roman numeral'
##class Roman:
##    def __init__(self,integer,romans,length,num):
##        self.integer = integer
##        self.romans = romans
##        self.length = length
##        self.num = num
##        
##    def roman(self):
##        while self.num>0:
##            div = self.num//self.integer[self.length]
##            self.num = self.num%self.integer[self.length]
##            while div:
##                print(self.romans[self.length],end="")
##                div -= 1
##            self.length -= 1
##            
##integer = [1,4,5,9,10,50,100,500,1000]
##romans = ['I','IV','V','IX','X','L','C','D','M']
##length = 8
##num  = int(input('enter a number: '))
##convert = Roman(integer,romans,length,num)
##convert.roman()

'2. Write a Python class to convert a roman numeral to an integer.'
##class RomanToInt:
##    def fun(self,symbol):
##        integer = [1,4,5,9,10,50,100,500,1000]
##        romans = ['I','IV','V','IX','X','L','C','D','M']
##        num = 0
##        for i in symbol:
##            count = 0
##            for j in romans:
##                if i==j:
##                    num = num+integer[count]
##                count = count+1
##        print(num)
##symbol = input('>: ').upper()
##obj = RomanToInt()
##obj.fun(symbol)


'''3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.'''
##class Validity:
##    def string(str):
##        a = ['()','{}','[]']
##        while any(i in str for i in a):
##            for j in a:
##                str = str.replace(j,' ')
##                print(str)
##        return not str
##str = input('>: ')
##if Validity.string(str):
##    print('true')
##else:
##    print('false')


'''4.Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''
##import itertools
##class Unique:
##    def __init__(self,mylist):
##        self.mylist = mylist
##
##    def sub_set(self):
##        for i in range(len(mylist)+1):
##            for j in (itertools.combinations(mylist,i)):
##                print(list(j))
##                
##mylist = [4,5,6]
##sets = Unique(mylist)
##sets.sub_set()

'''5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.

Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4'''
##class Sum:
##    def __init__(self,mylist,num):
##        self.mylist = mylist
##        self.num = num
##    def target(self):
##        for i,j in enumerate(self.mylist):
##            n = mylist[i]+mylist[i-1]
##            if n==num:
##                print(i,i+1)
##mylist = [10,20,10,40,50,60,70]
##num = 50
##x = Sum(mylist,num)
##x.target()



'''6.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]'''
##import itertools
##class Sum:
##    def __init__(self,mylist):
##        self.mylist = mylist
##
##    def zero(self):
##        x = itertools.combinations(mylist,3)
##        for j in x:
##            if sum(j)==0:
##                    print(list(j))
##            
##mylist =  [-25, -10, -7, -3, 2, 4, 8, 10]
##real = Sum(mylist)
##real.zero()
##    




'7.Write a Python class to implement pow(x, n).'
##class Solution:
##    def isValid(s: str) -> bool:
##        if len(s) % 2 != 0:
##            return False
##        dict = {'(' : ')', '[' : ']', '{' : '}'}
##        stack = []
##        for i in s:
##            if i in dict.keys():
##                stack.append(i)
##            else:
##                if stack == []:
##                    return False
##                a = stack.pop()
##                if i!= dict[a]:
##                    return False
##        return stack == []
##string = input('>:')
##if Solution.isValid(string):
##    print('its valid')
##else:
##    print('invalid')



'''8.Write a Python class to reverse a string word by word. Go to the editor
Input string : 'hello .py'
Expected Output : '.py hello'''
##class Reverse:
##    def __init__(self,string):
##        self.string = string
##
##    def word(self):
##        mylist = string.split(' ')
##        mylist.reverse()
##        print(' '.join(mylist))
##
##string = 'hello .py'
##y = Reverse(string)
##y.word()



'9.Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.'
##class String:
##    def get_string(self,name):
##        self.name = name
##        print('accepted the string')
##    def print_string(self):
##        print(self.name)
##
##string = input('>: ')
##s = String()
##s.get_string(string)
##s.print_string()       


'10.Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.'''

##class Rectangle:
##    def __init__(self,length,width):
##        self.length = length
##        self.width = width
##
##    def area(self):
##        rec_area = (self.length*self.width)
##        print(rec_area)
##        
##length = 5
##width = 10
##x = Rectangle(length,width)
##x.area()















