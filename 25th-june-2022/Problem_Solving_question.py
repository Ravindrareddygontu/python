'''given alist of integers write a program to print the count of all possible unique combinations of numbers whose sum is equal to k
explanation:for example if given list of integers and k are 
2 4 6 1 3
6
all possible combinations of the given list are
(6,)(2,)(4,)(1,)(  3,)
(2,4)(1,2)(3,4)(4,6)(1,4)(2,3)(2,6)(3,6)(1,6)(1,3)
(3,4,6)(2,3,6)(1,2,6)(1,2,3)(1,4,6)(1,3,4)(2,3,4)(1,3,6)
(2,3,4,6)(1,2,3,4)(1,2,4,6)(1,2,3,6)(1,3,4,6)
out of all the above combinations  the unique combinations with the sum equal to 6 are
6
2 4
2 1 3
so the output should be the count of unique combinations which is 3
for example if the given list of integers and k are
-1 4 5 6 7 8 2 4 5 2 3 8
7
The unique combinations with the sum equal to 7 are
7
-1 8
3 4
2 5
-1 3 5
-1 4 4
-1 2 6
2 2 3
-1 2 2 4
so the output should be the count of unique combinations which is 9
input:  2 4 6 1 3
         6
output:  3
Note: Dont use permutations and combiations method'''
##import itertools
##mylist = [-1,4,5,6,7,8,2,4,5,2,3,8]
##list2 = []
##list3 = []
##list4 = []
##def my_function(mylist,r):
##    if r == 0:
##        return[[]]
##    list2 = []
##    for i in range(len(mylist)):
##        m = mylist[i]
##        y = mylist[i+1:]
##        comblist = my_function(y,r-1)
##        for x in comblist:
##              list2.append([m]+x)
##    return list2
##list3 = []
##for i,j in enumerate(mylist):
##    print(i,j)
##    list3.append(my_function(mylist,i))
##
##for t in list3:
##    for m in t:
##        if sum(m)==7 and m not in list4:
##            list4.append(m)
##            print(m)
        
    
##for i in range(len(mylist)):
##    y = mylist[:i]+mylist[i+1:]
##    for j in range(len(y)):
##        x = y[:j]+y[j+1:]
##        if x not in list2:
##            list2.append(x)
##        for k in range(len(x)):
##            z = x[:k]+x[k+1:]
##            if z not in list2:
##                list2.append(z)
##            for b in range(len(z)):
##                l = z[:b]+z[b+1:]
##                if l not in list2:
##                    list2.append(l)
##    list2.append(y)
##count = 0
##for i in list2:
##   if sum(i)==6 :
##       print(i)
##       count+=1
##print(count)








