''''1.You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code.
The sentence you want to encode is "the lazy dog jumped over the quick brown fox."
and the
output should be "vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."

I/P-"The lazy dog jumped over the quick brown fox."

O/P-"vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."'''

sen = "the lazy dog jumped over the quick brown fox."
alpha = 'abcdefghijklmnopqrstuvwxyz'
lst = []

for i in sen:
    if i == ' ':
        lst.append(' ')
    k = ord(i)+2
   
    for j in alpha:
        if ord(j) == k:
            lst.append(j)
            
print(''.join(lst))
print(type(ord('5')))
