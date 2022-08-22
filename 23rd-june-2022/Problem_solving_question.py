'''first you have to create the diagram by using nested for loops and symbol(| |) to repeat for 9 times
3 in a row and 3 in a column as shown in below
diagram = | |  | |  | |
          | |  | |  | |
          | |  | |  | |
then:
user has to enter 9 numbers randomly in the input
if user entered "1" it has to be filled in the first position of the diagram like this
|1| | | | |
| | | | | |
| | | | | |
if user entered second number "6" then :
|1| | | | |
| | | | |6|
| | | | | |
like that user has to enter total numbers of 9 and fill in the diagram as shown in below
|1| |2| |3|
|4| |5| |6|
|7| |8| |9|
if user enter other than 1-9 numbers you had to give "please enter numbers between 1 to 9" message in the output'''
mylist = []
game = 9
while game>0:
    user = int(input(">: "))
    mylist.append(user)
    for i in range(1,10):
        if i in mylist:
             print(f"|{i}|", end=" ")
        else:
            print(f"| |",end=" ")
        if i%3==0:
            print()
    game -= 1

