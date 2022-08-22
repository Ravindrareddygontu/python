'1.Write a python program in fibonacci series using generator'
##def fib(n):
##    p,q = 0,1
##    while p<n:
##        yield p
##        p,q = q,q+p
##
##n = 6
##for i in fib(n):
##    print(i)


'2.Write a python program to generate the running product of the elemnts of a given iterable'
##def pro(tup):
##    n = 1
##    for i in tup:
##        n *= i
##        print(n)
##
##tup = (1,2,3,4,5,6)
##print(f"running product of a tuple is: ",tup)
##lst = [1,2,3,4,5,6]
##pro(lst)
##pro('running produt of a list is: ',lst)




'3.factorial using iterators'

##def fact():
##    a = 1
##    for i in range(1,10):
##        a *= i
##        yield a
##        
##k = 7
##for i in range(k):
##    for j in fact(i):
##        print(j)
      
'4.Write a simple registeration form which contains input buttons heading and radio buttons by using tkinter module'
##from tkinter import*
##root = Tk()
##root.geometry('500x500')
##root.title("Registration Form")
##
##label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
##label_0.place(x=90,y=53)
##
##
##label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
##label_1.place(x=80,y=130)
##
##entry_1 = Entry(root)
##entry_1.place(x=240,y=130)
##
##label_2 = Label(root, text="Email",width=20,font=("bold", 10))
##label_2.place(x=68,y=180)
##
##entry_2 = Entry(root)
##entry_2.place(x=240,y=180)
##
##label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
##label_3.place(x=70,y=230)
##var = IntVar()
##Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
##Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
##
##label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
##label_4.place(x=70,y=280)
##
##
##entry_2 = Entry(root)
##entry_2.place(x=240,y=280)
##
##Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
### it is use for display the registration form on the window
##root.mainloop()
##print("registration form  seccussfully created...")



'5.prime progam using sys module'
##import sys
##
##for i in sys.stdin:
##    if i.strip() == i.isdigit():
##        print('you entered wrong')
##        break
##    else:
##        for j in range(2,int(i)):
##            if int(i)%j==0:
##                print('this is not a prime')
##                break
##        else:
##            print('this is a prime')
            













