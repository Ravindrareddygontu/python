'recursive function'
"the function calling itself inside the function is called recursive function"

'finding factorial'
##def my_function(num):
##    if num == 1:
##        return num
##    else:
##        return num * my_function(num-1)
##    
##fact = my_function(5)
##print(fact)

'adding of natural numbers'

##def add(n):
##    if n==1:
##        return n
##    else:
##        return n + add(n-1)
##
##natural = add(10)
##print(natural)

'adding list'
##def list_add(mylist):
##    total = 0
##    for element in mylist:
##        if type(element) == type([]):
##            total = total + list_add(element)
##        else:
##            total = total + element
##    return total
##
##mylist = [1,3,4,[4,5],[8,6]]
##list2 = list_add(mylist)
##print(list2)

'global variable'
##'global variable'
##a = 9
##def my_var():
##    global a
##    a = 8
##    print(a)
##
##my_var()
##print(a)



























