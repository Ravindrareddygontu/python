'1) WAPP to reverse internal content of every second word present in the given String.'
##string = "ravindra reddy rakesh ganta"
##mylist = string.split(" ")
##string2 = ""
##
##for i in range(len(mylist)):
##    if i%2 !=0:
##        string2 = string2 + mylist[i][::-1]+" "
##    else:
##        string2 = string2 + mylist[i]+" "
##
##print(string2)
##    

'''2) WAPP for the following requirements
    input->a3z2b4
    output->aaabbbbzz(sorted string).'''

##string = "a3z2b4"
##count = 0
##string2 = ""
##string3 = ""
##for i in string:
##    if i.isdigit():
##        string2 = string[count-1]*int(i)
##        string3 =string3+string2
##    count +=1
##    
##mylist = sorted(string3)
##string4 = "".join(mylist)
##print(string4)
    


'3)WAPP  to extract year ,month,date and time using lambda Function.'
##import datetime
##
##current = datetime.datetime(2022,6,17)
##print(current)
##
##year = lambda x:x.year
##month = lambda x:x.month
##day = lambda x:x.day
##
##print(year(current), month(current), day(current))




'4)WAPP to find the values of length six in given list of week days using lambda Function.'
##weekdays = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
##
##length =  list(filter(lambda x : x if len(x)==6 else 0, weekdays))
##
##print(length)




'5)WAPP to find factorial of number using closure Function.'
##def my_function(num):
##    fact =  1
##    def factorial(fact):
##        for i in range(1,num+1):
##            fact = fact*i
##        return fact
##    return factorial(fact)
##
##number = 5
##final = my_function(number)
##print(final)






























    










