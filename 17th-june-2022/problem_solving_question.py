'''Given a string S and a character C (as string of length 1), return a string with the characters surrounding any occurrence of C reversed. 
For example, if S is "Hello beautiful world" and C is a space, return "Hellb oeautifuw lorld" 

take input as a string with many words,seperated by spaces,swap the last character of 1st word and 1st character of the next word.

hint: split the string into a list and loop the list and write if condition for whitespaces where occured,
if condition is True then swap the last character of the word
with 1st character of the next word. 

ex1: input=" ravi teja kumar"
    output="ravt iejk aumar"

ex2: input="happy new year"
    output:happn yey wear"'''

string = "ravi teja kumar"
mylist = list(string)
count = 0

for i in mylist:
    count = count+1
    if i == " ":
        mylist[count-2],mylist[count] = mylist[count],mylist[count-2]
        
string2 = "".join(mylist)
print(string2)
