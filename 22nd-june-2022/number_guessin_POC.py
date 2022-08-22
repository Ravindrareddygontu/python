import random
a=1
b=2
num = random.randint(1,100)
user_num = int(input("enter number: "))
while user_num != num:
    user_num = int(input("enter a number: "))
    if user_num>num:
        print("number is greater enter small number")
    if user_num<num:
        print("number is small enter big number")
    
print("correct number")
