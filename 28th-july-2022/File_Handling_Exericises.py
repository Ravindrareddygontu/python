#1.WAP to replace all words "the" by another word "them" in a file "poem.txt"
'''f=open("poem1.txt",mode="r")
d=f.read()
d=d.replace("the","them")
f.close()
f=open("poem1.txt",mode="w")
f.write()
f.close()'''


#2.WAP to replace a character by another character in a file "story.txt".(Accept both the characters from the user)

'''f=open("story.txt","r")
d=f.read()
ch=input("enter a character to be replaced")
ch1=input("enter a character that will replaced")
d=d.replace(ch,ch1)
f.close()
f=open("story.txt","w")
f.write()
f.close()'''


#3.WAP to replace all the 'a' by '@' in a file "data.txt".

'''f=open("data.txt","r")
d=f.read()
d=d.replace('a','@')
f.close()
f=open("data.txt","w")
f.write()
f.close()'''


#4.WAP to read file "data.txt" and display only those lines whose lenght is more than 40 characters.

'''f=open("data.txt")
d=f.readlines()
for i in d:
    if len(i)>40:
        print(i)'''
        
#5.WAP to remove all duplicate lines from the file "story.txt"

'''f=open("story.txt","r")
d=f.readlines()
m=[]
for i in d:
    if i not in m:
        m.append(i)
print(i)
f.close()
f=open("story.txt","w")
for i in m:
    f.write(i)
    f.close()'''

#6.WAP to display only unique words from the file "story.txt"

'''f=open("story.txt","r")
d=f.read()
d=d.split()
str=""
m=[]
for i in d:
    if i not in str:
        str=str+i
        print(i,end="")
f.close()'''


#7.WAP to count the frequency of each vowels in a file "task.txt"

'''f=open("task.txt","r")
d=f.read()
va=ve=vo=vu=vi=0
for i in d:
    if i=='a' or i=='A':
        va=va+1
    if i=='e' or i=='E':
        ve=ve+1
    if i=='i' or i=='I':
        vi=vi+1
    if i=='u' or i=='U':
        vu=vu+1
    if i=='o' or i=='O':
        vo=vo+1
print("frequency of vowel\"a\"is",va)
print("",ve)
print("",vi)
print("",vo)
print("",vu)'''


#8.WAP to count those words whose lenght is more than 7 characters in a file "story.txt"

'''f=open("story.txt","r")
d=f.read()
d=d.split()
c=0
for i in d:
    if len(i)>7:
        c=c+1
print("total words are:",c)'''


#9.WAP to count those lines from the file "div.txt" which are starting from 'T' or 'M'.

'''f=open("div.txt","r")
d=f.readlines()
c=0
for i in d:
    if i[0]=='M' or i[0]=='T':
        c=c+1
print("total lines are:",c)'''


#10.WAP to count those lines from the file "div.txt" which are not starting from 'M'.


'''f=open("div.txt")
d=f.readlines()
c=0
for i in d:
    if i[0]!='M':
        c=c+1
print("total lines are:",c)'''


#11.WAP to display those words from a file "image.txt" which are ending from alphabet 'm'.

'''f=open("image.txt")
d=f.read()
d=d.split()
c=0
for i in d:
    if i[-1]=='m':
        c=c+1
print("total words are:",c)'''

#12.WAP to read all lines of file "data.txt" using readline() only.

'''f=open("data.txt","r")
str=""
while str:
    str=f.readline()
    print(str,end="")
f.close()'''

#13.WAP to copy the entire content from file "data.txt" to "story.txt".

'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.read()
f1.write(d)
f.close()
f1.close()'''


#14.WAP to copy the alternate lines from file "data.txt" to "story.txt".

'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.readlines()
for i in range(len(d)):
    if i%2==0:
        f1.write(d[i])
f.close()
f1.close()'''

#15.WAP to read the entire content from file "data.txt" and copy the contents to "story.txt" in upper case.

'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.readlines()
for i in d:
    f1.write(i.upper())
f.close()
f1.close()'''

#16.WAP to read the entire content from file "data.txt" and copy only those words to "story.txt" which start from vowels.


'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.read()
d=d.lower()
word=d.split()
for i in word:
    if i[0] in ['a','e','i','o','u']:
        f1.write(i)
f.close()
f1.close()'''


#17. Write a program in Python to read the entire content from file “data.txt” and copy only those words in separate lines to “story.txt” which are starting from lower case alphabets .

'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.read()
d=d.lower()
word=d.split()
for i in word:
    if i[0].islower():
        f1.write(i)
        f1.write("\n")
f.close()
f1.close()'''

#18.. Write a program in Python to read file “data.txt” and copy only those lines to “story.txt” which are starting from alphabets “A” or “T”.

'''f=open("data.txt","r")
f1=open("story.txt","w")
d=f.readlines()
for i in d:
    if i[0]=="A" or i[0] == "T":
        f1.write(i)
f.close()
f1.close()'''

#19.Write a program in Python which display the longest word from file “star.txt”

'''f=open("data.txt","r")
d=f.read()
l=d.split()
longword=""
for i in l:
    if len(i)>len(longword):
        longword=i
