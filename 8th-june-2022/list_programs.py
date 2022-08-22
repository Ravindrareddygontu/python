'''1.Take 10 integer inputs from user and store them in a list and print them on screen.'''
##list = []
##for i in range(10):
##    numbers = int(input("enter: "))
##    list.append(numbers)
##print(list)


'''2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
( Iterate over list using while loop ).'''
##list = []
##i = 0
##while i<10:
##    nums = int(input("enter: "))
##    list.append(nums)
##    i = i+1
##print(list)
##enter = int(input("enter check number: "))
##if enter in list:
##    print("given is in list")
##else:
##    print("given number not found in list")


'''3.
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s.'''
##list = []
##i = 0
##while i<20:
##    print("enter ",i," st value")
##    nums = int(input(">: "))
##    list.append(nums)
##    i = i+1
##print(list)
##pos,neg,odd,even,zero = 0,0,0,0,0
##for iter  in list:
##    if iter == 0:
##        zero += 1
##    elif iter<0:
##        neg += 1
##    elif iter%2 == 0:
##        even += 1
##        pos += 1
##    else:
##        iter%2 != 0
##        odd +=1
##        pos += 1
##print(f"positives are {pos}, negatives are {neg}, odds are {odd}, evens are {even}, zeros are {zero}")
##        
    
        



'''4.Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.'''
##list = []
##i = 0
##while i<10:
##    nums = int(input("enter: "))
##    list.append(nums)
##    i +=1
##print(list)
##list2 = []
##for i in reversed(list):
##            list2.append(i)
##print(list2)

               

'''5.Write a program to find the sum of all elements of a list.'''
##list = [1,2,3,4]
##add = 0
##for i in list:
##    add = add + i
##print(add)




'''6.Write a program to find the product of all elements of a list.'''
##list = [1,2,3,4]
##product = 1
##for i in list:
##    product *=i
##print(product)





'''7.Initialize and print each element in new line of a list inside list.'''
list = [[1,2],[4,5,7],[6,8,9]]
for i in list:
    for j in i:
        print(j)
    
        

'''8.Find largest and smallest elements of a list.'''
##list = [3,45,23,1,56,12,15]
##max = 0
##for i in list:
##    if i > max:
##        max = i
##min = max
##for i in list:
##    if i<min:
##        min =i
##print(min,max)




'''9.Write a program to print sum, average of all numbers, smallest and largest element of a list.'''
##list = [3,4,23,12,34,2,6,78,43]
##avg = len(list)
##average = sum(list)//avg
##add = sum(list)
##small = min(list)
##large = max(list)
##print(f"sum of list is {add}, average of list is {average}, smallest of list{small}, largest of list is {large}")




'''10.Write a program to check if elements of a list are same or not it read from front or back. E.g.-
2	3	15	15	3	2'''
##list = [2,3,15,15,3,2]
##list2 = []
##for i in reversed(list):
##    list2.append(i)
##print(list2)
##if list2 == list:
##    print("same elements ")
##else:
##    print("not same elements")




'''11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78
After spliting :
58	24	13	15	63
9	8	81	1	78'''
##list = [58,24,13,15,63,9,8,82,1,78]
##length = len(list)
##middle = length//2
##list1 = list[:middle]
##list2 = list[middle:]
##print(list1,list2)





'''12.
Ask user to give integer inputs to make a list. Store only even values given and print the list.'''
##list = []
##for i in range(8):
##    num = int(input("enter: "))
##    if num % 2 == 0:
##        list.append(num)
##print(list)
