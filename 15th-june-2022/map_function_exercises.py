'1map()'
"map function does it will iterate through every element and manupulate data with a given condition"

##mylist = [2,3,4,5,6,7,8]
##
##add = list(map(lambda x : x*2,mylist))
##
##print(add)


'2tripling the list'
##nums = (1, 2, 3, 4, 5, 6, 7) 
##print("Original list: ", nums)
##result = list(map(lambda x: x + x + x, nums))
##print(result)

'3adding three list elements'
##nums1 = [1, 2, 3] 
##nums2 = [4, 5, 6] 
##nums3 = [7, 8, 9]
##
##total = list(map(lambda x,y,z : x+y+z,nums1,nums2,nums3))
##print(total)

'4string word  to list'
##color = ['Red', 'Blue', 'Black', 'White', 'Pink']
##
##my_list = list(map(list,color))
##
##print(my_list)

'5.string words to set'

##color = ['red','blue','black','white','pink']
##
##my_set = list(map(set,color))
##
##print(my_set)

'6.list1 powers list2 '
##bases_num = [10, 20, 30, 40]
##
##index = [1, 2, 3, 4]
##
##my_list = list(map(pow, bases_num,index))
##
##print(my_list)

'7.function as argument'
##def my_function(num):
##    num = num*2
##    return num
##
##num = [4,5,6,7]
##my_list = list(map(my_function,num))
##print(my_list)

'8.returns list of upper and lowercase of given string'
##def change_cases(s):
##  return str(s).upper(), str(s).lower()
## 
##chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
##
##my_list = list(map(change_cases , chars))
##
##print(my_list)

'9.counting the same pairs in given lists'
##nums1 = [1,2,3,4,5,6,7,8]
##nums2 = [2,2,3,1,2,6,7,9]
##
##k = list(map(lambda x:x*2,nums1))
##
##j = set(map(lambda y: y*2,nums2))
##
##print(k)
##
##print(j)

'10.counting same pairs in list'
##from operator import eq
##def count_same_pair(nums1, nums2):
##    result = sum(map(eq, nums1, nums2))
##    return result
##
##nums1 = [1,2,3,4,5,6,7,8]
##nums2 = [2,2,3,1,2,6,7,9]
##print("Original lists:")
##print(nums1)
##print(nums2)
##print("\nNumber of same pair of the said two given lists:")
##print(count_same_pair(nums1, nums2))

'11.map funtion in funtion'
##def strings_to_listOflists(str):
##    result = map(list, str)
##    return list(result)
##
##colors = ["Red", "Green", "Black", "Orange"]
##
##print("\nConvert the said list of strings into list of lists:")
##
##print(strings_to_listOflists(colors))

'12.adding and substracting lists'
##def my_function(a,b):
##    return a+b , a-b
##
##
##nums1 = [6, 5, 3, 9]
##nums2 = [0, 1, 7, 7]
##
##my_list = list(map(my_function,nums1,nums2))
##
##print(my_list)

'13.adding list itself'

##my_list = [2,3,4,5,6]
##
##newlist = list(map(lambda x,y:x+y,my_list,my_list))
##
##print(newlist)

'14.creating dict'

##def my_function(x,y):
##    return x+":"+y
##
##my_list = ["first","second","third","four"]
##
##my_list2 = ["one","two","three"]
##
##mydict = list(map(my_function,my_list,my_list2))
##
##print(dict.fromkeys(mydict,my_list))

'15.adding list and tuple'
##def myMapFunc(list1, tuple1):
##    return list1+"_"+tuple1
##
##my_list = ['a','b', 'b', 'd', 'e']
##my_tuple = ('PHP','Java','Python','C++','C')
##
##updated_list = map(myMapFunc, my_list,my_tuple)
##print(updated_list)
##print(list(updated_list))


























































































































