'''=====================================================
atm pin code validation
======================================================
Write a function with the name validate_atm_pin_code that takes a word as argument.
ATM PIN is considered valid only if the given word contains
- Exactly 4 or 6 characters
- All the characters should be digits
Explanation:
For example, if the given word is “A289h4”, the output should be “Invalid PIN code”, though the given word contains exactly six characters, all the characters are not digits.
Whereas, if the given word is “A289h4”,the output should be “Invalid PIN code”, though the given word contains exactly the six characters, all the characters are not digits.
Input:
The input will be a single line containing a string.
Output:
The output should be a single line containing either “Valid PIN code”.
Sample input 1:
9837
Sample output 1:
Valid PIN Code
Sample input 2:
A289h4
Sample output2:
Invalid PIN Code'''

def my_function(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            print("Valid Pin")
        else:
            print("Invalid Pin")
    else:
        print("enter numbers only")

pin = input(" ")
my_function(pin)
