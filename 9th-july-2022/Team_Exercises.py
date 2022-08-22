'''1write a program to print the list of elements of prinicipal diaognal
input:
3 3
1  2 3
10 20 30
5  10 15
output:[1, 20, 15]'''
##mylist = [[1,2,3],[10,20,30],[5,10,15]]
##count = 0
##list2 = []
##for i in mylist:
##    list2.append(i[count])
##    count+=1
##print(list2)



'''2.wap take a string sparate with space and done add,sub,mul,div?
eg:- input:-18 7
     output:-(25,12,126,2)'''
##string = input('>:').split(' ')
##mylist = []
##for i in string:
##    c = int(i)
##    mylist.append(c)
##    
##print(mylist)
##print(mylist[0]+mylist[1])
##
##print(mylist[0]-mylist[1])
##print(mylist[0]*mylist[1])
##print(mylist[0]//mylist[1])


'''3.In this question, we will provide an integer int_1, we have already declared the calculate_sum 
function for you in solution.py. The initial int_1 of this function represents the initial value, 
and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.
input:5
output:6170'''
##num = 5
##c = 0
##b = 0
##for i in range(num-1):
##    b = b*10+num
##    c = c+b
##print(c)



'''4.Please complete the code in solution.py to realize the function of get_sum. get_sum function receives an array parameter nums. Please use the lambda function to pass 
in two unknown number x and y for the get_sum function and take this lambda function as the return value of the get_sum function. For the parameter nums received by get_sum, 
if the length of the array num is an even number, return the sum of nums by x times. If the length of the array num is an odd number, return the sum of nums by -y times.
input:[1,2,3,4]
       2,3
output:20'''
##mylist = [1,2,3,4,5]
##x = 10
##y = 20
##
##def get_sum(lst,x,y):
##    if len(lst)%2==0:
##        add = sum(lst)*x
##        return add
##    else:
##        sub = sum(lst)*-y
##        return sub
##x = get_sum(mylist,x,y)
##print(x)    


'''5.Mathematicians have come up with a famous conjecture - the Collatz conjecture.
For any positive integer n, if n is even, make it n // 2.
If n is an odd number, make it 3 * n + 1.
If you follow this rule, you must end up with 1.
How many rounds of transformation will that number go through to become 1?'''
##num = 8
##while num>1:
##    if num%2==0:
##        num = num//2
##        print(num,end=' ')
##    else:
##        num = 3*num+1
##        print(num,end=' ')
    














