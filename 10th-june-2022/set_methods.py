'add()'
"it takes only one argument and if already element exist it will not add the element"
##setlist = {1,2,3,4,7,5}
##setlist.add(6)
##setlist.add(2)
##print(setlist)

'clear()'
##setlist = {1,2,3,2,5}
##setlist.clear()
##print(setlist)#it doesn't throws an error

'copy()'
##fruits = {"apple", "banana", "cherry"}
##
##x = fruits.copy()
##
##print(x)

'difference()'
"it will remove the common elements in the second set"
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.difference(y)#it will return all different elements not in y
##a = y.difference(x)
##
##print(z)
##print(a)

'intersection_update'
"it will return all common elements in all given sets"
##x = {"a", "b", "c"}
##y = {"c", "d", "e"}
##z = {"f", "g", "c"}
##
##x.intersection_update(y, z)
##
##print(x)

'isdisjoint()'
"returns true or false if first elements are common in second set elements"
##first = {'first','second','third'}
##
##second = {'four','five','six'}
##
##print(first.isdisjoint(second))#it returns true

'discard()'
"it will remove the given element it doesn't throws an error while remove not"
##fruits = {"apple", "banana", "cherry"}
##
##fruits.discard("banana")
##
##print(fruits)

'intersection()'
"it will return the common elements in given sets and creates new set"
##x = {"a", "b", "c"}
##y = {"c", "d", "e"}
##z = {"f", "g", "c"}
##
##result = x.intersection(y, z)
##
##print(result)

'intersection_update()'
"it will delete uncommon elements from the list"
##x = {"a", "b", "c"}
##y = {"c", "d", "e"}
##z = {"f", "g", "c"}
##
##result = x.intersection_update(y, z)#it returns none
##
##print(result)

'issubset()'
"returns true if all elements in present in another list"
##x = {"a", "b", "c"}
##y = {"f", "e", "d", "c", "b", "a"}
##
##z = x.issubset(y)#it returns true
##k = y.issubset(x)#it returns false
##
##print(z)
##print(k)

'issuperset()'
"returns true if all elements are in subset are in superset "
##superset = {1,2,3,4,5,6}
##
##sub = {1,2,3}
##
##print(superset.issuperset(sub))
##
##print(sub.issuperset(superset))#it returns false

'pop()'
"removes a random element and takes no argument"
##fruits = {"apple", "banana", "cherry"}
##
##remove = fruits.pop()
##
##print(fruits)
##print(remove)

'remove()'
'''it removes specific element in a set and if no element
is present it throws an error discard also done same but not throws an error'''
##setlist = {"ferry","is","useful"}
##
##setlist.remove("is")
##
##print(setlist)

'symmentric_difference()'
"returns all elements except common elements"
##x = {"apple", "banana", "cherry"}
##
##y = {"google", "microsoft", "apple"}
##
##z = x.symmetric_difference(y) 
##
##print(z)#return all except 'apple'

'symmentric_difference_update()'
'''The symmetric_difference_update() method updates the original set
by removing items that are present in both sets, and inserting the other items.'''
##x = {"apple", "banana", "cherry"}
##
##y = {"google", "microsoft", "apple"}
##
##x.symmetric_difference_update(y)
##y.symmetric_difference_update(x)
##
##print(x)
##
##print(y)

'union()'
"it returns all elements but not duplicates from both of sets"
##x = {"apple", "banana", "cherry"}
##y = {"google", "microsoft", "apple"}
##
##z = x.union(y)
##k = y.union(x)
##
##print(z)
##
##print(k)

'update'
##setlist = {'discard','pop','union','difference','disjoint','intersection'}
##
##setlist2 = {'clear','copy','issubset'}
##
##x = setlist.update(setlist2)
##
##print(setlist)

##lis = [45,65]
##set = {1,2,'gsai',7,'rt',lis}
##print(set)
