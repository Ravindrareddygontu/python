'1.write a program Example 9: Pascals Triangle'
number = 7
for i in range(1,number):
    print(number*" ",end=" ")
    number-=1
    for j in range(1,i):
        if j<2 or j==i-1:
            print(1,end=" ")
        else:
            print(j,end=" ")
    print()
'''2.write a program to count number of chareters and print accending and desending
orderinput:RameshRamoutput:a-2,e-1,h-1,m-2,R-2,s-1-assendingdecending :s-1,R-2m-2,,h-1,e-1,a-2'''
##import collections 
##string = input("enter a string: ")
##coun = collections.Counter(string)
##mylist = []
##for key,value in coun.items():
##    mylist.append([key,value])
##print(sorted(mylist))
##print(sorted(mylist,reverse=True))


'3.Python Program to Find HCF or GCD'
##num1 = int(input("enter first number: "))
##num2 = int(input("enter second number: "))
##list1 = []
##list2 = []
##for i in range(1,num1):
##    for j in range(1,num2):
##        if num1%i==0 and num2%j==0:
##            if i==j:
##                gcd = i
##print(gcd)     


'4.Write a Python program to find the list with maximum and minimum length using lambda.'
##mylist = [1,2,12,34,21,3,3,3,53,5]
##x = lambda x:print(max(x),min(x))
##x(mylist)

'5.Write a Python program to count the same pair in two given lists. use map() function.'
##from operator import eq
##list1 = [1,2,3,4,5,6]
##list2 = [9,8,7,6,5,4]
##def same_pair(a,b):
##    count = sum(map(eq,a,b))
##    return count
##print(same_pair(list1,list2))














