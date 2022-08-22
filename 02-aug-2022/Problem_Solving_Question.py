'''Polynomial

Given polynomial, write a program that prints
polynomial in Cix^Pi + Ci-1x^Pi-1 + ... + C1x + CO
format.

Input
The first line contains a single integer N.
Next N lines contain two integers Pi, Ci
separated with space, where Pi denotes power
and Ci denotes coefficient of Pi.

Output
Print the polynomial in the format Cix^Pi + Ci-
1x^Pi-1 + ... + C1x + CO, where Pi's are powers
in decreasing order, Ci is coefficient, and CO is
constant. There will be space before and after
the plus or minus sign.
If the coefficient is zero, then don't print the
term.
If the term with the highest degree is negative,
in decreasing order, Ci is coefficient, and CO is
constant. There will be space before and after
the plus or minus sign.
If the coefficient is zero, then don't print the
term.
If the term with the highest degree is negative,
the term should represent -Cix^Pi.
For the term where power is 1, represent it as
C1x instead of C1x^1.
If the polynomial degree is zero and the
constant term is also zero, then print 0 to
represent the polynomial.
For term Cix^Pi, if the coefficient of the term Ci
is 1, print x^Pi instead of 1x^Pi.

Explanation
If N = 4
For power 0, the coefficient is 5
For power 1, the coefficient is 0
For power 2, the coefficient is 10
For power 3, the coefficient is 6.
Then polynomial represents "6x^3 + 10x^2 + 5"
For power 2, the coefficient is 10
For power 3, the coefficient is 6.
Then polynomial represents "6x^3 + 10x^2 + 5"
Constraints
N <= 100
0 <= Pi < 1000
-1000 <= Ci <= 1000

Sample Input
4
0 5
10
2 10
36

Sample Output
6x^3 + 10x^2 + 5'''
n = int(input('>:'))
k = ''
while n>1:
    m = (input('>:'))
    k = k+f'{m}x^{n} +'
    n -= 1
print(k[:-1])






