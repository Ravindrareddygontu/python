'''#capitalize()
capitalize method returns first character to be upper and remaining all are lowercase'''
##string = "hello WOrld"
##print(string.capitalize())

'casefold()'
##string = "hellO woRld"
##casefold = string.casefold()
##print(casefold)

'center'
##string = "hello"
##center = string.center(9,"o")
##print(center)

'count'
##string = "hello world"
##count = string.count("l",3,6)
##print(count)

'encode'
##string = "welcomae"
##encode = string.encode(encoding = "ascii" ,errors = "namereplace")
##print("encode of a string is: ",encode)

'endswith'
##string = "what are you talking"
##end = string.endswith("you",1,12)
##print(end)

'expandtabs'
##string = "h\te\tl\tl\ao"
##print(string.expandtabs())
##print(string.expandtabs(2))
##print(string.expandtabs(6))

'find()'
##string = "welcome to the world"
##find = string.find("e",5,10)
##print(find)
##print(string.find("w",1))

'format()'
##string = "pi value is {n:<5f}"
##print(string.format(n = 3.14))
##string = "For only {price:.2f} dollars!"
##print(string.format(price = 49))
##txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
##txt2 = "My name is {0}, I'm {1}".format("John",36)
##txt3 = "My name is {}, I'm {}".format("John",36)
##print(txt1,txt2,"\n",txt3)

'format_map'
##n = 6
##string = "hello {n}world"
##print(string.format_map)

'index()'
##string = "welcome to the world"
##print(string.index("w"))
##print(string.index("w",2))
##print(string.index("t",5,9))

'isalnum()'
##string = "index123@"
##print(string.isalnum())

'isalpha()'
##string = "she12iscoming"
##print(string.isalpha())

'isascii()'
##string = "ascii\n values"
##print(string.isascii())

'isdecimal()'
"this method is used on unicode values"
##string = "\u0033"#unicode for 3
##print(string.isdecimal())
##string = "\u0047"#unicode for G
##print(string.isdecimal())

'isdigit()'
##string = "123rt"
##print(string.isdigit())
##string = "573985793"
##print(string.isdigit())

'isidentifier()'
##string = "3helloworld"
##string2 = "hello_world"
##string3 = "hello world"
##print(string.isidentifier())
##print(string2.isidentifier())
##print(string3.isidentifier())


'islower()'
##string = "hello world"
##string2 = "Hello World"
##print(string.islower())
##print(string2.islower())

'isnumeric()'
##a = "\u0030" #unicode for 0
##b = "\u00B2" #unicode for &sup2;
##c = "10km2"
##d = "-1"
##
##print(a.isnumeric())
##print(b.isnumeric())
##print(c.isnumeric())
##print(d.isnumeric())

'isprintable()'
"printables are all except escape sequences(\n, \t) like that"
##string = "welcome to the world"
##print(string.isprintable())
##string = "welcome to the \nworld"
##print(string.isprintable())

'isspace()'
"returns true if string is contains only white spaces"
##string = "     "
##print(string.isspace())
##string2 = "     r   "
##print(string2.isspace())#becomes false

'istitle()'
"returns true if all words starting with a capital letter"
##string = "Welcome To The World"
##print(string.istitle())
##string2 = "welcome to the World"
##print(string2.istitle())#becomes false


'isupper()'
##string = "Hello WOrld"
##string2 = "HELLO WORLD"
##
##print(string.isupper())#returns false
##print(string2.isupper())

'join()'
##string = "hello world"
##string2 = "h "
##print(string2.join(string))

'ljust()'
##txt = "banana"
##
##x = txt.ljust(10)
##
##print(x, "is my favorite fruit.")
##txt = "banana"
##
##x = txt.ljust(20, "O")
##
##print(x)

'maketrans'
##txt = "Hello Sam!"
##mytable = txt.maketrans("S", "P")
##print(txt.translate(mytable))

'partition()'
##"it splits where given element of first occurance"
##string = "hello welcome to the  world"
##string2 = "welcome to the python to the code"
##
##print(string.partition("to"))
##print(string2.partition("to"))

'replace()'
##string = "i like apples and imangoes"
##print(string.replace("i","l"))#replace all i's
##print(string.replace("i","l",2))#replace only 2 i's

'rfind'
"it finds the index of the given char if doesn't exit it returns -1 and rindex returns error"
##string = "i am the new engineer here"
##print(string.rfind('r'))
##print(string.rfind('r',5,10))


'rindex'
"same as rfind but if value doesn't exit it returns error"
##string = "basics of the python we learn"
##print(string.rindex("a"))
##print(string.rindex("a",0,10))

'rjust'
"returns justified version of the word"
##string = "python"
##print(string.rjust(7))
##print(string.rjust(9,"o"))

'rpartition'
##string = "i would like to go to the  city"
##print(string.rpartition('to'))
##print(string.rpartition("o"))

##string = "     i am liking it    t"
##print(string.rstrip())

'rstrip'
"it removes the whitespaces in the left"
##string = "     i am liking it    t"
##print(string.rstrip())

'rsplit'
"it returns a list"
##string = "it is reversed order"
##print(string.rsplit(" "))
##print(string.rsplit(" ",1))#return two list elements

'split'
##string = "iam, the basic, programmer ,in the room"
##print(string.split(","))
##print(string.split(",",1))

'splitlines'
"it will split into list when a new line occurs"
##string = "music is the best\nmedicine"
##print(string.splitlines())


'swapcase'
"it will return capital in to small letters and viceverse"
##string = "welcoMe"
##print(string.swapcase())

'title'
"make every first char capital in every word "
##string = "welcome to the Elephat coutn"
##print(string.title())

'translate'
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
##mydict = {83:  80}
##txt = "Hello Sam!"
##print(txt.translate(mydict))

'upper'
##string = "element FOr the word"
##print(string.upper())

'zfill'
"zfill add the zeros at the beginning of the string until required length is reached"
##string = "zebra"
##a = "hello"
##b = "welcome to the jungle"
##c = "10.000"
##print(string.zfill(8))
##print(a.zfill(10))
##print(b.zfill(10))
##print(c.zfill(10))
