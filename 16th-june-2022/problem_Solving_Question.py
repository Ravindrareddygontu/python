'''program:
write a program to merge characters of two strings into single string by taking characters alternatively.
Input:
Take any two strings(note:The string contains alpha numeric characters also)
ex:
s1=""
s2=""

Output:''program:

The output should be a single string such a way that input strings characters are printed alternatively.

Explanation:
For example,if the given string1 is "gopi" and string2 is "venkat".

The output should be "gvoepmikat"

Example1:

Sample Input:
priya12
45rohit
Sample Output:
p4r5iryoah1i2t'''

string1 = input("")

string2 = input("")

length = max(len(string1),len(string2))

for i in range(length):
   
    if i < len(string1):
        print(string1[i],end= "")
    if i < len(string2):
        print(string2[i],end="")



   
    
    
