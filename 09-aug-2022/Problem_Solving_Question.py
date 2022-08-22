'''1) create a list of combinations of entered number like below
input: 5
list must be created as [4,4,4,3,3,2,2,1,1,1]
if input: 7
list must be created as [6,6,6,5,5,4,4,3,3,2,2,1,1,1]
first decending number and number 1 should be repeated three times'''

n = int(input('>:'))
m = 3
lst = []
for i in range(n-1,0,-1):
    for j in range(m):
        lst.append(i)
    if m==3:
        m=2

lst.append(1)
print(lst)

