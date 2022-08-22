'''create a banking application,to check current balance,to deposite,to withdraw.

account class
atributes-name,balance,min_balance
methods-deposite,withdraw,printstatement

currentaccount class.....currentaccount balance
atributes-name,balance
methods- __str__
give min_balance


saving account class.....currentaccount balance
atributes-name,balance
methods- __str__

deposit rs.5000 in saving account
withdraw rs.7000 from saving

input:
1.print current balance
2.print current balance after deposit-5000
3.print current balance after withdraw-10000
4.withdraw 6000 rupees

output:
1.print current balance 10000
2.print current balance after deposit-15000
3.print current balance after withdraw-5000
4.insufficient balance'''
class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,add):
        self.balance = self.balance+add
        print('balance after deposit: ',self.balance)

    def withdraw(self,minus):
        if minus<self.balance:
            self.balance = self.balance-minus
            print('balance after withdraw: ',self.balance)
        else:
            print('insufficient balance')
            
    def printstatement(self):
        pass

class Saving(Account):
    def __str__(self):
        pass
    
obj = Saving('ravi',10000,500)
obj.deposit(2000)
obj.withdraw(10000)
obj.withdraw(3000)



        






