
'''1. WAP to print middle charector of the string'''
##string = "strings"
##count= 0
##for i in string:
##    count= count+1
##print(count)
##middle = count//2+1
##find = 0
##for i in string:
##    find += 1
##    if find == middle:
##        print(i)



'''2. WAP to print half reverse of the string 

Input: KNOWLEDGE
Output: EGDELKNOW'''
##name = "KNOWLEDGE"
##string = name[4:][::-1]
##print(string+name[:4])


'''
3. WAP to remove all the vouels from the given string '''
##string = "vowelsofthe"
##vowels = "aeiou"
##for i in string:
##    if i not in vowels:
##        print(i,end= '')



'''
4. WAP to insert * in front of every vouels in the string.'''
##string = "vowelsin range"
##vowels = "aeiou"
##for i in string:
##    if i in vowels:
##        print("*",end='')
##    else:
##        print(i, end='')



'''
Input: BANANA
Output: B*AN*AN*A'''
##string = "BANANA"
##for i in string:
##    if i =="A":
##        print("*",end = "")
##    print(i,end = "")




'''
5. WAP to count number of words in the string.'''
##string = "ravindrareddy"
##count = 0
##for i in string:
##    count = count+1
##print(count)




'''
6. WAP to remove extra space from the given string '''
##string = "  ravindra   r eddy "
##for i in string:
##    if i != " ":
##        print(i,end = "")
##        




'''
7. WAP to insert string in between the given string
Input: Ojas technologies 
Output: Ojas innovative technologies '''
##string = "Ojas technologies"
##sub = "innovative"
##for i in string:
##    print(i,end="")
##    if i == " ":
##        print(sub,end=" ")



'''
8. WAP to find the ascci value of given char'''
##print("a".encode()[0])
##print("3".encode()[0])
##print("#".encode()[0])



'''
9. insert ojas in front of every string '''
##string = "ravindra"
##insert = "ojas"
##for r in string:
##    print(r,end = " ")
##    print(insert,end = " ")



'''
10. insert ojas in every extra space in the string '''
##string = "r a v i"
##insert = "ojas"
##for i in string:
##    print(i,end = "")
##    if i == " ":
##        print(insert,end = " ")
































































