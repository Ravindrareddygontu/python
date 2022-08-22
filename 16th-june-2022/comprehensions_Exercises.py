'comprehensions'

'1.list by range()'
##mylist = [i for i in range(10)]
##
##print(mylist)

'2.list by range() with condition'
##mylist = [i for i in range(10) if i%2==0]
##
##print(mylist)


'3.listing two elements by range'
##mylist = [(i,j) for i in range(10) for j in range(10) if i==j]
##print(mylist)

'4.finding permutations'
##string = "abc"
##
##string2 = [(a,b,c) for a in string for b in string for c in string]
##
##for i in string2:
##
##    print(str(i))

'5.creating dict'
##string = "abc"
##
##values = 12
##
##mydict = dict([(i,values) for i in string])
##
##print(mydict)

'6.dict with key and double of it is value'

##mydict = {i:i*i for i in range(10)}
##
##print(mydict)


'7,creating set'
##mylist = ["append","update","extend","discard"]
##
##myset = {i for i in mylist}
##print(myset)

'8.finding length of each string in list'
##mylist = ["discard","fromkeys","maketrans","subset"]
##
##length = [len(i) for i in mylist]
##
##print(length)

'9.creating dict by enumerate()'
##string = "ravindra"
##
##mydict = {i:j for i,j in enumerate(string)}
##
##print(mydict)

'10.creating set by two elements'
##myset = {(i,j) for i in range(3,8) for j in range(7,9)}
##
##print(myset)














































