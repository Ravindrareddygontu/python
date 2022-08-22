'''1. How would you confirm that 2 strings have the same identity?'''
##a = 10
##b = 10
##if id(a) == id(b):
##     print("same identity")
##else:
##    print("no identity")


'''2. How would you check if each word in a string begins with a capital letter?'''
##string = "My Name Is Ravindra Reddy"
##print(string.istitle())


'''3. Check if a string contains a specific substring'''
##string = "My Name Is Ravindra Reddy"
##substring = "Reddy"
##if substring in string:
##    print("string having substring")
##else:
##    print("string doesn't have a substring")
    

'''4. Find the index of the first occurrence of a substring in a string'''
##string = "My Name Is Ravindra Reddy"
##substring = "Reddy"
##print("first occurance of substring in a string is: ",string.find(substring))


'''5. Count the total number of characters in a string'''
##string = "My Name Is Ravindra Reddy"
##print("total number of characters in a string are: ",len(string))


'''6. Count the number of a specific character in a string'''
##string = "My Name Is Ravindra Reddy"
##character = input("enter a character: ")
##print("no.of characters in a string are: ",string.count(character))


'''7. Capitalize the first character of a string'''
##string = "my name is ravindra reddy"
##print(string.capitalize())


'''8. What is an f-string and how do you use it?'''
##a = 0
##b = 1
##print(f'given numbers are {a},{b}')

'''9. Search a specific part of a string for a substring'''
##string = "my name is ravindra reddy"
##substring = "name"
##result = string.find(substring)
##if result:
##    print("string has a substring")
    

'''10. Interpolate a variable into a string using format()'''
##string = "my name is ravindra {name} my age is {age}"
##a = 25
##b = "reddy"
##print(string.format(name=b,age = a))


'''11. Check if a string contains only numbers'''
##string = "1235725"
##print(string.isdigit())



'''12. Split a string on a specific character'''
##string = "my name is, ravindra ,reddy"
##character = ","
##print(string.split(character))


'''13. Check if a string is composed of all lower case characters'''
##string = "my name is, ravindra ,reddy"
##if(string.islower()):
##    print("string is having all lower characters")
##else:
##    print("string is not having all lower characters")

'''14. Check if the first character in a string is lowercase'''
##string = "my Name is rajesh"
##for i in string:
##    if i == i.lower():
##        print("first character is lowercase")
##        break
##    else:
##        print("first character is not a lowercase")
##        break


'''15. Can an integer be added to a string in Python?'''
##print("no, we cannot add integer to a string in python")


'''16. Reverse the string “hello world”'''
##string = "hello world"
##print(string[::-1])


'''17. Join a list of strings into a single string, delimited by hyphens'''
##list = ["gatathri", "reddy", "sravani", "tarak"]
##string = "-"
##print(string.join(list))


'''18. Check if all characters in a string conform to ASCII'''
##string = "ascii"
##print(string.isascii())



'''19. Uppercase or lowercase an entire string'''
##string = "hello world"
##print(string.upper())
'''
20. Uppercase first and last character of a string'''
##string = "hello world"
##first = string[0].upper()
##last = string[-1].upper()
##print(first+string[1:-1]+last)
'''
21. Check if a string is all uppercase'''
##string = "hello world"
##print(string.isupper())
'''
22. When would you use splitlines()?'''
##string = "welcome to the \rojas and enjoy\nthe evening"
##print(string.splitlines())
##print(string.splitlines(True))

'''
23. Give an example of string slicing'''
##string = "ojasit"
##print(string[1:5])

'''
24. Convert an integer to a string'''
##integer = 6
##string = str(integer)
##print(type(string))
##print(type(integer))



'''
25. Check if a string contains only characters of the alphabet'''
##string = "ojasit5"
##print(string.isalpha())


'''
26. Replace all instances of a substring in a string'''
##string = "welcome to the it industry to the ojas"
##substring = "what"
##print(string.replace("it",substring))



'''
27. Return the minimum character in a string'''
##string ="welcome to the it industry"
##list = []
##for i in string:
##    j = ord(i)
##    list.append(j)
##print(min(list))
    

'''
28. Check if all characters in a string are alphanumeric'''
##string = "alpha394"
##print(string.isalnum())



'''
29. Remove whitespace from the left, right or both sides of a string'''
##string = "     welcome to the world    "
##print(string.strip())



'''
30. Check if a string begins with or ends with a specific character?'''
##string = "fjoenogo"
##char = "f"
##if string[0] == char or string[-1] == char:
##    print("yes")
##else:
##    print("no")









































































































































































