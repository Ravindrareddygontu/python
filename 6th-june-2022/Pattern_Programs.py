'''1. Write a program to print the following Patterns
  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5'''
##string = '1 2 3 4 5'
##for i in range(5):
##    print(string)




'''2.Write a program to print the following Pattern
  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1''' 
##string = '5 4 3 2 1'
##for i in range(5):
##    print(string)





'''3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1'''
##string = '54321'
##for i in string:
##    print(5*i)





'''4.Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5'''
##string = '12345'
##for i in range(1,len(string)+2):
##    for j in range(1,i):
##        print(j,end=' ')
##    print()





'''5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5'''
##string = '12345'
##for i in range(len(string)+1):
##    for j in range(i):
##        print(i,end=' ')
##    print()





'''6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15'''

##k = 1
##for i in range(6):
##    for j in range(i):
##        print(k,end = ' ')
##        k += 1
##        
##    print()





'''7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1'''
##k =6
##for i in range(6):
##    for j in range(i):
##        print(k,end = ' ')
##    k -=1
##    print()




'''8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9 '''
##for i in range(6):
##    for j in range(i):
##        print(i,end=' ')
##        i +=1
##    print()




'''9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O'''
##strings = 'ABCDEFGHIJKLMNO'
##k = 0
##for i in range(6):
##    for j in range(i):
##        print(strings[k],end = ' ')
##        k = k+1
##    print()





'''10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * *'''
##for i in range(5):
##    print(5*'* ')




'''11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * '''
##for i in range(6):
##    for j in range(i):
##        print(j*'*',end=' ')
##    print()



    
'''12.Write a program to print the following Pattern
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * '''
##n = 5
##print(n*'* ')
##for i in range(n-1):
##    print('*',(n-2)*'  '+'*')
##print(n*'* ')
    

'''13.Write a program to print the following Pattern
          * 
        * * * 
      * * * * * 
    * * * * * * *'''
##n = 7
##for i in range(1,8,2):
##    print(n*' ',i *'* ')
##    n = n-2



'''14.Display Multiplication Table in given range using Nested for loops'''
##num = 5
##rang = 10
##for i in range(rang):
##        print(num , '*' , i ,'=' , num*i)



'''15.Display Prime Numbers in the given range using nested for loops '''
##first = int(input("enter first range: "))
##second = int(input("enter second range: "))
##for prime in range(first,second):
##    for div in range(2,prime):
##        if prime%div == 0:
##            break
##    else:
##        print(prime)



'''16.Write a program to print the following Pattern
	          1
              3  2
       6   5   4
10  9   8   7'''
##m = 0 
##y = 12
##n = 0
##k = 1
##for i in range(1,5):
##    print(y*" ",end = " ")
##    y = y-4
##    m = 1+n
##    k = k+1
##    n = n+k
##    for j in range(i):
##        print(m,end = " ")
##        m = m -1
##    print()
   
   


'''17.Write a program to print the following Pattern
10  9  8   7
      6   5  4
           3  2
               1'''
##m = 10
##y = 0
##for i in range(4,0,-1):
##    print(y*"  ",end = "")
##    y += 3
##    for j in range(i):
##        print(m,end = "  ")
##        m = m-1
##    print()




















