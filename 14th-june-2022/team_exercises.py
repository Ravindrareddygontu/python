'1 write a program to print the kth largest number in the list'
##a = [2,3,4,5,-2,3,-1,8]
##b = 2
##sort = a.sort()
##print(a)
##
##k = a[-b]
##
##print(k)


'2 write a function with name sum of cubes a to b that takes two integers and sum of the cubes from a to b'
##def sum_of_cubes(a,b):
##    sum = 0
##    for i in range(a,b):
##        sum = sum +i**3
##    print(sum)
##
##first = 3
##second = 5
##sum_of_cubes(first,second)




'3 write a program to remove duplicates numbers'
##my_list = [2,2,3,4,5,5,4,6,3,5]
##list2 = []
##for i in my_list:
##    if i not in list2:
##        list2.append(i)
##
##print(list2)


'4 write a program tht given function will return the second character in the word passed to the function'
##def my_function(string):
##    return string[1]
##
##string = "reddy"
##second = my_function(string)
##print(second)


'5 write a program to remove n key-value pairs from the dictionary if they present'
##mydict = {"add":"update","remove":"popitem","give":"get"}
##n = int(input("enter a index: "))
##count = 0
##
##for i in mydict:
##    
##    if n == count:
##        mydict.pop(i)
##        print(mydict)
##        break
##    count = count+1
##else:
##    print("given index is not in a dictionary")


