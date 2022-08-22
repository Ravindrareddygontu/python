'''1.Write a Python program to convert string element to integer inside a given tuple using lambda.
input tuple values:
(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
output tuple values:
((233, 33), (1416, 55), (2345, 34))'''
##mytuple = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
##mylist = []
##for j in mytuple:
##    m = list((j))
##    for i in m:
##        if i.isalpha():
##            m.remove(i)
##    mylist.append(tuple(m))
##print(tuple(mylist))



'2. Write a Python program to extract year, month, date and time using Lambda.'
##from datetime import datetime
##currentdate = datetime(2012,12,12)
##year = lambda x: x.year
##month = lambda x: x.month
##day = lambda x: x.day
##print(year(currentdate))
##print(month(currentdate))
##print(day(currentdate))


'''3. Largest missing negative number 
you are given unsorted array A of N integers . you have to find the largest negative integer missing from the array.
example:1
input: A = -2 -1 0 1 2 
output:-3
example2:
input:-11 -10 -12
output:-1'''
##mylist = [-2,-1,0,1,2]
##negative = -1
##for i in mylist:
##    if negative in mylist:
##        negative -= 1
##print(negative)



'''4. Roman Numerals
Write a program to convert a non-negative integer N to its Roman numeral representation. Roman numerals are usually written largest to smallest from left to right.
symbol value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
A number containing several decimal digits is built by appending Roman numeral equivalent for each, from highest to lowest, as in the following examples:
39 = XXX + IX = XXXIX.
246 = CC + XL + VI = CCXLVI.
789 = DCC + LXXX + IX = DCCLXXXIX.
2,421 = MM + CD + XX + I = MMCDXXI.
160 = C + LX = CLX
207 = CC + VII = CCVII
1,009 = M + IX = MIX
1,066 = M + LX + VI = MLXVI
1776 = M + DCC + LXX + VI = MDCCLXXVI
1918 = M + CM + X + VIII = MCMXVIII
Sample Input 1
2
Sample Output 1
II
Sample Input 2
1994
Sample Output 2
MCMXCIV'''
##numbers = [1,4,5,9,10,50,100,500,1000]
##romans = ["I","IV","V","IX","X","L","C","D","M"]
##length = 8
##num = int(input("enter a number: "))
##while num:
##    div = num//numbers[length]
##    num = num%numbers[length]
##
##    while div:
##        print(romans[length],end="")
##        div -= 1
##    length -= 1


'''5.Group similar elements in a list:
Input : [1, 3, 5, 1, 3, 2, 5, 4, 2]
Output : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]'''
##mylist = [1,3,5,1,1,3,2,5,4,2,2]
##list2 = []
##list3 = []
##for i in mylist:
##    if mylist.count(i)>1:
##        string = str(i)*mylist.count(i)
##        list3 = list(string)
##        if list3 not in list2:
##            list2.append(list3)
##    else:
##        list2.append([i])
##print(list2)












