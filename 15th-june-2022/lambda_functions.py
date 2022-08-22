'lambda functions'
"1.lambda functions are one line anonymous functions which is used for quick use in the program and mostly these are used in higher order functions"

##n = lambda x : print(x*2)
##n(5)


##n = lambda x,y = 6 : x+y
##print(n(8))#x takes 8


'2.map_function_exercises.pylambda using in functions'
##def lam():
##    return lambda x,n : print(x+n)
##    
##fun = lam()
##print(fun(5,6))

'3.lambda in lambda'
##n= lambda x :lambda y:print(x+y)
##k =n(3)
##print(k(4))

'4.higher order functions'
"map"
##mylist = [2,3,4,5,6,7,8]
##
##add = list(map(lambda x : x*2,mylist))
##
##print(add)

"5.filter"
##mylist = [2,3,4,5,6,7,8]
##
##evens = list(filter(lambda x : x%2 == 0,mylist))
##
##print(evens)

"6.reduce"
##from functools import reduce
##
##mylist = [2,3,4,5,5]
##
##compress = reduce(lambda x,y : x*y,mylist)
##print(compress)

'common exercises by lambda'

"7.looping over lambda"
##my_dict = {1,2,3,4}
##
##x = lambda x:x+2
##
##for i in my_dict:
##    
##    print(x(i))

"8.map function does it will iterate through every element and manupulate data with a given condition"

##mylist = [2,3,4,5,6,7,8]
##
##add = list(map(lambda x : x*2,mylist))
##
##print(add)


'9.2tripling the list'
##nums = (1, 2, 3, 4, 5, 6, 7) 
##print("Original list: ", nums)
##result = list(map(lambda x: x + x + x, nums))
##print(result)

'10.3adding three list elements'
##nums1 = [1, 2, 3] 
##nums2 = [4, 5, 6] 
##nums3 = [7, 8, 9]
##
##total = list(map(lambda x,y,z : x+y+z,nums1,nums2,nums3))
##print(total)

'11.adding list itself'

##my_list = [2,3,4,5,6]
##
##newlist = list(map(lambda x,y:x+y,my_list,my_list))
##
##print(newlist)

'12.counting the same pairs in given lists'
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

'13.separating  evens and odds'
##nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
##evens = list(filter(lambda i: i%2 == 0,nums))
##
##odds = list(filter(lambda i: i%2 != 0,nums))
##
##print(evens)
##
##print(odds)


'14.concatinating two lists'
##nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
##x = lambda x,y : x+y
##
##print(x(nums,nums2))

'15.squares and cubes of list'
##nums = [1,3,4,6,2,12,10]
##
##squares = list(map(lambda x : x**2 , nums))
##
##cubes = list(map(lambda x : x**3,nums))
##
##print(squares)
##
##print(cubes)


'16.checking string starting with certain character'
##string = "reddy"
##
##capital = lambda x: True if x[0]=="r" else False
##
##print(capital(string))

'17.finding intersection of two given lists'
##array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
##array_nums2 = [1, 2, 4, 8, 9]
##
##intersection = list(filter(lambda x: x in array_nums1,array_nums2))
##
##print(intersection)

'18.sorting list'
##mylist = [-1, 2, -3, 5, 7, 8, 9, -10]
##
##result = sorted(mylist, key = lambda i: 0 if i == 0 else -1/i)
##
##print(result)

'19.printing string having given length'
##weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
##
##highest = filter(lambda day:len(day)==6 ,weekdays)
##
##print(list(highest))

'20.finding palindromes in a list'
##texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
##
##palin = list(filter(lambda x : x[::-1]==x,texts))
##
##print(palin)























































































































































































