'''1.How do you print duplicate characters from a string?'''
##string = "ravindra gontyu reddy"
##string2 = ""
##for i in string:
##    count = 0
##    for j in string:
##        if i == j:
##            count += 1
##    if count>=2:
##         string2 = string2 + i
##string3 = ""
##for i in string2:
##    if i not in string3 and i != " ":
##        string3 = string3 + i + " "
##print(f"duplicates in a given string are '{string3}'")


'''2.How do you find all the permutations of a string?'''
##string = "123"
##order = 0
##for i in string:
##    order = order + ord(i)
##list = ((a,b,c) for a in string for b in string for c in string)
##for a,b,c in list:
##    if a != b and b != c and c!=a:
##        print(a,b,c)

   

'''
3.How can a given string be reversed using recursion? '''
##string = "hello world"
##for i in reversed(range(len(string))):
##    print(string[i],end = "")



'''
4.How do you check if a string contains only digits?'''
##string = "123456423523523"
##nums = "1234567890"
##count = 0
##for i in string:
##    if i in nums:
##        count += 1
##if count == len(string):
##    print("string having all digits")
##else:
##    print("string not having all digits")



'''
5.How do you print the first non-repeated character from a string?'''
##string = "hello worledh"
##for i in string:
##    counter = 0
##    for j in string:
##        if i==j:
##            counter += 1
##    if counter==1 and i != " ":
##        print("first non-repeated charcter in string is: ",i)
##        break
        


'''
6.How do you check if two strings are a rotation of each other?( check if two String is an anagram of each other)'''
##string = "mnai"
##string2 = "maan"
##counter = 0
##count = 0
##for i in string:
##    if i in string2:
##        count = count +1
##for k in string2:
##    if k in string:
##        counter += 1
##if count == counter:
##    print("given strings are anagrams")
##else:
##    print("givne strings are not anagrams")
        

'''
7.Check if the string is anagram or not , if not make it anagram.'''
##string = "abbadfsfd"
##string2 = "abbdcksddfhkfhkau"
##count = 0
##string3 = ""
##counter = 0
##for i in string:
##    if i in string2:
##        count += 1
##for j in string2:
##    if j in string:
##        counter += 1
##if count == counter and len(string) == len(string2):
##    print("strings are anagrams")
##else:
##    for i in string2:
##        if i in string:
##            string3 = i+string3
##string2 = string3
##print(string2)

            
            


'''
8.Given string str, How do you find the longest palindromic substring in str?'''
##string = "hello world radar malayalam ridir python"
##string2 = ""
##count = 0
##counter = 0
##max = 0
##string3 = ""
##for i in string:
##    count  += 1
##    if i == " ":
##        string2 = string[counter:count-1]
##        counter = count
##        if string2 == string2[::-1]:
##            add = 0
##            for i in string2:
##                add = add+1
##            if max < add:
##                max = add
##            if max == add:
##                string3 = string2[:max]
##print(string3)
            


'''
9.How do you remove a given character from String? '''
##string = "hello world"
##char = "l"
##for i in string:
##    if i != char:
##        print(i,end= "")



'''
10.How do you find the length of the longest substring without repeating characters'''
##string = "hello worldl to the placedwi of codingzav"
##string = string + " "
##count = 0
##string2 = ""
##counter = 0
##max = 0
##string4 = ""
##for i in string:
##    count += 1
##    if i == " ":
##        string2 = string[counter:count-1]
##        counter = count
##        string3 = ""
##        for i in string2:
##            add = 0
##            coun = 0
##            for j in string2:
##                if i == j:
##                    add += 1
##            if add == 1:
##                string3 = string3+i
##            if string3 ==string2:
##                for i in string3:
##                    coun = coun + 1
##                if max < coun:
##                    max = coun
##                if(max == coun):
##                   string4 = string3[:coun]
##print(f"the longest substring without repeating characters is: '{string4}'")