print("longest word is",longword)
f.close()'''

#20.Write a program in Python which display the longest line from file “star.txt”


'''f=open("data.txt","r")
d=f.readlines()
longline=""
for i in d:
    if len(i)>len(longline):
        longline=i
print("longline is",longline)
f.close()'''

#21.Write a program in Python to read the file “star.txt” and display the entire content after removing leading and trailing spaces.

'''f = open("data.txt", "r")
d = f.readlines()
for i in d:
    print(i.strip())
f.close()
'''

#22.Write a program in python that read the content from file “sumit.txt” and display all numbers.

'''f=open("sum.txt","r")
d=f.read()
for i in d:
    if i.isdigit():
        print(i)
f.close()
'''

#23.Write a program in Python that display the second and second last line from the file “data.txt”

##f=open("life.txt","r")
##d=f.readlines()
##print("Second line is :",d[1])
##print("Second last line is :",d[-2])
##f.close()
##s


'''25.Write a menu driven program which shows all operations on Binary File 

Add Record 

Display All Record 

Display Specific Record 

Modify Record 

Delete Record 

Use “data.dat” file which stores the record of “Hotel” in the form of list containing Room_no, Price, Room_type'''

##with open('data.dat','w') as f:
##    for i in range(10):
##        m = f.write(f'\nroom no is {i}\n price is {20000}\n room_type is AC room')
##
##lst = []
##lst2 = []
##k = i
##def display():
##    with open('data.dat','r') as f:
##        for j in range(10):
##            for i in f.readlines(50):
##                lst.append(i.strip())
##            lst2.append(lst)
##            lst = []
##    print(lst2)
##
##    
##def add(roomno, price):
##    record = f'\nroom no is {roomno}\n price is {price}\n room_type is AC room'
##    lst2.append(record.strip())
##    with open('data.dat','a') as f:
##        f.write(record)
##
##
##add(20,3000)
##
##def del(record):
##    lst2.pop(record)




'''26.Write a function disp75() in Python to display only those records of students from file “school.dat” who scored more than 75 percent marks.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]''' 

##lst = 25,'ravin',10,'80'
##lst2 = 12,'reddy',10,'90'
##with open('school.dat','w') as f:
##    f.write(f"25,'ravin',10,'80'\n""12,'reddy',10,'90'")
##
##def disp(r):
##    with open('school.dat','r') as f:
##        n = f.readlines()
##        print(n)
##        for i in n:
##            lst = i.split(',')
##            j = lst[3]
##            if int(lst[3][1:3])>(r):
##                print(i)
##
##disp(70)
    



'''27.Write a function dispname() in Python which will display only names of all the students from file “school.dat”. Structure stored in “school.dat”
is in the form of list containing information like [rollno, name, class, percentage]''' 

##lst = 25,'ravin',10,'80'
##lst2 = 12,'reddy',10,'90'
##with open('school.dat','w') as f:
##    f.write(f"25,'ravin',10,'80'\n""12,'reddy',10,'90'")
##
##def dispname():
##    with open('school.dat','r') as f:
##        n = f.readlines()
##        for i in n:
##            lst = i.split(',')
##            print(lst[1])
##dispname()
    






'''28.Write a function disp12() in Python which will display records of class 12th students from file “school.dat”.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]''' 
##lst = 25,'ravin',10,'80'
##lst2 = 12,'reddy',10,'90'
##with open('school.dat','w') as f:
##    f.write(f"25,'ravin',10,'80'\n""12,'reddy',10,'90'")
##
##def disp12():
##    with open('school.dat','r') as f:
##        n = f.readlines()
##        for i in n:
##            lst = i.split(',')
##            if lst[3]==12:
##                print(lst)
##disp12()




'''29.Write a function search(name) in Python which will display record of a student from file “school.dat” whose name is passed as an argument.
Structure stored in “school.dat” is in the form of list containing information like [rollno, name, class, percentage]''' 
##lst = 25,'ravin',10,'80'
##lst2 = 12,'reddy',10,'90'
##with open('school.dat','w') as f:
##    f.write(f"25,'ravin',10,'80'\n""12,'reddy',10,'90'")
##
##def disp12(name):
##    with open('school.dat','r') as f:
##        n = f.readlines()
##        for i in n:
##            lst = i.split(',')
##            if lst[2]==name:
##                print(lst)
##disp12('ravin')




'''30.Write a function disp_mob(model no.) in Python which will display the record of a mobile from “mobile.dat” whose model number (integer type) is
passed as an argument. Structure of “mobile.dat” is [Mobile id, Mobile brand, Model No., Price]'''
##lst = 25,'ravin',10,'80'
##lst2 = 12,'reddy',10,'90'
##with open('school.dat','w') as f:
##    f.write(f"25,'ravin',10,'80'\n""12,'reddy',10,'90'")
##
##def disp12():
##    with open('school.dat','r') as f:
##        n = f.readlines()
##        for i in n:
##            lst = i.split(',')
##            if lst[3]==12:
##                print(lst)
##disp12()







