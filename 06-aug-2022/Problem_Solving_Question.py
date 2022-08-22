'''write a python program on sprial number using inner function
and decorator
eg:-1 2 3
    8 9 4
    7 6 5'''

spi = int(input('enter the range of spiral:'))
lst = []
lst2 = []
n = 3
for i in range(spi-1,0,-1):
    for j in range(n):
        lst.append(i)
    if n==3:
        n=2

lst.append(1)
lst2.append(1)
print(lst)
for i in lst:
    for j in range(i):
        lst2.append(j)

m = 1
k = 0
element = 1
for i in lst:
    for j in range(i):
        lst2[k] = element
        element += 1
        k += m
    if m == 1:
        m = spi
    elif m == -1:
        m = -spi
    elif m == -spi:
        m = 1
    else:
        m = -1

for i in range(1,len(lst2)):
   print(lst2[i-1],end=' ')
   if i%spi==0:
       print()







    
