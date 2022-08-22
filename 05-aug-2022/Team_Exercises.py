'1) write a program on magical method add , pos and neg?'
##class Magic:
##    def __init__(self,name):
##        self.name = name
##        
##    def __add__(self,other):
##        return self.name+other.name
##
##    def __pos__(self):
##        return self.name
##
##    def __neg__(self):
##        return self.name[:4]
##
##obj = Magic('ravindra')
##obj2 = Magic('reddy')
##
##print(obj+obj2)#it defaultly uses __add__ method
##print(+obj)
##print(-obj)


'2) write a program convert day number to date in particular year?'
##from datetime import datetime
##
##day = '34'
##s = day.rjust(3+len(day),'0')
##year = '2020'
##d = datetime.strptime(year+'-'+day,'%Y-%j').strftime('%d-%m-%Y')
##print(d)



'3) write a dictionary to a file in python?'
##dic = {1:'rag',2:'mag',3:'nag'}
##with open('dic.txt','w') as f:
##    f.write(f'{dic}')




'4) find the most repeated word in a text file?'
##from collections import Counter
##
##with open('data.txt','w') as f:
##    f.write('welcome to the world and hello to the people and welcome them to the century')
##
##    
##with open('data.txt', 'r') as f:
##    r = f.read()
##    c = Counter(r)
##    print(c.most_common(2))







'''5) write a program on sprial number?

eg:-1 2 3
    8 9 4
    7 6 5'''
##n = 1
##order = [0,1,2,5,8,7,6,3,4]
##lst = [1,2,3,4,5,6,7,8,9]
##for i in order:
##    lst[i]=n
##    n+=1
##print(lst)
##
##m = 0
##for i in lst:
##    print(i,end=" ")
##    m+=1
##    if m%3==0:
##        print()








