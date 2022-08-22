'append()'
##list = [1,2,3,4]
##list.append(2)
##print(list)
##list.append([3,2,1])#adding list
##print(list)

'clear()'
"it takes no arguments"
##list = ["name","age","gender"]
##list.clear()
##print(list)

'count()'
"it will count the number of occurances of given value"
##list = [4,5,3,5,3,4,5,2]
##print(list.count(4))
##print(list.count(5))

'copy()'
"it will create the another list,it is shallow copy"
##list = [5,6,4,3,5]
##list2 = list.copy()
##list[0] = 89#it will not modify the copied list(list2)
##print(list2)

'extend()'
"it adds the elements in the last"
##list = ["apple","banana","cherry"]
##list2 = ["papaya","mango","sundar"]
##list.extend(list2)
##print(list)

'index()'
##"it will return the first occurance of the given value"
##list = ["list","tuple","dict","list","tuple"]
##print(list.index("list"))
##print(list.index("tuple"))

'insert()'
"add an element to the given index it takes two arguments first is index second is value"
##list = [1,2,3,4,5]
##list.insert(3,23)
##list.insert(0,[4,5,6])
##print(list)

'pop()'
"it takes an index as an its one argument of specified value"
##list = ["remove","insert","index","extend"]
##list.pop()#it removes last element by default
##list.pop(0)
##print(list)

'remove()'
"it takes a value as an its one argument and remove first occurance of it"
##list = ["append","extend","index","insert","extend"]
##list.remove("append")
##list.remove("extend")
##print(list)


'reverse()'
"it takes no parameters"
##list = ["insert","index","append","remove","extend"]
##list.reverse()
##print(list)

'sort()'
"it sort the items in ascending order"
##list = ["insert","extend","remove","index"]
##list.sort()
##list2 = [1,6,23,54,3,12]
##list2.sort()
##
##print(list)
##print(list2)
