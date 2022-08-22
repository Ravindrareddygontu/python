'''Imagine a pager with only one button. For a letter "A", you press the button one times. For "B", you press it two times.
 For "Z", you press twenty six (26)times.
Given a string "S",print thee total number of times thr button should be pressed

Input:
The first line of input contains a string

Output:
The output should be a single integer denoting the total number of times the button is pressed.

Explanation:
For example,if the given string is Ramesh, Then
the total number of times the button pressed is r:18 a:1 m:13 e:5 s:19 h:8
18+1+13+5+19+8=64
The output should be 64
(Note:This is will be not case sensitive)
Example1:
Sample Input:
usha
Sample Output:
49
Example2:
Sample Input:
tejeshwari
Sample Output:
128
Example1:
Sample Input:
bazequa
Sample Output:
73'''
alphabets = 'abcdefghijklmnopqrstuvwxyz'
string = input(" ").lower()
count = 0
total = 0

for i in alphabets:
    count += 1
    for j in string:
        if i == j:
            total = total + count
    
print(total)
