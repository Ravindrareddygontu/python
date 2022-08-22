'1) wap to print range of twin prime numbers by not using function'
##small = int(input("Enter a min range: "))
##large = int(input("Enter a max range: "))
##
##for i in range(small,large):
##    for j in range(2,i):
##        if i%j == 0:
##            break
##    else:
##        k = i+2
##        for n in range(2,k):
##            if k%n == 0:
##                break
##        else:
##            print(i,k)


'2) wap to print perimutations of the string "abc" by not using function.'
##string = "abc"
##
##for a in string:
##    for b in string:
##        for c in string:
##            if a!=b and b!=c and c!=a:
##                print(a,b,c)


'3) wap to print even and odd numbers separatly from a list by using filter function.'
##mylist = [2,3,12,36,14,436,1,26,79]
##
##evens = list(filter(lambda x : x%2 == 0,mylist))
##
##odds = list(filter(lambda x : x%2!=0, mylist))
##
##print(evens)
##
##print(odds)


'4) wap to print range of fibonacci series by using recursion function.'
##def my_function(fib):
##    if fib <= 1:
##        return fib
##    else:
##        return (my_function(fib-1)+my_function(fib-2))
##    
##num = 13
##for i in range(num):
##    print(my_function(i),end= " ")



'5) wap to print the strings from a list which are having the length of the list.'
##mylist = ["string","tuple","dictionary","sets"]
##
##length = len(mylist)
##
##for i in mylist:
##    if len(i)==length:
##        print(i)
##        break
##else:
##        print("No element is there")





























