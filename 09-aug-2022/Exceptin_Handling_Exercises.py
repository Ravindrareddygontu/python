##tryExcept'''

##a = 10
##b = 0
##
##try:
##    d = a/b
##    print(d)
##    print('Inside Try')
##
##except ZeroDivisionError:
##    print('Division by Zero Not allowed')
##
##print('Rest of the Code')

'''2. TryExceptElse'''
##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##    print("Inside Try")
##except ZeroDivisionError:
##    print("Division by Zero not allowed")
##else:
##    print("Inside Else")
##print("rest of the code")

'''3. TryExceptElseFinally '''
##a=10
##b=9
##try:
##    d=a/b
##    print(d)
##    print("try block")
##except ZeroDivisionError:
##    print("'Division by Zero Not allowed'")
##
##
##else:
##    print("Inside else")
##finally:
##    print("final block")
##print("rest of the code")


'''except obj'''
##a=10
##b=0
##try:
##    d=a/b
##    print(d)
##    print('inside try')
##
##except ZeroDivisionError as obj:
##    print(obj)
##print("rest of the code")



'''5. ExceptMultiple1'''


##a = 10
##b = 9
##try:
##    d = a/b
##    print(d)
##    
##except ZeroDivisionError as obj:
##    print(obj)
##    
##except NameError as ob:
##    print(ob)
##
##print('Rest of the Code')

'''ExceptMultipl'''

##a = 10
##b = 25
##try:
##    d = a/b
##    print(d)
##    
##except (NameError, ZeroDivisionError) as obj:
##    print(obj)
##
##print('Rest of the Code')


'''7. Except (2)'''
##a = 10
##b = 0
##try:
##    d = a/b
##    print(d)
##    
##except:
##    print('Exception Handler')
##
##print('Rest of the Code')


'''8. AssertStatement'''
##a=20
##assert a<=10,"invalid number"




'''9. CustomeException'''
##class Balance_Exception(Exception):
##    def __init__(self,arg):
##        self.msg=arg
##def check():
##    money=10000
##    withdraw=9000
##    try:
##        balance=money-withdraw
##        print(balance)
##        if(balance <=2000):
##            raise Balance_Exception("insufficient balance")
##    except Balance_Exception as be:
##            print(be)
##        
##
##check()
